# for 使用

# for循环遍历一个对象（比如数据序列，字符串，列表，元组等）,根据遍历的个数来确定循环次数。
for i in range(5):
    print(i, end=" ")
print()

for i in range(3, 10):
    print(i,end=" ")
print()

for i in range(1, 20, 2):
    print(i, end=" ")
print()

for i in range(20, 0, -2):
    print(i, end=" ")
print()

name = input("pls type your name:")

for i in name:
    print(i, end=" ")
print()

lists = [1, 3, 5, 7, 9]
# 注意，变量名不能使用python的关键字，虽然可以使用该变量，但是会覆盖该关键字在python中的原有含义
for i in lists:
    print(i, end=" ")

li = list(lists)
print(li)
