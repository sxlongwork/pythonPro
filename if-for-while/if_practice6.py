# if practice

has = input("if you have ticket(yes/no):")

len = int(input("pls input length of your knife(cm):"))

if has == "yes":
    if len >=20:
        print("your knife is too long,it's {}cm".format(len))
    else:
        print("you can come in now.")
else:
    print("you need buy ticket first")
