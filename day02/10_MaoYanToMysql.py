import urllib.request
import re
import pymysql
import warnings

class MaoyanSpider:
    def __init__(self):
        self.baseurl = "https://maoyan.com/board/4?offset="
        self.headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)"}
        self.offset = 0
        # 数据库连接对象
        self.db = pymysql.connect(
                    "192.168.56.129",
                    "lion",
                    "123456",
                    "spiderdb",
                    charset="utf8")
        # 游标对象
        self.cursor = self.db.cursor()
        
    
    # 获取页面
    def getPage(self,url):
        req = urllib.request.Request(url,
                    headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        self.parsePage(html)
    
    # 解析页面
    def parsePage(self,html):
        # 创建编译对象
        p = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>',re.S)
        rList = p.findall(html)
        # rList:[("霸王别姬","张国荣","1993"),()]
        self.writeToMysql(rList)
        
    # 保存数据
    def writeToMysql(self,rList):
        # 忽略下面语句的所有警告
        warnings.filterwarnings("ignore")

        ins = 'insert into film(\
          name,star,releasetime) \
          values(%s,%s,%s)'
        for r in rList:
            L = [r[0].strip(),
                 r[1].strip(),
                 r[2].strip()[5:15]
                ]
            # execute必须使用列表传参
            self.cursor.execute(ins,L)
            # 提交到数据库执行
            self.db.commit()
        
    # 主函数
    def workOn(self):
        while True:
            c = input("爬取按y,退出按q:")
            if c.strip().lower() == "y":           
                url = self.baseurl +\
                          str(self.offset)
                self.getPage(url)
                self.offset += 10
            else:
                print("爬取结束")
                # 必须等所有爬完之后再关闭
                self.cursor.close()
                self.db.close()
                break
        
                
        #for i in range(0,91,10):
        #    url = self.baseurl + str(i)
        #    self.getPage(url)
        #    time.sleep(0.1)
           
if __name__ == "__main__":
    spider = MaoyanSpider()
    spider.workOn()







