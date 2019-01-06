# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CsdnPipeline(object):
    def process_item(self, item, spider):
        print("================")
        print(item['title'])
        print(item['time'])
        print(item['number'])
        print("================")
        # 必须保留
        return item
