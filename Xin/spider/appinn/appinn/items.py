'''
Author: your name
Date: 2021-02-09 19:49:36
LastEditTime: 2021-02-09 20:02:35
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \undefinedc:\mywork\Python_test\Xin\spider\appinn\appinn\items.py
'''
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AppinnItem(scrapy.Item):
    title = scrapy.Field()  # 标题
    time = scrapy.Field()  # 时间
    author = scrapy.Field()  #作者
    score = scrapy.Field()  #分数
    content = scrapy.Field()  #内容
