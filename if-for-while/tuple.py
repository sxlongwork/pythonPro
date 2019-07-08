# tuple 使用

# 元组tuple一旦定义，就不能改变，这里的不能改变指的是指向不变改变

classmates = ("zhangsan", "lisi", "wangwu", "xiaoming")
print(len(classmates))
print(classmates)
for i in range(len(classmates)):
    print(classmates[i])

# 在定义tuple时，元素就必须确定下来
aa = (1, "ok")
# aa[0] = 2 tuple元素不能修改
print(aa)

# 在定义只有一个元素的tuple时，注意要在第一个元素后加上",",aa=(2,)，否则会被认为是赋值aa=(2)
aa = (2, )  # tuple
print(type(aa))
aa = (2)    # int,被认为是一个数字
print(type(aa))

# tuple的元素指向不变，但指定的内容可变
classes = [1, 2]
tuple1 = ("a", "b", classes)    # tuple1指向classes没有变，但classes本身的内容是可以变的
print(tuple1)
classes[0] = 11
classes[1] = 22
print(tuple1)

'''
总结
1.tuple与list类似，但是是不可变的，一旦定义，就不能修改
2.获取元素的方式和元素个数与list相同
3.当定义只有一个元素的tuple时，注意要在元素后加上","
4.tuple一旦初始化后就不能改变指的是指向不能变，但被指的元素内容可变

'''

# 测试使用
print("===============================")
tuple1 = (1, 2, 3, 2, 4, 5)

# 获取元组元素个数，即元素长度
print(len(tuple1))
print(tuple1.__len__())
# for i in tuple1:
#     print(i)

# print(tuple1[::])       # 获取所有元素
# print(tuple1[::-1])     # 倒序打印元组所有元素,tuple1元素本身不变
# print(tuple1[1:3])      # 获取下标为1, 2的元素(2, 3)
# print(tuple1[:4])       # 不写起始位置，默认从头开始，0，1，2，3，(1,2,3,4)
# print(tuple1[3:])       # 不写结束位置，默认一直截到最后，3，4，(4,5)

print(tuple1.count(2))      # .count(e),获取元素e在元组中出现的次数
print(tuple1.index(2))      # .index(e),获取元素e在元组中第一次出现时的下标
