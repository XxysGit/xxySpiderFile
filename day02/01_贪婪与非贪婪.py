import re 

html = """
<div><p>苟利国家生死以</p></div>
<div><p>床前明月光</p></div>
"""
# 创建编译对象,贪婪匹配
p = re.compile('<div><p>.*</p></div>',re.S)
r = p.findall(html)
#print(r)

# 非贪婪匹配
p = re.compile('<div><p>.*?</p></div>',re.S)
r = p.findall(html)
print(r)















