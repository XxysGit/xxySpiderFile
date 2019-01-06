from selenium import webdriver
import time 

# 创建浏览器对象
driver = webdriver.Chrome()
# 访问京东首页
driver.get('https://www.jd.com/')
# 找到搜索框按钮,接收终端输入,发送到搜索框
text = driver.find_element_by_class_name(
                                  'text')
key = input("请输入要搜索的内容:")
text.send_keys(key)
# 点击 搜索按钮
button = driver.find_element_by_class_name(
                                'button')
button.click()
time.sleep(2)

while True:
    # 执行脚本,进度条拉到最底部
    driver.execute_script(
     'window.scrollTo(0,document.body.\
    scrollHeight)')
    time.sleep(3)
    # 提取数据,分析数据
    rList = driver.find_elements_by_xpath(
               '//div[@id="J_goodsList"]//li')
    # rList : ['商品1节点对象','商品2节点对象']
    for r in rList:
        contentList = r.text.split('\n')
        price = contentList[0]
        name = contentList[1]
        commit = contentList[2]
        market = contentList[3]
        
        d = {
                "价格":price,
                "名称":name,
                "评论":commit,
                "商家":market,
                }
        with open("jd.json","a",encoding="utf-8") as f:
            f.write(str(d) + '\n')
        
    # 点击下一页,-1表示没找到
    if driver.page_source.find(
            'pn-next disabled') == -1:
        driver.find_element_by_class_name\
                   ('pn-next').click()
        time.sleep(3)
    else:
        print("爬取结束")
        break
          
#下一页能点 ：  pn-next
#下一页不能点： pn-next disabled

















