# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫名
    name = "baidu"
    # 允许要爬取的域
    allowed_domains = ["www.baidu.com"]
    # 起始URL地址
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        with open("Baidu.html","w",encoding="utf-8") as f:
            f.write(response.text)








