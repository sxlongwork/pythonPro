# set

# 集合主要特点:
# 1. 天生去重（去掉重复值）
# 2. 可以增，删（准确来说,集合可以增加删除元素，但不能修改元素的值)
# 3. 可以方便的求交集，并集，补集

# 集合的定义

set1 = {"xiaoming", 12, 12, "man", (1, )}

# print(set1)
# print(len(set1))    # 集合长度
# print(type(set1))   # 类型

# 集合的交集(相同的元素)
set2 = {1, 2, 3, 4, 5, 6}
set3 = {2, 4, 6, 8}
# print(set2.intersection(set3))  # 打印set2和set3的交集
# print(set2 & set3)              # &符号也是求交集
# print(set2.isdisjoint(set3))    # 判断set2和set3是否有交集，有交集返回False;没有返回True
# print(set1.isdisjoint(set2))    # 判断set1和set2是否有交集,True

# 集合的并集(合并)
# print(set2.union(set3))         # 打印结合set2和set3的并集
# print(set2 | set3)              # |符号也可以求并集


# 集合的补集
# print(set2.difference(set3))        # 打印set3集合有，set2集合没有的元素
# print(set2 - set3)                  # set3-set2 也可以求补集
# print(set3.difference(set2))        # 打印set3集合有，set2集合没有的元素
# print(set3 - set2)                  # set3-set2 也可以求补集


# 对称差集
print(set2.symmetric_difference(set3))  # set2有的set3没有的元素 加上 set2没有set3有的元素
print(set2 ^ set3)                      # ^符号也可以求对称差集

# 判断一个集合是否是另一个集合的子集
print(set2.issubset(set3))      # set2是否是集合set3的子集
print(set2.issuperset(set3))    # set2是否包含set3

print("----------------------------------------")
set2 = {1, 2, 3, 4, 5, 6}
# 添加集合元素
set2.add(7)             # 添加一个元素7
print(set2)
set2.update([9, 10])    # 一次添加多个元素
set2.update((11, 12))   # 一次添加多个元素
print(set2)

# 删除集合元素
set2.remove(9)          # 删除元素9
set2.discard(10)        # 删除元素10
print(set2)

