import requests

url = "http://tieba.baidu.com/p/5962974313"
headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"}

res = requests.get(url,headers=headers)
res.encoding = "utf-8"
html = res.text

with open("视频.html","w",encoding="utf-8") as f:
    f.write(html)
