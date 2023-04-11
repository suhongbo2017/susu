# import requests as rq
# import pandas as pd
# import os
# from bs4 import BeautifulSoup as bs
# import time
# # def get_url_lists():
# #     url= 'http://www.tianqihoubao.com/lishi/lengshuijiang/month/201101.html'
# #     header= {
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
# #     }
# #     data= rq.get(url,header)
# #     soup= bs(data.text,'lxml')
# #     list= soup.find(class_= 'months').find_all('a')
# #     lists= []
# #     for l in list:
# #         lists.append('http://www.tianqihoubao.com'+ l.get('href'))
# #     return lists
# # ur= get_url_lists()

# def get_page_data():
#     url= 'http://www.tianqihoubao.com/lishi/lengshuijiang/month/201610.html'
#     header= {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
#     }
#     # data= rq.get(url,header)
#     # # time.sleep(0.5)
#     # soup= bs(data.text,'lxml')
#     # list= soup.find(class_= 'months').find_all('a')
#     # lists= []
#     # for l in list:
#     #     lists.append('http://www.tianqihoubao.com'+ l.get('href'))
#     # for url in lists:
#     data= rq.get(url,header)
#     soup1= bs(data.text,'lxml')
#     page_name= soup1.find('h1').text.strip()
#     names= os.listdir()
#     if f'{page_name}.csv' in names:
#         print(f'{page_name}已经存在')
#     else:
#         df= pd.read_html(url,encoding='gb2312')
#         df[0].to_csv(f'{page_name}.csv',index=False)
#         print(f'{page_name}下载完成')
# get_page_data()
# print('全部下载完成')

print(148//12)
