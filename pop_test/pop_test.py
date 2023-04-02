import requests 
from bs4 import BeautifulSoup as bs


url= 'http://www.jiche.com/Ducati/chexing.html'
# print(url)
header= {
    'Referer': 'http://www.jiche.com/Ducati/chexing.html',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
# def get_url():
#     try:
#         response = requests.get(url)
#     except Exception:
#         pass
#     html = response.text
#     # print(html)
#     soup= bs(html,'lxml')
#     motors= soup.find(class_='list-txt').find_all('a')
#     # print(motors)
#     motor_list= []
#     for motor in motors:
#         m= motor.get('href')
#         motor_list.append(m)

#     return motor_list
# url_list= get_url()
# print(url_list)

def motor_data(url):
    # for m_url in url:
    http= requests.get(url,headers=header)
    html= http.text
    soup= bs(html,'lxml')
    
    all= soup.find(class_="customtable j-model")
    print(all.text)

motor_data('http://www.jiche.com/Ducati/Monster696')