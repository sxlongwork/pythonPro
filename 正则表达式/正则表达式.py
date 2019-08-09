"""
python中正则表达式的使用
"""

import re

# match方法,  从字符串的头部开始匹配，不匹配结尾，group()方法会返回匹配的内容

# 基本正则匹配
data1 = re.match(r'\d+', '2019年')
data2 = re.match(r'\d+', '今年是2019年')  # data = None

data3 = re.match(r'[a-zA-Z0-9_]{4,20}@(163|126)\.com$', '0a12@126.com')
print(data3.group())  # 0a12@126.com

print(data1.group())  # 2019

# 分组操作
data4 = re.match(r'([a-zA-Z_])([a-zA-Z0-9_]*)', 'a_123b')
print(data4.group(1), data4.group(2))  # a _123b

# search()方法，匹配字符串中是否包含某个字符串
data5 = re.search(r'\d+', 'python=2019, java=2018')
print(data5.group())  # 2019, 只匹配一次，匹配到了后就反hi，后面的就不再匹配

# findall()方法， 匹配所有出现的字符串
data6 = re.findall(r'\d+', 'python=2019, java=2018')
print(data6)  # ['2019', '2018'], 返回一个匹配到的字符串列表，

# sub()方法，用一个值替换所有匹配到的字符串
data7 = re.sub(r'\d+', '0000', 'python=2019, java=2018')
print(data7)  # python=0000, java=0000,

# split() ,使用正则表达式分割字符串，
data8 = re.split(r":| ", "root:123 admin boot")
print(data8)  # ['root', '123', 'admin', 'boot']
