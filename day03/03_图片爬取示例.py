import requests

url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1545973683621&di=2bf6d1391d99ad76870d8e871afd7a9f&imgtype=0&src=http%3A%2F%2Fpic4.iqiyipic.com%2Fimage%2F20181016%2F23%2F03%2Fv_119993043_m_601_720_405.jpg"
headers = {"User-Agent":"Mozilla/5.0"}
# 三步走,发请求,指编码,获内容
res = requests.get(url,headers=headers)
res.encoding = "utf-8"
html = res.content
# 以 wb 的方式写入本地文件
with open("颖宝.jpg","wb") as f:
    f.write(html)

print("颖宝到本地")








