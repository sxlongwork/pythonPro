# variables  不同类型的变量不能使用+拼接
a = -3

b = 3
print("a+b=",a+b,sep="")  # 将seq中的内容插入到values中

a = float(a)
print(type(a), a+4)

name = "xiaoming"
age = 23
# print(name, "you " + age + "years old")   # TypeError: must be str, not int
print(name, "you " + str(age) + " years old")
