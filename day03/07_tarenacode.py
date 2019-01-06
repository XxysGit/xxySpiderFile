import requests
import pymysql
import re 
import warnings

class NoteSpider:
    def __init__(self):
        self.url = "http://code.tarena.com.cn/"
        self.headers = {"User-Agent":"Mozilla/5.0"}
        # Web客户端验证参数(元组)
        self.auth = ("tarenacode","code_2013")
        # 库对象
        self.db = pymysql.connect("192.168.56.129",
                            "lion",
                            "123456",
                            "spiderdb",
                            charset="utf8")
        # 游标对象
        self.cursor = self.db.cursor()
        
    # 获取并解析页面
    def getPrasePage(self):
        res = requests.get(self.url,
                    auth=self.auth,
                    headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        # 正则编译对象
        p = re.compile('<a href="(.*?)/.*?</a>',re.S)
        rList = p.findall(html)
        print(rList)
        self.writePage(rList)
        
    # 保存数据
    def writePage(self,rList):
        ctab = 'create table if not exists \
                tarenaNote(name varchar(30))'
        ins = 'insert into tarenaNote \
               values(%s)'
        # 忽略下面语句警告
        warnings.filterwarnings("ignore")
        self.cursor.execute(ctab)
        for r in rList:
            if r != "..":
                self.cursor.execute(ins,[r])
                # 千万别忘了提交
                self.db.commit()
        # 关闭
        self.cursor.close()
        self.db.close()
                
if __name__ == "__main__":
    spider = NoteSpider()
    spider.getPrasePage()
    print("成功")














