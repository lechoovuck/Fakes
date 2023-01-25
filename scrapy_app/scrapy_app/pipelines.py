from itemadapter import ItemAdapter
from crawler.models import ScrapyItem
import json

class ScrapyAppPipeline(object):
    def __init__(self, unique_id,start_url, *args, **kwargs):
        self.start_url = start_url
        self.unique_id = unique_id
        self.items = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            unique_id=crawler.settings.get('unique_id'),
            start_url=crawler.settings.get('start_url'),
        )

    def close_spider(self, spider):
        item = ScrapyItem()
        item.start_url = self.start_url
        item.unique_id = self.unique_id
        item.data = json.dumps(self.items)
        item.save()

    def process_item(self, item, spider):
        self.items.append(item['url'])
        return item