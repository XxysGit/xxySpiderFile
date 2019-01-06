# -*- coding: utf-8 -*-
import scrapy
from Daomu.items import DaomuItem

class DaomuSpider(scrapy.Spider):
    name = "daomu"
    allowed_domains = ["www.daomubiji.com"]
    start_urls = ['http://www.daomubiji.com/dao-mu-bi-ji-1']

    def parse(self, response):
        # 创建item对象
        item = DaomuItem()
        # 所有章节列表
        aList = response.xpath('//article/a/text()').extract()
        # aList : ["七星鲁王 第一章 血尸",""]
        i = 0
        for a in aList:
            info = a.split()
            # info : ["七星鲁王","第一章","血尸"]
            item["bookTitle"] = info[0]
            item["bookNum"] = info[1]
            item["bookName"] = info[2]
            item["bookLink"] = response.xpath(
                '//article/a/@href').extract()[i]
            i += 1
            yield item
