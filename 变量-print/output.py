# 输出

print()

print("="*20)
print('''
1-新用户注册
2-用户登录
3-忘记密码
4-退出
''')
print("="*20)
# select = input("pls select:")

# name = input("pls input your name:")
# age = input("pls input your age:")
#
# print(name, "is", age, "years old!", sep=" ")
# print("%s is %s years old!" % (name, age))
# print("{} is {} years old!".format(name, age))


number = 111222333444
print('number is %09d' % number)        # %06d 可以将数值补全为6位，不足6位的前面补0
number2 = 0.33
print('number2 is %.3f' % number2)        # %f默认是小数点后面有6位，%.3f表示小数点后3位

print('number is %.2f%%' % (number2*100))   # %%输出百分号%

