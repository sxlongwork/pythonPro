# 字符串应用，密码判断
# 使用input输入一个字符串，判断是否为强密码:
# 长度至少8位,包含大写字母,小写字母,数字和下划线这四类字符则为强密码


passwd = input("pls input your passwd:")

if passwd.__len__() < 8:
    print("the passwd you input is less than 8 chracters.")
else:
    pass