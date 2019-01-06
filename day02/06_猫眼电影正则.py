import urllib.request
import re
import csv

class MaoyanSpider:
    def __init__(self):
        self.baseurl = "https://maoyan.com/board/4?offset="
        self.headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)"}
        self.offset = 0
    
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
        self.writeToCSV(rList)
        
    # 保存数据
    def writeToCSV(self,rList):
        for r in rList:
            #r = list(r)
            r = [r[0].strip(),r[1].strip(),r[2].strip()]
            with open("猫眼.csv","a",
                      newline="",
                      encoding="gb18030") as f:
                # 创建写入对象
                writer = csv.writer(f)
                # 调用writerow()方法
                writer.writerow(r)
                
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
                break
                
        #for i in range(0,91,10):
        #    url = self.baseurl + str(i)
        #    self.getPage(url)
        #    time.sleep(0.1)
           
if __name__ == "__main__":
    spider = MaoyanSpider()
    spider.workOn()







