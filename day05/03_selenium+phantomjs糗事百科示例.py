from selenium import webdriver

# 创建浏览器对象
driver = webdriver.PhantomJS()
driver.get('https://www.qiushibaike.com/text/')
# 查找单个节点 
rOne = driver.find_element_by_class_name(
                                'content')
#print(rOne.text)
# 查找多个节点
rList = driver.find_elements_by_class_name(
                                'content')
for r in rList:
    print(r.text)
    print("*" * 40)









