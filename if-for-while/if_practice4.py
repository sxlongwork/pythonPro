# 根据年龄与性别判断对一个人的称呼

name = input("pls input your name:")
age = int(input("pls input your age:"))
sex = input("pls input your sex:")

if age >= 18:
    if sex == "man":
        print("%s,you are %d years old,is a man." % (name, age))
    elif sex == "woman":
        print("%s,you are %d years old,is a woman." % (name, age))
    else:
        print("you type wrong sex.pls input again.")
elif age >= 1:
    if sex == "man":
        print("%s,you are %d years old,is a boy." % (name, age))
    elif sex == "woman":
        print("%s,you are %d years old,is a girl." % (name, age))
    else:
        print("you type wrong sex.pls input again.")
else:
    print("you input wrong age.pls input again.")
