import requests as rq
import pandas as pd
import json


df= pd.read_excel('H:\VSCODE\susu\pop_test\city_code.xlsx')
print(df[['中文名']:['adcode']])
api= '649085fda21f180a24d5336b93491a71'
城市= '东莞市'

# url= f'https://restapi.amap.com/v3/weather/weatherInfo?city={city}&key={api}