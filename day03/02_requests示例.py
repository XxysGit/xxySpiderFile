import requests

url = "http://www.baidu.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50"}
# 发请求获取响应对象
res = requests.get(url,headers=headers)
# 获取响应的编码格式,百度默认ISO-8859-1
res.encoding = "utf-8"
print(res.encoding)
# 获取res的内容(字符串)
print(type(res.text))
# 获取res的内容(bytes)
print(type(res.content))
# 获取HTTP响应码 
print(res.status_code)
# 获取返回实际数据的URL地址
print(res.url)








