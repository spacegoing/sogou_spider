# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class SogouSpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWriterPipeline(object):
    cached_dict = {}
    count = 0

    def close_spider(self, spider):
        with open('stock_links_%d.json' % self.count, 'w') as f:
            json.dump(self.cached_dict, f)

    def process_item(self, item, spider):
        first_stock = item['combo'][0]
        second_stock = item['combo'][1]

        if first_stock in self.cached_dict:
            if second_stock not in self.cached_dict[first_stock]:
                self.cached_dict[first_stock][second_stock] = {}
        else:
            self.cached_dict[first_stock] = {}
            self.cached_dict[first_stock][second_stock] = {}

        self.cached_dict[first_stock][second_stock][item['type']] = item['resnum']
        self.count += 1

        spider.logger.info('%d: "%s"+AND+"%s"+AND+"%s"' % (self.count, first_stock, second_stock, item['type']))

        return item
