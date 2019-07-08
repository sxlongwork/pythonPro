# str

name = "xiaoming"

print(name.upper().isupper())
print(name.__len__())
print(name.replace("i", "I", 1))
# print(name.split("i"))

# 常量池：-5~256
age = 12345
print(id(age))
age = 2
bb = 12345
print(id(age))
print(id(bb))


