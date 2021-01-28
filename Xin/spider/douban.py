import requests
import time
from bs4 import BeautifulSoup

#爬取豆瓣top250书单
print('豆瓣书单:')
def get_douban_books(url):
    headers = {
     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    items = soup.select('div.pl2 a')
    for i in items:
        name = i['title']
        link = i['href']
        print(name,link)

url = 'https://book.douban.com/top250?start={}'
urls = [url.format(num*25) for num in range(10)]
for items in urls:
    get_douban_books(items)
    time.sleep(1)
#爬取豆瓣top250电影
print('豆瓣推荐电影:')
def get_douban_movies(url):
    headers = {
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    items = soup.select('div.hd a')
    for i in items:
        link = i['href']
        name = i.find('span').text
        print(name,link)
url = 'https://movie.douban.com/top250?start={}'
urls = [url.format(num*25) for num in range(10)]
for items in urls:
    get_douban_movies(items)
    time.sleep(1)
