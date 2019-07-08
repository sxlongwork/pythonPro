# variables  变量值交换

a, b = 1, 2
print("a=", a, "b=", b)
a, b = b, a
print("a=", a, "b=", b)

print("-------------------------")
name1, name2 = "hello", "dear"
print("name1:", id(name1))
print("name2:", id(name2))

name1, name2 = name2, name1
print("name1:", id(name1))
print("name2:", id(name2))
