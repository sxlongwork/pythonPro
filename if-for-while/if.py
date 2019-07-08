# if elif else expressions

# 单分支
if 3 > 5:
    print("oh,my gold,it's impossible.")

# 双分支
if 3 > 5:
    print("hehe~")
else:
    print("3<5 is true")

# 多分支及嵌套
age = input("pls type your age:")
sex = input("pls type your sex:")

if type(int(age)) is not int:
    print("error")
elif int(age) < 0:
    print("you type wrong age.pls input again.")
elif int(age) < 18:
    print("it's a boy.")
else:
    if sex == "man" or sex == "male":
        print("you are %s years old, is a %s" % (age, sex))
    elif sex == "woman" or sex == "female":
        print("you are {} years old ,is a {}".format(age, sex))
    else:
        print("you type wrong sex,pls input again")
