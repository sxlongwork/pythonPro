'''
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e:
    语句2
...
else:
    语句e

注意：else语句可以没有

作用：用来检测try语句块中的错误，except获取到错误信息并处理

执行逻辑：
1.try语句块出现了错误，且except匹配到，则执行相应的处理代码
2.try语句块出现了错误，且except没有匹配到，则抛给上一层的try
3.没有错误，执行else
'''

# try语句块常见的三种形式
# 所有可能出现的具体错误都用except接收
try:
    # print(int("aaa"))
    print(3/0)
except ValueError as e:
    print("int 无法将非数字字符串转换为整数")
except ZeroDivisionError as e:
    print("0 不能作为除数")
else:
    print("everything is ok!")
print("-----------------------------")

# 使用一个except接收可能出现的错误
try:
    # print(int("aaa"))
    print(3/0)
except:     # 匹配所有的错误，但是无法确定是哪一种
    print("代码有错误")
print("------------------------------")

# 将可能出现的错误都列出来放到except后面的括号里
try:
    print(int("aaa"))
except (NameError, ValueError, ZeroDivisionError):      # 将多种错误放到一个except中匹配
    print("代码有debug")
print("=======")


# 函数嵌套多次调用，在最外层的代码加上try，可以捉到到内部函数出现的错误
