# list

numbers = [1, 2, 3, 4]

# print(id(numbers))    # 打印numbers列表在解释器中的内存地址
# numbers.reverse()     # 将列表反转
# print(numbers)        # 反转后打印列表成员
# print(id(numbers))    # 再打印numbers列表在解释器中的内存地址，和上一次未修改前比较相同，说明列表是可变数据类型

# list添加成员
# numbers.append(5)   # 添加成员5到列表最后
# print(numbers)
# numbers.insert(1, 0)    # 在列表下标为1的位置添加成员0
# print(numbers)

# list删除成员
# del numbers[0]      # 删除下标0位置的元素，此时numbers = [2, 3, 4]
# numbers.remove(2)   # 删除元素2，此时numbers = [3, 4]
# numbers.pop(0)      # 删除下标0位置的元素，此时numbers = [4]
# print(numbers)      # 打印numbers = [4]
# del numbers       # 把列表都删掉了

# list 修改元素值
# numbers[0] = "one"  # 将下标0位置的元素重新赋值为"one"
# print(numbers)      # 打印numbers = ["one", 2, 3, 4]

# list 查询成员
# print(numbers[0])

# list元素个数
# print(numbers.__len__())
# print(len(numbers))

