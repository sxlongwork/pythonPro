# list 使用
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素
classmates = ["zhangsan", "lisi", "wangwu", "xiaoming"]
print(classmates)
print(classmates.index("lisi")) #根据元素获取该元素的下标
print("classmates length is %s" % len(classmates))      # len可以获取list元素个数

for i in range(len(classmates)):
    print(classmates[i])                    # 通过下标即索引可以遍历list中的每一个成员，索引从0开始

# print(classmates[4])       # IndexError: list index out of range,索引超出范围
# help(len)
print("="*20)
print(classmates[-1])   # 倒数第一个元素，即最后一个元素
print(classmates[-2])   # 倒数第二个元素
print(classmates[-3])   # 倒数第三个元素
print(classmates[-4])   # 倒数第四个元素，
# print(classmates[-5])      # IndexError: list index out of range

# 添加元素
print("="*30)
classmates.append("xianqian")   # append添加元素到list末尾
print(classmates)
classmates.insert(1, "aiai")    # insert添加元素到list指定下标位置,1为指定下标
print(classmates)

# 删除元素
print("="*30)
classmates.pop()    # 删除最后一个元素
print(classmates)
classmates.pop(1)   # 删除指定下标位置的元素
print(classmates)

# 替换元素，可以直接给对应位置的元素重新赋值
classmates[3] = "xianqian"
classmates.sort()
print(classmates)


# list中的元素可以是多类型的，数字，字符串等，也可以是一个list
L = []
# list 可以为空，一个元素也没有
print(len(L))

'''
总结
1.list是一个有序的集合列表
2.len(list_name)可以获取list的元素个数
3.可以通过下标来获取list中的每一个元素，下标从0开始;也可以使用list[-1],list[-2]...获取倒数第一,倒数第二...个元素，直到第一个
4.list.append("xxx")可以将xxx加入到list末尾
  list.insert(下标，"xxx")可以将xxx加入到list的指定下标位置
5.list.pop()可以删除list的最后一个元素
  list.pop(i)可以删除list下标为i位置的元素
6.替换元素可以直接赋值，list[i] = "xxx"
7.list中可以包含多种类型的元素，数字，字符串，也可以是另一个list,list[i][j]可以获取list下标i位置的元素的第j位置的元素
8.list可以为空，元素个数为0个
'''