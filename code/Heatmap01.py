# _*_ coding: utf-8 _*_
__author__ = 'xbr'
__date__ = '2019/1/9 15:47'

import numpy as np
import pandas as pd
import folium
import webbrowser
from folium.plugins import HeatMap


# 读取csv文件,以Dataframe形式保存
df = pd.read_csv(r"D:\data\PM25-20180101.csv")
# 获取数据个数
num = df.shape[0]
# 获取纬度
lat = np.array(df["lat"][0:num])
# 获取经度
lon = np.array(df["lon"][0:num])
# 获取PM2.5，转化为numpy浮点型
pm25 = np.array(df["PM25"][0:num], dtype=float)
# 将数据制作成[lats, lons, weights]的形式
data = [[lat[i], lon[i], pm25[i]] for i in range(num)]
# 绘制Map，中心经纬度[32, 120],开始缩放程度是5倍
map_osm = folium.Map(location=[32, 120], zoom_start=5)
# 将热力图添加到前面建立的map里
HeatMap(data).add_to(map_osm)

file_path = r"D:\AirQualityMap.html"
# 保存为html文件
map_osm.save(file_path)
# 默认浏览器打开
webbrowser.open(file_path)
