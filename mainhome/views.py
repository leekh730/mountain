from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
# For folium Modules
from folium import plugins
from folium.plugins import MarkerCluster
import folium
import pandas as pd
# Paginator
from django.core.paginator import Paginator

def test(request):
    return HttpResponse("Start Project!") # django 제대로 실행 여부 확인용

def home(request):
    return render(request, 'hello/home.html')

def mountainlist(request):
    data = request.GET.copy()
    with MongoClient('mongodb://127.0.0.1:27017/') as client:
        mountain = client.mountain
        result = list(mountain.sampleCollection.find({}))
        # for info in result:
        #     print(type(info),info)
    paginator = Paginator(result,10) # show 10 contents per page
    page_number = request.GET.get('page',1)
    data['page_obj'] = paginator.get_page(page_number)
    return render(request, 'main/mountainlist.html', context=data)
    
def f_maps(request):
    with MongoClient('mongodb://127.0.0.1:27017/') as client:
        client = MongoClient('mongodb://127.0.0.1:27017')
        db = client.mountain # mountain 데이터베이스에 접속
        df = pd.DataFrame(db.sampleCollection.find()) # dataFrame타입으로 전환 후 sampleCollection이라는 collection에 접속
        #print(df.dtypes) # dataframe columns type check
        df['address_1']=df['address_1'].astype(float) # address_1 column type이 기존 object여서 float으로 변경
        df['address_2']=df['address_2'].astype(float) # address_2 column type이 기존 object여서 float으로 변경
        m = folium.Map(location=[36.70,127.90], zoom_start=8) # map을 열었을때의 시작 화면
        # iterrrows()함수보다 apply()함수(+lamda)가 data처리가 더 빠름
        marker_cluster = MarkerCluster().add_to(m)
        for index, row in df.iterrows(): # pandas for문, iterrows는 dataframe의 행을 나타냄
            tooltip = 'Click!'
            html = f"""
            <header>
                <h3>{row['class_']}</h3>
            </header>
            <body>
                <table>
                    <tr>
                        <td><img src ={row['img_data'][2]} width='100' height='100'></td>
                        <td>
                            <p style="font-size:15px">
                            &nbsp;
                            {row['address_1']}
                            {row['address_2']}
                            </p>
                            <p style="font-size:15px">
                            &nbsp;
                            날씨 : {row['weather_data']}
                            </p>
                            <p style="font-size:15px">
                            &nbsp;
                            풍속 : {row['wind_data']}
                            </p>
                        </td>
                    </tr>
                </table>
            """
            html = folium.Html(html,script=True, width=300, height=150) # popup을 html로 열기
            popup = folium.Popup(html=html, max_width='100%')
            folium.Marker([row['address_1'], row['address_2']], popup=popup,  icon=folium.Icon(icon='star'), tooltip=tooltip).add_to(marker_cluster) # dataframe에 각 열의 위도,경도 값 불러오기

        minimap = plugins.MiniMap() # minimap 추가
        m.add_child(minimap)
    m = m._repr_html_
    return render(request, 'maps.html')

def detail(request):
    # http://127.0.0.1:8000/detail/?lat=36.7066013257&lon=126.60836041
    # request.GET['lat'], request.GET['lon']
    with MongoClient('mongodb://127.0.0.1:27017/') as client:
        client = MongoClient('mongodb://127.0.0.1:27017')
        db = client.mountain # mountain 데이터베이스에 접속
        df = pd.DataFrame(db.sampleCollection.find()) # dataFrame타입으로 전환 후 sampleCollection이라는 collection에 접속
        #print(df.dtypes) # dataframe columns type check
        df['address_1']=df['address_1'].astype(float) # address_1 column type이 기존 object여서 float으로 변경
        df['address_2']=df['address_2'].astype(float) # address_2 column type이 기존 object여서 float으로 변경
        m = folium.Map(location=[37.87137778,127.9564694], zoom_start=8) # map을 열었을때의 시작 화면
    m = m._repr_html_

    return render(request, 'detail.html')
