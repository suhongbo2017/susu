import requests as rq
from bs4 import BeautifulSoup as bs
import os
import time
import re

url= 'http://www.177pica.com/html/category/tt/page/2/'
header= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

def get_urls():
    '''获取页面上的h2标签下a标签的href链接,并返回一个包含名称与链接的字典'''
    all= rq.get(url,headers=header)
    soup= bs(all.content,'lxml')
    # print(soup)
    data= soup.find_all(class_="picture wow fadeInUp")
    datas={}
    for link in data:
        
        link_name= link.find('h2').text
        link_href= link.find('a').get('href')
        # print(link_name,'\n',link_href)
        datas[link_name]= link_href
    # print(datas)
    return datas

        

page_link= get_urls()
# print(page_link)
def get_folder(page):
    for pa in page.keys():
        path= os.chdir(r'E:\mapinfo\下载器')
        if not (pa in os.listdir(path)):

            os.mkdir(pa)

            print(f'{pa}新建完成')
        else:
            print(f'{pa}已经存在')
        
        # print(page[pa])

get_folder(page_link)

def get_pagelink(page_link):
    for folder in page_link.keys():
        path= os.chdir(f'E:/mapinfo/下载器/{folder}')
        print(f'进入{path}下。')
        url= page_link[folder]
        data= rq.get(url,headers=header)
        soup= bs(data.content,'lxml')
        links= soup.find(class_= 'page-links').find_all('a')
        num= len(links)

        for i in range(1,num):
            page_url= url + '/' + str(i)
            print(f'{page_url}开始下载')
            page_data= rq.get(page_url,headers=header)
            page_soup= bs(page_data.content,'lxml')
            datas= page_soup.find(class_="single-content").find_all('p')
            for pics in datas:
                pic= pics.find('img').get('data-lazy-src')                    
                pic_name= re.search(r'/([^/]+)$',pic).group(1)
                picdata=rq.get(pic,headers=header)
                lists= os.listdir(path)
                if pic_name not in lists:
                    with open(f'{pic_name}','wb')as p:                       
                        p.write(picdata.content)
                        print(f'文件{pic_name}下载成功')
                        time.sleep(0.5)
                else:
                    print(f'{pic_name}已存在。')
            print(f'{folder}下载完成')

                
                    


get_pagelink(page_link)










