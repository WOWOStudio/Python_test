# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class AppinnPipeline:
    def process_item(self, item, spider):
        if item.get('score'):
            item['score'] = int(item['score'])
            if item['score'] < 3:
                raise DropItem('去掉3分一下的文章')
            return item
