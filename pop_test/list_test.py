import requests as rq
from bs4 import BeautifulSoup as bs
url= 'https://blog.xbookcn.net/2017/10/blog-post_89.html'
heade= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}
response= rq.get(url,headers=heade)
soup= bs(response.text,'html.parser')
# print(soup)
all_links= soup.find_all('p')
for link in all_links:
    print(link.text)