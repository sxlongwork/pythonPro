# variables  变量的数据类型

a = 3
b = 3.2
c = True
d = 2+4j

e = "xiaoming"

f = [1,2,3,4,5]
print(f)
for i in  f:
    print(i, end=" ")

print()
g = (2,3,4,5,6)
print(g)
for i in g:
    print(i,end=" ")
print()

h = {"name": "zhangsan", "age": 23}
print(h)
print(h.keys())
print(h.values())

setl = {1, 3, 5, 7, 9}
print(setl)

# 类型转换
int(3)
str(123)
float(34)
aa = list([12, 12, 34])
print(aa)

bb = tuple((12, 13, 14, 15))
print(bb)

# help()

cc = dict({"name": "tianleilei", "age": 50})
print(cc)
a=33
b=2
print(a%b)




