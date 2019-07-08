# set 使用

# set 与dict类似，存储key，但set不存储值，key不能重复，有重复key，输出时会自动去掉
# set 可以看成时一个无序和无重复的集合

# help(set)

set1 = {1, 2, 2, 2}
print(type(set1))
print(len(set1))
print(set1)
print("="*20)
set1.add(3)
set1.add("hehe")
print(set1)
# remove移除元素，如果不存在，会报错
# set1.remove(5)
set1.remove(1)
# discard移除元素，如果不存在，不会报错
set1.discard(5)
# pop()随机删除一个元素
set1.pop()
print(set1)
if 3 in set1:
    print(3)

print("-"*30)
set1.add((1, 2, 3))
# set1.add((1, [2, 3])) # 列表无法加入set中
print(set1)
'''
总结
1.set是无序，无重复元素的集合
2.添加元素add(xxx)
3.删除元素remove(xxx),discard(xxx),pop();clear()清空set集合
4.len(set1)取集合元素个数,重复元素只算一个
5.xx in set1,判断xx是否在set1中
'''