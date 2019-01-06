import requests

baseurl = "http://www.baidu.com/s?"
headers = {"User-Agent":"Mozilla/5.0"}

# 终端输入
key = input("搜索内容:")
pn = input("输入页数:")
pn = (int(pn) - 1) * 10
# 把所有查询参数定义为字典
params = {
        "wd" : key,
        "pn" : pn,
    }
# 无需拼接URL,也不用URL编码
# 自动URL编码,自动拼接URL地址
res = requests.get(baseurl,
                   params=params,
                   headers=headers)
res.encoding = "utf-8"
html = res.text
print(html)















