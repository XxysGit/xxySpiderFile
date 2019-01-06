import requests
from multiprocessing import Queue
from threading import Thread
import time
import urllib.parse
import json

class XiaomiSpider:
    def __init__(self):
        self.baseurl = 'http://app.mi.com/categotyAllListApi?'
        self.mainurl = 'http://app.mi.com/details?id='
        self.headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)"}
        # URL队列
        self.urlQueue = Queue()
        # 解析队列
        self.parseQueue = Queue()
    
    # URL入队列
    def getUrl(self):
        for page in range(2):
            params = { 'page':str(page),
                       'categoryId':'2',
                       'pageSize':'30',
                    }
            params = urllib.parse.urlencode(params)
            # params : 'page=0&categoryId=2&pageSize=30'
            url = self.baseurl + params
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
            if not self.parseQueue.empty():
                # html为json格式的字符串
                html = self.parseQueue.get()
                # hList : [{应用1信息},{应用2信息},{}]
                hList = json.loads(html)['data']
                for h in hList:
                    # 应用名称
                    name = h['displayName']
                    # 应用链接
                    link = self.mainurl + h['packageName']
                    d = {
                         "名称":name,
                         "链接":link,
                      }
                    with open("XM.json","a",
                              encoding="utf-8") as f:
                        f.write(str(d)+'\n')    
            else:
                break
    # 主函数
    def workOn(self):
        # url先入队列
        self.getUrl()
        # 存放所有采集线程对象列表
        t1List = []
        # 存放所有解析线程对象列表
        t2List = []
        # 采集线程
        for i in range(10):
            t = Thread(target=self.getHtml)
            t1List.append(t)
            t.start()
        # 统一回收采集线程
        for i in t1List:
            i.join()
        # 解析线程
        for i in range(10):
            t = Thread(target=self.getData)
            t2List.append(t)
            t.start()
        # 统一回收解析线程
        for i in t2List:
            i.join()
        
if __name__ == "__main__":
    start = time.time()
    spider = XiaomiSpider()
    spider.workOn()
    end = time.time()
    print("执行时间:%.2f" % (end - start))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    






