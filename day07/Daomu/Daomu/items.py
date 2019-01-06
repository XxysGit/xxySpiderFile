# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomuItem(scrapy.Item):
    # define the fields for your item here like:
    # 标题
    bookTitle = scrapy.Field()
    # 章节数量
    bookNum = scrapy.Field()
    # 章节名称
    bookName = scrapy.Field()
    # 章节链接
    bookLink = scrapy.Field()
