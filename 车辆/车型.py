import requests as rq
from bs4 import BeautifulSoup as bs
import os


def car():
    url= 'https://car.yiche.com/xuanchegongju/?p=0-5#anchorTitle'
    head= {
        'Referer': 'https://www.yiche.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    alllist= rq.get(url,headers=head)
    # print(alllist.content)
    soup= bs(alllist.content,'html.parser')
    lists= soup.find_all('div',class_= 'search-result-list-item')
    file= []

    for list in lists:
        名称= list.find('a').find('p').text
        价格= list.find(class_= 'cx-price').text
        file.append(f"{名称}:{价格}/")

    with open('car.txt','a',encoding='utf-8')as ss:
        ss.writelines(file)
        
        

car()
file= os.listdir()
print(file)