import requests
from bs4 import BeautifulSoup
headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
#爬虫，爬取豆瓣书单
print('豆瓣书单:')
res = requests.get('https://book.douban.com/top250',headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
items = soup.select('div.pl2 a')
for i in items:
    name = i['title']
    link = i['href']
    print(name,link)

#爬虫，爬取豆瓣推荐电影
print('豆瓣推荐电影:')
res = requests.get('https://movie.douban.com/top250',headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
items = soup.select('div.hd a')
for i in items:
    link = i['href']
    name = i.find('span').text
    print(name,link)
