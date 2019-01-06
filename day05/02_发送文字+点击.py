from selenium import webdriver
import time 

# 先创建浏览器对象
driver = webdriver.Chrome()
# 打开百度
driver.get('http://www.baidu.com/')
# 找到搜索框,发送文字
key = input("请输入要搜索的内容:")
kw = driver.find_element_by_id('kw')
kw.send_keys(key)
# 找到 百度一下 按钮,点击一下
su = driver.find_element_by_id('su')
su.click()

time.sleep(1)
# 截图
driver.save_screenshot('美女.png')
# 关闭浏览器
driver.quit()










