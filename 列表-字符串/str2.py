# str的拼接与格式化输出

name = "xiaoming"
str1 = "hello "+name+",fine?"  # 万恶的+
print(str1)

print("hello ===%s===" % name)
print("hello ==={}===".format(name))

age = 45
print("you are "+str(age)+" years old.")
print("you are %d years old." % age)
print("you are {} years old.".format(age))


