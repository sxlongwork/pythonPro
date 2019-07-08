# str 定义

# 凡是引号括起来的都是字符串，还有input输入的，str()函数转换的

# help(str)

str1 = 'abc'
str2 = "abc"
str3 = '''abc'''
str4 = """abc"""
str5 = str(123)
str6 = input("pls input a number:")
print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))
print(type(str5))
print(type(str6))
print("-"*30)
print(isinstance(str1, str))
print(isinstance(str2, int))
print(isinstance(str3, float))
print(isinstance(str4, bool))
print(isinstance(str5, list))
print(isinstance(str6, tuple))
print(isinstance(str6, (int, float, dict)))

# help(isinstance)

# age = 12.8
# print(isinstance(age, (int, float)))  # 可以判断age是否属于int或float类型

