import requests

url = "http://httpbin.org/get"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50"}
proxies = {"http":"http://37.192.32.213:36344"}

res = requests.get(url,
                   proxies=proxies,
                   headers=headers,
                   timeout=5)
res.encoding = "utf-8"
html = res.text
print(html)






