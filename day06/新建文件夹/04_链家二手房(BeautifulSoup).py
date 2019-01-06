import requests
import pymongo
from bs4 import BeautifulSoup
import time 

class LianjiaSpider:
    def __init__(self):
        self.baseurl = 'https://bj.lianjia.com/ershoufang/pg'
        self.headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)"}
        # 连接对象
        self.conn = pymongo.MongoClient(
                              "192.168.56.129",
                              27017)
        # 库对象
        self.db = self.conn["Lianjia"]
        # 集合对象
        self.myset = self.db["houseInfo"]
        
    # 获取页面
    def getPage(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        self.parsePage(html)
    
    # 解析并保存页面
    def parsePage(self,html):
        # 创建解析对象
        soup = BeautifulSoup(html,'lxml')
        # 解析对象的find_all()方法获取每个房源信息
        rList = soup.find_all('li',attrs=\
            {"class":"clear LOGCLICKDATA"})
        for r in rList:
            #################################
            # houseInfo节点
            Info = r.find('div',attrs=\
                      {"class":"houseInfo"})\
                      .get_text().split('/')
            # Info:["月坛北街","2室1厅",....]
            # 小区名称
            name = Info[0]
            # 户型
            huxing = Info[1]
            # 面积
            area = Info[2]
            #################################
            positionInfo = r.find('div',attrs=\
                 {"class":"positionInfo"})\
                 .get_text().split('/')
            # 楼层
            louceng = positionInfo[0]
            # 年份
            year = positionInfo[1]
            # 地点
            address = positionInfo[2]
            ################################
            # 总价
            totalPrice = r.find('div',attrs=\
                     {"class":"totalPrice"})\
                     .get_text()
            # 单价
            unitPrice = r.find('div',attrs=\
                     {"class":"unitPrice"})\
                     .get_text()
            ################################
            d = {
                "名称" : name,
                "户型" : huxing,
                "面积" : area,
                "楼层" : louceng,
                "年份" : year,
                "地点" : address,
                "总价" : totalPrice,
                "单价" : unitPrice,
              }
            self.myset.insert_one(d)
            
    # 主函数
    def workOn(self):
        n = int(input("请输入页数:"))
        for pg in range(1,n+1):
            # 拼接url
            url = self.baseurl + str(pg) + '/'
            self.getPage(url)
            time.sleep(1)
            print("第%d页爬取成功" % pg)
    
if __name__ == "__main__":
    spider = LianjiaSpider()
    spider.workOn()











