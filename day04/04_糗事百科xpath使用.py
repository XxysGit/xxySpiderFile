import requests
from lxml import etree
import pymongo

class QiushiSpider:
    def __init__(self):
        self.url = "https://www.qiushibaike.com/text/"
        self.headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"}
        # 连接对象
        self.conn = pymongo.MongoClient(
                      "192.168.56.129",
                      27017)
        # 库对象
        self.db = self.conn["Qiushidb"]
        # 集合对象
        self.myset = self.db["zhuanye"]
    
    # 获取页面
    def getPage(self):
        res = requests.get(self.url,
                    headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        self.parsePage(html)
    
    # 解析并写入数据库
    def parsePage(self,html):
        # 两步走
        parseHtml = etree.HTML(html)
        # 基准Xpath,每个段子对象
        # ['<element...>','<element...>','']
        baseList = parseHtml.xpath('//div[contains(@id,"qiushi_tag_")]')
        # for循环遍历每个段子对象,1个1个提取
        for base in baseList:
            # base : <element at ....>
            # 用户昵称
            username = base.xpath('./div/a/h2')
            if username:
                username = username[0].text.strip()
            else:
                username = "匿名用户"
            # 段子内容
            content = base.xpath('./a/div[@class="content"]/span/text()')
            content = "".join(content).strip()
            
            # 好笑数量
            laughNum = base.xpath('.//i[@class="number"]')[0].text        
            # 评论数量
            pingNum = base.xpath('.//i[@class="number"]')[1].text
        
            # 定义字典存mongo
            d = {
                "username":username,
                "content" :content.strip(),
                "laughNum":laughNum,
                "pingNum" :pingNum,
                }
            self.myset.insert_one(d)
        
    # 主函数
    def workOn(self):
        print("正在爬取中......")
        self.getPage()
        print("爬取结束,存入Qiushidb库")

if __name__ == "__main__":
    spider = QiushiSpider()
    spider.workOn()
    
    
    
    
    
    
    
    
    
    
    