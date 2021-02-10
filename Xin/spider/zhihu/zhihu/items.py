# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Question(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    question_id = scrapy.Field()

class Answer(scrapy.Item):
    author = scrapy.Field()
    vote_count = scrapy.Field()
    content = scrapy.Field()
    question_id = scrapy.Field()
