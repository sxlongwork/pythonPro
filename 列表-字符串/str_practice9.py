# 使用input输入一个字符串，判断是否为强密码:  长度至少8位,包含大写字母,小写字母,数字和下划线这四类字符则为强密码

# import getpass
#
# password = getpass.getpass("pls input your passwd:")
#
# print(password)

password = input("pls input your passwd:")

if len(password) < 8:
    print("your passwd is less than 8 chracters.")
else:
    digit_flag = False
    lower_flag = False
    upper_flag = False
    underline_flag = False
    for i in password:
        if i.isupper():
            upper_flag = True
            continue
        elif i.islower():
            lower_flag = True
            continue
        elif i.isdigit():
            digit_flag = True
        elif i.__eq__("_"):
            underline_flag = True
        else:
            pass
    if digit_flag == True and lower_flag == True and digit_flag == True and underline_flag == True:
        print("your passwd is strong passwd.")
    else:
        print("your passwd is simple passwd.")