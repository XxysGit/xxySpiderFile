import re

html = '''
<div class="animal">
  <p class="name">
    <a title="Tiger"></a>
  <p>

  <p class="content">
    Two tigers two tigers run fast
  </p>
</div>

<div class="animal">
  <p class="name">
    <a title="Rabbit"></a>
  <p>
  
  <p class="content">
    Small white rabbit white and white
  </p>
</div>'''
p = re.compile('<div class="animal">.*?title="(.*?)".*?class="content">(.*?)</p>',re.S)
rList = p.findall(html)
#print(rList)
# [("Tiger"," Two ..."),()]
# ('Tiger', '\n    Two tigers two tigers run fast\n  ')
for r in rList:
    print("动物名称:%s" % r[0].strip())
    print("动物描述:%s" % r[1].strip())
    print("*" * 30)
















