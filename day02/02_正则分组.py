import re 

s = "A B C D"
p1 = re.compile('\w+\s+\w+')
print(p1.findall(s))

# 第1步 : 匹配整体正则['A B', 'C D']
# 第2步 : 匹配分组内容['A','C']
p2 = re.compile('(\w+)\s+\w+')
print(p2.findall(s))
# 第1步 : 匹配整体正则['A B']
# 第2步 : [('A','B')]
p3 = re.compile('(\w+)\s+(\w+)')
print(p3.findall(s))












