import requests
from multiprocessing import Queue
from threading import Thread
from lxml import etree
import time 

class XiaomiSpider:
    def __init__(self):
        self.baseurl = 'http://app.mi.com/category/12#page='
        self.mainurl = 'http://app.mi.com'
        self.headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)"}
        # URL队列
        self.urlQueue = Queue()
        # 解析队列
        self.parseQueue = Queue()
    
    # URL入队列
    def getUrl(self):
        for page in range(20):
            url = self.baseurl + str(page)
            # 把拼接的url放到url队列中
            self.urlQueue.put(url)

    # 采集线程函数,get出URL发请求,把html给解析队列
    def getHtml(self):
        while True:
            # 先判断队列是否为空
            if not self.urlQueue.empty():
                url = self.urlQueue.get()
                # 三步走
                res = requests.get(url,headers=self.headers)
                res.encoding = "utf-8"
                html = res.text
                # 把html放到解析队列
                self.parseQueue.put(html)
            else:
                break
            
    # 解析线程函数,get出html源码,提取并处理数据
    def getData(self):
        while True:
            try:
                # block为True表示阻塞,超过0.5秒钟没有get到数据,则抛出超时异常
                html = self.parseQueue.get(block=True,timeout=0.5)
                # 创建解析对象,调用xpath
                parseHtml = etree.HTML(html)
                # [li1对象,li2对象]
                baseList = parseHtml.\
                           xpath('//ul[@id="all-applist"]//li')
                for base in baseList:
                    # 应用名称
                    name = base.xpath('./h5/a/text()')[0]
                    # 应用链接
                    link = self.mainurl +\
                           base.xpath('./h5/a/@href')[0]
                    d = {
                         "分类":"学习教育",
                         "名称":name,
                         "链接":link,
                      }
                    with open("XM.json","a",
                              encoding="utf-8") as f:
                        f.write(str(d)+'\n')    
            except:
                break
    # 主函数
    def workOn(self):
        # url先入队列
        self.getUrl()
        # 存放所有采集线程对象和解析线程对象列表
        tList = []

        # 统一创建线程,采集和解析一起干活
        for i in range(5):
            t1 = Thread(target=self.getHtml)
            t2 = Thread(target=self.getData)
            tList.append(t1)
            tList.append(t2)
            t1.start()
            t2.start()
            
        # 统一回收采集线程和解析线程
        for i in tList:
            i.join()
            
        
if __name__ == "__main__":
    start = time.time()
    spider = XiaomiSpider()
    spider.workOn()
    end = time.time()
    print("执行时间:%.2f" % (end - start))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    






