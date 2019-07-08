# 字符串的常见操作

str1 = "abcdefg"
# 字符串的长度
str1.__len__()
len(str1)

# 固定10个字符，不够的补*
str1.center(10, '*')    # 一共10个字符，str1居中，不够位补"*"
str1.ljust(10, '*')     # 一共10个字符，str1居左，不够位补"*"
str1.rjust(10, '*')     # 一共10个字符，str1居右，不够位补"*"

# 判断字符串是否以"xxx"结尾或开头，"xxx"表示任务字符串
str1.startswith("abc")
str1.endswith("bbc")

# 判断字符'a'在字符串里共出现了多少次
str1.count('a')



