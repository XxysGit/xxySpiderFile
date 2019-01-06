import requests
import json
import pymysql

class DoubanSpider:
    def __init__(self):
        self.url = "https://movie.douban.com/j/chart/top_list?"
        self.headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"}
        self.db = pymysql.connect(
                         "192.168.56.129",
                         "lion",
                         "123456",
                         "spiderdb",
                         charset="utf8")
        self.cursor = self.db.cursor()
        
    # 获取页面
    def getPage(self,params):
        res = requests.get(self.url,
                    params=params,
                    headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        # html为[{1个电影信息},{},{}]
        self.parsePage(html)
    
    # 解析页面
    def parsePage(self,html):
        ins = 'insert into film \
                           values(%s,%s)'
        rList = json.loads(html)
        # [{},{},{}]
        for rDict in rList:
            name = rDict["title"]
            score = rDict["score"]
            
            L = [name.strip(),
                 float(score.strip())
                 ]
            self.cursor.execute(ins,L)
            self.db.commit()
    
    # 主函数
    def workOn(self):
        
        print("*************")
        print("|剧情|喜剧|动作|")
        print("*************")
        # 存放所有电影类型的列表
        kinds = ["剧情","喜剧","动作"]
        # 存放所有电影类型及type值的字典
        fDict = {"剧情":"11",
                 "喜剧":"3",
                 "动作":"24"
                }
        kind = input("请输入类型:")
        if kind in kinds:
            number = input("请输入数量:")
            params = {
                    "type":fDict[kind],
                    "interval_id":"100:90",
                    "action":"",	
                    "start":"0",
                    "limit":number
                }
            self.getPage(params)
        else:
            print("电影类型不存在")
               
if __name__ == "__main__":
    spider = DoubanSpider()
    spider.workOn()
    
    

    
    
    
    
    
    





