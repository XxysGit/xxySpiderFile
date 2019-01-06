import urllib.request

# 创建请求对象(Request())
url = "http://www.baidu.com/"
headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)"}
req = urllib.request.Request(url,headers=headers)

# 获取响应对象(urlopen())
res = urllib.request.urlopen(req)

# 获取内容(read().decode("utf-8"))
html = res.read().decode("utf-8")

# 获取HTTP响应码
print(res.getcode())
# 获取实际数据URL
print(res.geturl())












