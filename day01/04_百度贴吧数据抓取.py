import urllib.request
import urllib.parse
import random
import time 

hList = [
         {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)"},
         {"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)"}
    ]
headers = random.choice(hList)
baseurl = "http://tieba.baidu.com/f?"
# 接收用户输入
name = input("请输入贴吧名称:")
begin = int(input("请输入起始页:"))
end = int(input("请输入终止页:"))
# 拼接贴吧主页URL地址
kw = urllib.parse.urlencode({"kw":name})
for page in range(begin,end+1):
    # 拼接第page页完整URL地址
    pn = (page - 1) * 50
    url = baseurl + kw + "&pn=" + str(pn)
    # 发请求,获取响应内容
    req = urllib.request.Request(url,headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read().decode("utf-8")
    # 保存到本地:第1页.html 第2页.html
    filename = "第" + str(page) + "页.html"
    with open(filename,"w",encoding="utf-8") as f:
        f.write(html)
    
    print("第 %d 页爬取成功" % page)
    time.sleep(0.5)
















