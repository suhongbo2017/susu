'''
对dataframre的查找进行熟悉与灵活应用的练习，使用尽可能多的方法。
'''
import pandas as pd
import requests as rq
import json


data= pd.read_excel(r'D:\vscode\susu\susu\susu\pandas学习\AMap_adcode_citycode_20210406.xlsx')
print(type(data))
data.set_index('中文名',inplace=True)
city_name= input('请输入要查询的城市名称(如‘北京市，河北省’):')
city_code= int(data.loc[city_name,'adcode'])
weather_api= '649085fda21f180a24d5336b93491a71'
weather_url= f'https://restapi.amap.com/v3/weather/weatherInfo?city={city_code}&key={weather_api}&output=json&extensions=base'
weather_data= rq.get(weather_url)
weather_info= weather_data.text
new_info= json.loads(weather_info)
print(type(new_info))
print(new_info)
省= new_info['lives'][0]['province']
市= new_info['lives'][0]['city']
城市代码= new_info['lives'][0]['adcode']
天气= new_info['lives'][0]['weather']
气温= new_info['lives'][0]['temperature']
风向= new_info['lives'][0]['winddirection']
风力等级= new_info['lives'][0]['windpower']
湿度= new_info['lives'][0]['humidity']
print(f'''
{省}省,
{市},
----------------
即时天气
----------------
天气情况：{天气},
气温：{气温},
风向：{风向},
风力{风力等级},
空气湿度：{湿度}
----------------
''')




# 单个查找



# 切片查找
# 条件查找
