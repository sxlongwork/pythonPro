'''
datatime比time高级，可以理解为是基于time进行了封装
提供了更为实用的函数，datetime模块的接口更直观，容易调用

模块中有几个类：
datetime(常用)  同时有时间和日期
timedelta  主要用于计算时间的跨度
tzinfo  时区相关
time  时间
date  日期

'''
import datetime

# 获取当前时间
d1 = datetime.datetime.now()
print(d1)
print(type(d1))

# 获取指定时间
d2 = datetime.datetime(2019,5,1,10,30,20,123456)
print(d2)

# 将datetime类型时间转为字符串
d3 = d1.strftime("%Y-%m-%d %X")
print(d3)

# 将格式化字符串转为datetime类型
# 注意：转换的格式要与字符串一致
d4 = datetime.datetime.strptime(d3,"%Y-%m-%d %X")
print(d4)

d5 = datetime.datetime(2019,5,1,10,30,20,123456)
d6 = datetime.datetime.now()
d7 = d6 - d5
print(d7)
print(type(d7))
# 间隔天数
print(d7.days)
# 天数除外的秒数
print(d7.seconds)






