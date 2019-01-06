import urllib.request
import urllib.parse
import json

# 接收用户输入
key = input("请输入要翻译的内容:")
# 把Form Data定义成1个大字典
data = {
        "i":key,
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":"15458120942800",
        "sign":"108feafc7c01c7461a41034463a8df9b",
        "ts":"1545812094280",
        "bv":"363eb5a1de8cfbadd0cd78bd6bd43bee",
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTIME",
        "typoResult":"false"
    }
# 把data转为bytes数据类型
data = urllib.parse.urlencode(data).encode("utf-8")
# 发请求,获响应,获取内容
# 此处的URL地址为F12抓到的POST的地址,去掉translate_o中的 "_o"
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers = {"User-Agent":"Mozilla/5.0"}
req = urllib.request.Request\
            (url,data=data,headers=headers)
res = urllib.request.urlopen(req)
html = res.read().decode("utf-8")

# 把json格式的字符串转为python中字典
rDict = json.loads(html)
result = rDict["translateResult"][0][0]["tgt"]
print(result)


#{'type': 'EN2ZH_CN', 
# 'errorCode': 0, 
# 'elapsedTime': 1, 
# 'translateResult': 
#     [[{'src': 'tiger', 'tgt': '老虎'}]]}










