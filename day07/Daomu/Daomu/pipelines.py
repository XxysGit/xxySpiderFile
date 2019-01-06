# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from Daomu.settings import *
import pymongo
import pymysql

class DaomuPipeline(object):
    def process_item(self, item, spider):
        return item

class MongoPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            host = MONGODB_HOST,
            port = MONGODB_PORT
           )
        self.db = self.conn[MONGODB_DB]
        self.myset = self.db[MONGODB_SET]

    def process_item(self,item,spider):
        # 把item转为字典格式
        d = dict(item)
        self.myset.insert_one(d)
        return item

class MysqlPipeline(object):
    def __init__(self):
        pass

    def process_item(self,item,spider):
        return item

    # 关闭
    def close_spider(self,spider):
        pass








