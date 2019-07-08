# - 题目描述:
# 输入两个字符串，从第一字符串中删除第二个字符串中所有的字符。
# 例如，输入”They are students.”和”aeiou”，则删除之后的第一个字符串变成”Thy r stdnts.”
#
# - 输入描述:
# 每个测试输入包含2个字符串
#
# - 输出描述:
# 输出删除后的字符串


str1 = input("pls input first string:")
str2 = input("pls input second string:")

list1 = list(str1)
set1 = set(str2)
i = 0
while i < len(list1):
    for j in set1:
        if list1[i] == j:
            list1.pop(i)
            i -= 1
            break
    i += 1
# print(str[list1])
str3 = ""
for m in list1:
    str3 += m
print(str3)
