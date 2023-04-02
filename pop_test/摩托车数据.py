import requests as rq
import pandas as pd
from bs4 import BeautifulSoup as bs
import time

url= 'https://www.mtchome.com/brand/'
header= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

print(22233)
# data= rq.get(url,headers=header)
# all_data= bs(data.content,'lxml')
# print(all_data)
