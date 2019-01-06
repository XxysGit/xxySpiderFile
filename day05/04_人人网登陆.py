from selenium import webdriver
import time 

# 如何设置chrome为无界面浏览器
opt = webdriver.ChromeOptions()
opt.set_headless()
opt.add_argument('windows-size=1920x3000')


# 创建浏览器对象
driver = webdriver.Chrome(options=opt)
# 发请求,获响应
driver.get('https://www.douban.com/')
# 窗口最大化
driver.maximize_window()
# 用户名,发送
uname = driver.find_element_by_name(
                         'form_email')
uname.send_keys('309435365@qq.com')
# 密码,发送
pwd = driver.find_element_by_name(
                         'form_password')
pwd.send_keys('zhanshen001')
# 验证码,屏幕截图,从终端输入验证码,发送
driver.save_screenshot('yzm.png')
yzm = input("请输入验证码:")
driver.find_element_by_id('captcha_image')\
                   .send_keys(yzm)
print(111)
# 登陆按钮点击
driver.find_element_by_class_name('bn-submit').click()
print(222)
# 屏幕截图
time.sleep(2)
driver.save_screenshot('成功.png')
# 关闭浏览器

driver.quit()





#用户名  ：email
#密码    ：password
#验证码  ：icode
#登陆(id)：login   


