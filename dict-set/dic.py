# dic 使用

# dic->dictionary ,存储键值对，有极快的查找速度


dic = {"first": 1, "second": 2, "third": 3}
print(dic)
print(len(dic))
print(dic['first'])
print("="*20)
# 添加元素和修改元素
# dict内部存放的顺序和key放入的顺序是没有关系的。
dic['first'] = "one"
dic['fourth'] = 4

# 删除元素,pop(key)
dic.pop('first')
# del 删除元素
del dic['second']
print(len(dic))
print(dic)

# 判断key是否在dic字典中,如果在，就使用dic.get(key值)方法获取key对应的值；也可以使用dic['key值']获取
# 如果key值不存在，使用get方法获取时返回None，或自己指定的值,如dic.get(key, -1)，key不存在，返回-1
if "third" in dic:
    print("yes, the value is %s" % dic.get('third'))
else:
    print("no")


'''
总结
1.dict的key必须是不可变对象
2.添加/修改元素可通过dic[key]=xxx的方法
3.删除元素.pop(key)方法，或del dic[key];清空dict可使用.clear()方法;删除字典可使用del dic
4.获取值使用.get(key)方法，key不存在会返回None；或使用dic[key]获取，key不存在会报错
1.dict与list的比较
dict的特性
查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
list的特性
查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。

'''
