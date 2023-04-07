import requests as rq
import pandas as pd
import os
from bs4 import BeautifulSoup as bs

def get_url_lists():
    url= 'http://www.tianqihoubao.com/lishi/lengshuijiang/month/201101.html'
    header= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }
    data= rq.get(url,header)
    soup= bs(data.text,'lxml')
    list= soup.find(class_= 'months').find_all('a')
    lists= []
    for l in list:
        lists.append('http://www.tianqihoubao.com'+ l.get('href'))
    return lists
get_url_lists()

def get_page_data():
    # for url in urls:
    url= 'http://www.tianqihoubao.com/lishi/lengshuijiang/month/201101.html'
    header= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }
    data= rq.get(url,header)
    soup= bs(data.text,'lxml')
    page_name= soup.find('h1').text.strip()
    all_data= soup.find('table')
    page_data= []
    df= pd.read_html(all_data)
    print(df)
    return
    for data in all_data:
        print(data.find('tr'))
        # page_data.append(data.find('td').text.strip())

        
    p_name= page_name.strip()[-8:]
    print(page_data)
        
    with open(f'{page_name}.csv','w',encoding='utf-8')as f:
        f.write(str(page_data))
    print(f'{p_name}已经下载完成')
        
        
    # return print('列表下载完成。')
get_page_data()