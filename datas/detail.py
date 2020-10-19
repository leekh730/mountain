from pymongo import MongoClient
from folium import plugins, IFrame
import folium, pandas, base64

df = pandas.read_csv('mtngps.csv', encoding='utf-8') # read csv file

m = folium.Map(location=[36.7,127.9], zoom_start=15)
for i, row in df.iterrows():
    name = row['C_name']
    lon = row['C_gps1']
    lan = row['C_gps2']
    tooltip = 'Click!'
    html = folium.Html(name,script=True)
    popup = folium.Popup(html, max_width=500)
    folium.Marker([lon, lan], popup=popup, icon=folium.Icon(icon='star'), tooltip=tooltip).add_to(m)

    # html = folium.Html(row['C_name'],script=True)
    # popup = folium.Popup(html, max_width=500)
    # folium.Marker([row['C_gps1'], row['C_gps2']], popup=popup, icon=folium.Icon(icon='star'), tooltip=tooltip).add_to(m)

minimap = plugins.MiniMap()
m.add_child(minimap)

m.save('maps.html')


# name = df['C_name']
# lat = df['C_gps1']
# lon = df['C_gps2']


# for i in zip(df['C_name'], df['C_gps1'], df['C_gps2']):
#     folium.Marker([i]).add_to(m)
#     print(m)

# print(m)

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
