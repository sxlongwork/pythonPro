# if practice
# input输入一个年份,判断是否为闰年(能被4整除但不能被100整除的是闰年，或者能被400整除的也是闰年)

num = int(input("pls input a year(xxxx):"))

if num % 4 == 0 and num % 100 != 0 or num % 400 ==0:
    print("%d is leap year." % num)
else:
    print("{} is not leap year.".format(num))
