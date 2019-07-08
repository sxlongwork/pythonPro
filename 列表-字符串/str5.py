# str 练习

name = "a!@#$2 D"
# print(name[:3])

# 求字符串长度
# print(len(name))

str1 = "ABCdefg"
print(str1)
print(len(str1))
print(str1.__len__())
print(str1.lower())
print(str1.upper())

name ="xiaoming"
print(name.center(13, "*"))
print(name.ljust(13, "*"))

print(name.startswith("xiao"))
print(name.endswith("ming"))

# help(str)

char = input("pls input a chracter:")
if char.isalpha():
    if char.islower():
        print("%s is a lower chracter." % char)
    elif char.isupper():
        print("%s is a upper chracter." % char)
    else:
        print("%s is lower and upper chracters.")
elif char.isdigit():
    print("%s is a digit." % char)
elif char.isalnum():
    print("%s ia digit and lower or upper chracters." % char)
else:
    print("%s is other chracters.")





