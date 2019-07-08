# variables 变量定义，不用加上变量的类型，变量第一次定义时确定它的类型

help(id)
a = 1
print(id(a))
a = 3
print(id(a))
c = 1
print(id(c,))
d = 3
print(id(d))

print("==========================")
name1 = "priya"
print("name1:", id(name1))
name1 = "anisch"
print("name1:", id(name1))
name2 = "priya"
print("name2:", id(name2))


