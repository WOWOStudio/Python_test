import requests
import time
from bs4 import BeautifulSoup
from openpyxl import Workbook

headers = {
     'user-agent': ''
}

#爬豆瓣top250书单和top250电影，并存入excel中
class set_excel:
    def __init__(self,the_title,the_type,url):
        urls = [url.format(num*25) for num in range(10)]
        wb = Workbook()
        self.sheet = wb.active
        self.sheet.title = the_title
        for items in urls:
            self.get_soup(items)
            if the_type == 'book':
                self.get_book()
            else:
                self.get_movie()
            time.sleep(1)
        if the_type == 'book':
            wb.save('{}.xlsx'.format(the_title))
        else:
            wb.save('{}.xlsx'.format(the_title))

    def get_soup(self,url):
        res = requests.get(url,headers=headers)
        self.soup = BeautifulSoup(res.text,'html.parser')

    def get_book(self):
        items = self.soup.find_all(class_='item')
        for item in items:
            tag = item.find(class_='pl2').find('a')
            link = tag['href']
            name = tag['title']
            rating = item.find(class_='rating_nums').text
            row = [name,rating,link]
            self.sheet.append(row)
            print(name,rating,link)

    def get_movie(self):
        items = self.soup.select('div.item')
        for item in items:
            tag = item.find(class_='hd').find('a')
            link = tag['href']
            name = tag.find('span').text
            rating = item.find(class_='rating_num').text
            row = [name,rating,link]
            self.sheet.append(row)
            print(name,rating,link)

set_excel('豆瓣Top250图书','book','https://book.douban.com/top250?start={}')
set_excel('豆瓣Top250电影','movie','https://movie.douban.com/top250?start={}')
