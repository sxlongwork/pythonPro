'''
UTC(世界标准时间)，中国时间是UTC+8
DST(夏令时)：是一种节约能源而人为规定的时间制度，在夏季调快一个小时
'''

'''
时间表示
1.时间戳
单位为秒，从1970.1.1 00:00:00开始算起
2.元组
用元组的9个整数内容元素表示
year,month,day,hours,minutes,seconds,weekday,Julia day,DST(1或-1，0)
DST:0表示正常时间
1表示夏令时
-1表示根据时间自行判断
3.格式化字符串

'''
import time

# 返回当前时间的时间戳，浮点数形式，不需要参数
c = time.time()
print(c)

# 将时间戳转为UTC时间元组
t = time.gmtime(c)
print(t)

# 将时间戳转为本地时间元组
b = time.localtime(c)
print(b)

# 将本地时间元组转为时间戳
m = time.mktime(b)
print(m)

# 将时间元组转为字符串
s = time.asctime(b)
print(s)

# 将时间戳转为字符串,
p = time.ctime(c)
print(p)

# 将时间元组转为指定格式的字符串，时间元组可以不写，不写则默认转当前时间
q = time.strftime("%Y-%m-%d %H:%M:%S",b)
print(q)

# 将时间字符串转为时间元组
w = time.strptime(q,"%Y-%m-%d %X")
print(w)

# 延迟一个时间，整形或浮点型
time.sleep(2)

# 返回当前程序的CPU时间
# Unix始终返回全部的运行时间
# windows从第二次开始，都是以第一个调用此函数的开始时间戳作为基数
cpu1 = time.clock()
print(cpu1)
time.sleep(2)
cpu2 = time.clock()
print(cpu2)


