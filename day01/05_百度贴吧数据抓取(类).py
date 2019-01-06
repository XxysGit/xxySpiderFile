import urllib.request
import urllib.parse

class BaiduSpider:
    def __init__(self):
        self.baseurl = "http://tieba.baidu.com/f?"
        self.headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)"}
    
    # 获取页面
    def getPage(self,url):
        req = urllib.request.Request\
                  (url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        return html
        
    # 解析页面
    def parsePage(self):
        pass
    
    # 保存数据
    def writePage(self,filename,html):
        with open(filename,"w",encoding="utf-8") as f:
            f.write(html)
    
    # 主函数
    def workOn(self):
        name = input("请输入贴吧名称:")
        begin = int(input("请输入起始页:"))
        end = int(input("请输入终止页:"))
        # 拼接贴吧主页URL地址
        kw = urllib.parse.urlencode({"kw":name})
        for page in range(begin,end+1):
            # 拼接第page页完整URL地址
            pn = (page - 1) * 50
            url = self.baseurl + kw + "&pn=" + str(pn)
            html = self.getPage(url)
            filename = "第" + str(page) + "页.html"
            self.writePage(filename,html)       
            print("第 %d 页爬取成功" % page)
    
if __name__ == "__main__":
    spider = BaiduSpider()
    spider.workOn()






    
    
    
    
    
    
    
    
    


