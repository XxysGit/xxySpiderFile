import urllib.request

url = "http://www.renren.com/969255813/profile"
headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        #Accept-Encoding: gzip, deflate
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Connection":"keep-alive",
        "Cookie":"anonymid=jq7d42gh-gr2bw; depovince=BJ; _r01_=1; JSESSIONID=abcReukbdFRnJc41oCYFw; ick_login=2a4b43b1-f36e-4bc4-983b-d7f6b80bc3b7; first_login_flag=1; ln_uact=18633615542; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; loginfrom=syshome; ch_id=10016; jebe_key=f448d565-0c8d-4f43-b79c-002d5e47bae0%7C2e9beece3ead42fe6a26739d515f14df%7C1545960795286%7C1%7C1545960795988; wp_fold=0; jebecookies=fbce59e9-2a4b-42a2-9e63-5b0f10d2fc7b|||||; _de=2229A2704041535FC5E7FC3B0F076082; p=96d21992fd673d6af178f0583cf315e43; t=89f2de512578d793ac1593f83fa3dad83; societyguester=89f2de512578d793ac1593f83fa3dad83; id=969255813; xnsid=d88ce62",
        "Host":"www.renren.com",
        "Referer":"http://www.renren.com/SysHome.do",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    }

req = urllib.request.Request(url,headers=headers)
res = urllib.request.urlopen(req)
html = res.read().decode("utf-8")
print(html)







