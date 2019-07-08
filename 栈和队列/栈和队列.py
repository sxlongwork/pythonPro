'''
栈：先进后出
压栈：添加元素
出栈：删除元素
'''

'''
队列：先进先出
进队
出对
'''
import collections
queue = collections.deque()

# 进队
queue.append("A")
queue.append("B")
queue.append("C")

# 出队
data1 = queue.popleft()
print(data1)
data2 = queue.popleft()
print(data2)
data3 = queue.popleft()
print(data3)
print(queue)




