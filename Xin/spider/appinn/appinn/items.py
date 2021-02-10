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
