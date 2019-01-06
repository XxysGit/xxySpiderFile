# 导入selenium中的webdriver
from selenium import webdriver
import time 

# 创建phantomjs浏览器对象
driver = webdriver.PhantomJS()
# 发请求
driver.get('http://www.baidu.com/')
# 获取html源码
n = driver.page_source.find('kw')
print(n)

# 获取网页截屏
driver.save_screenshot('百度.png')

time.sleep(10)
# 关闭浏览器
driver.quit()


















