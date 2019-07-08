
import pickle       # 数据持久性模块

#列表可以换成元组，字典，集合等数据类型，效果相同
list1 = [1, 2, 3, 4, "xianqian"]

f = open("3.txt", mode="wb")

# write的参数为str类型，不能直接写list,tuple,dict,set等数据类型，需要导入模块pickle,使用二进制模式wb写入,
pickle.dump(list1, f)   # 将list1元素写入文件描述符f

f.close()

f1 = open("3.txt", mode="rb")

data = pickle.load(f1)      # 将f1中的数据读出来
print(data)

f.close()
