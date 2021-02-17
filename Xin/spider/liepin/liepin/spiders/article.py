import scrapy


class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['https://www.liepin.com']
    start_urls = ['http://https://www.liepin.com/']

    def parse(self, response):
        pass
