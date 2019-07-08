'''
日历模块

'''
import calendar

# 返回指定某年某月的日历
print(calendar.month(2019,5))

# 返回指定年份的日历
# print(calendar.calendar(2018))

# 判断是否是闰年，是返回True;否则返回False
print(calendar.isleap(2008))

# 返回某个月的第一天的weekday(0~6)和当月天数
print(calendar.monthrange(2019,5))

# 返回每个月以每周为元素的列表
print(calendar.monthcalendar(2019,5))
