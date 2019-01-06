import urllib.request

# 直接发请求,并得到响应对象
url = "http://www.baidu.com/"
respone = urllib.request.urlopen(url)
print(respone.read().decode("utf-8"))

# decode() : bytes -> string
# encode() : string -> bytes






