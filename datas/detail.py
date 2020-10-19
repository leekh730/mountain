from pymongo import MongoClient
from folium import plugins, IFrame
import folium, base64
import pandas as pd

# csv, pandas를 이용하여 folium 시각화 방법
df = pd.read_csv('mtngps.csv', encoding='utf-8') # read csv file
# df.shape # (100,3) 100개의 행과 3개의 열로 이루어졌다는 것을 확인
# df.head() # 데이터 위에서부터  미리보기
m = folium.Map(location=[36.70,127.90], zoom_start=8) # map을 열었을때의 시작 화면, list html과 연결하기
html = "<img src='1.jpg'><b>한라산</b>"

# iterrrows()함수보다 apply()함수(+lamda)가 data처리가 더 빠름
for index, row in df.iterrows(): # pandas for문, iterrows는 dataframe의 행을 나타냄
    tooltip = 'Click!'
    #html = folium.Html(row['C_name'],script=True) # popup을 html로 열고, dataframe에 각 열의 name 값 불러오기
    #html = folium.Html(row['C_name'],script=True) # popup을 html로 열고, dataframe에 각 열의 name 값 불러오기
    iframe = IFrame(html=html, width='40', height='40')
    popup = folium.Popup(html, max_width=500)
    folium.Marker([row['C_gps1'], row['C_gps2']], popup=popup, icon=folium.Icon(icon='star'), tooltip=tooltip).add_to(m) # dataframe에 각 열의 위도,경도 값 불러오기

minimap = plugins.MiniMap() # minimap 추가
m.add_child(minimap)

m.save('maps.html') # html로 저장


# for i in zip(df['C_name'], df['C_gps1'], df['C_gps2']):
#     folium.Marker([i]).add_to(m)
#     print(m)

# print(m)
# mongodb database를 이용하여 folium 시각화 방법
# client = MongoClient('mongodb://127.0.0.1:27017')
# db = client.mtlist1 # mtlist 데이터베이스에 접속
# datas = list(db.mountain1.find()) # Dict타입을 List타입으로 전환 후 mountain이라는 collection에 접속

# # print(datas[0]['이름']) # datas list에 첫번째 값의 이름(key) value 값 출력
# # print(datas[0]['내용'])
# # print(datas[-1]['좌표'])


# for i in range(0, 4):
#     # dt_frame = pandas.DataFrame({
#     #     '이름':[i],
#     #     '좌표':[i],
#     # })
#     # db_name = datas[i]['이름']
#     # db_gps = datas[i]['좌표']
#     # xy = db_gps.split(',')
#     # print(db_name, db_gps)
#     # x = xy[0]
#     # y = xy[1]

#     tooltip = 'Click!'
#     m = folium.Map(location=[x,y], zoom_start=10)
#     folium.Marker(location=[x.y], popup=db_name, tooltip=tooltip).add_to(m)

    

# print(m)
