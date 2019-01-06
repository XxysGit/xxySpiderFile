import urllib.request
import re

class NeihanSpider:
    def __init__(self):
        self.baseurl = "https://www.neihan8.com/njjzw/"
        self.headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)"}
        self.page = 2
    
    # 获取页面
    def getPage(self,url):
        req = urllib.request.Request(url,
                  headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8") 
        self.parsePage(html)
    
    # 解析页面
    def parsePage(self,html):
        p = re.compile('<div class="text-.*?title="(.*?)">.*?class="desc">(.*?)</div>',re.S)
        rList = p.findall(html)
#        print(rList)
        # [("动物贴墙","海豹"),(),(),()]
        self.writePage(rList)
    
    # 保存数据
    def writePage(self,rList):
        for rTuple in rList:
            with open("内涵.txt","a") as f:
                f.write(rTuple[0].strip()+"\n")
                f.write(rTuple[1].strip()+"\n\n") 
    # 主函数
    def workOn(self):
        self.getPage(self.baseurl)
        while True:
            c = input("成功,是否继续(y/n):")
            if c.strip().lower() == "y":
                url = self.baseurl + \
                   "index_" + str(self.page) + \
                   ".html"
                self.getPage(url)
                self.page += 1
            else:
                print("爬取结束")
                break
            
if __name__ == "__main__":
    spider = NeihanSpider()
    spider.workOn()












