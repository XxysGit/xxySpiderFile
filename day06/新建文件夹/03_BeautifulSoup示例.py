from bs4 import BeautifulSoup

html = '''
<div class="test">雄霸</div>
<div class="test">聂风</div>
<div class="test2">
  <span>步惊云</span>
</div>
'''
# 创建解析对象
soup = BeautifulSoup(html,'lxml')
# 调用find_all()方法
rList = soup.find_all('div',{"class":"test2"})

for r in rList:
    # string属性只能获取当前节点内文本内容
    print(r.span.string)
    # get_text()能获取当前节点所有文本内容
    # 包括子节点的文本内容
    print(r.get_text())














