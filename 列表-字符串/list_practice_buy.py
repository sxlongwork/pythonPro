# 小购物车程序
# 1, 双十一来了，你的卡里有一定金额(自定义)
# 2, 买东西，会出现一个商品列表(商品名，价格)
# 3, 选择你要买的商品,卡里的钱够就扣钱成功，并加入到购物车;卡里钱不够则报余额不足
# （或者做成把要买的商品都先加入到购物车，最后可以查看购物车，并可以删除购物车里的商品；确定后，一次性付款）
# 4, 买完后退出，会最后显示你一共买了哪些商品和显示你的余额

# 思路
# 1.展示商品列表(list)
# 2.定义1个空列表，存储用户选择的商品
# 3.用户购买完毕后，进入结账页面，显示用户购买的商品列表，并提示用户一共需要多少钱结账
# 4.若余额不足，则提示用户可以删除购物车中的商品；还不够，则可以再删除...
# 5.结账成功，列出用户购买的商品并显示银行卡余额

money = 15000

goods_list = [
    ["iphoneX", 8000],
    ["laptop", 5000],
    ["book", 30],
    ["earphone", 100],
    ["share_girlfriend", 2000],
]
user_list = []
# 商品列表展示，用户选择商品加入购物车
while True:
    print("商品列表".center(40, '*'))
    print("商品编号".ljust(8, " ")+"商品名称".ljust(17, " ")+"商品价格".ljust(20, " "))
    for i, j in enumerate(goods_list):
        print("{}".format(i+1).ljust(10, " "), end="")
        print("{}".format(j[0]).ljust(20, " "), end="")
        print("{}".format(j[1]).ljust(20, " "), end="")
        print()
    print("****".center(40, '*'))
    user_select_product = int(input("请输入你要购买的商品编号:"))
    for i in range(1,len(goods_list)+1):
        if user_select_product == i:
            user_list.append([goods_list[user_select_product-1][0], goods_list[user_select_product-1][1]])
    buy_again_flag = input("请问你还要再买吗？请输入(yes/no):")
    if buy_again_flag == "yes":
        continue
    else:
        print("即将进入结账页面...")
        break

# 结账页面

while True:
    total_money = 0
    print("已购买商品列表".center(40, "*"))
    print("商品编号".ljust(8, " ")+"商品名称".ljust(17, " ")+"商品价格".ljust(20, " "))
    for i, j in enumerate(user_list):
        total_money += j[1]
        print("{}".format(i + 1).ljust(10, " "), end="")
        print("{}".format(j[0]).ljust(20, " "), end="")
        print("{}".format(j[1]).ljust(20, " "), end="")
        print()
    print("*******".center(40, '*'))
    delete_product_flag = input("你需要从已购买商品列表中删除商品吗？(yes/no)")
    if delete_product_flag == "yes":
        delete_product_number = int(input("请输入你要删除的商品编号:"))
        for i in range(1, len(user_list)+1):
            if delete_product_number == i:
                user_list.pop(delete_product_number-1)
                print("删除成功")
        continue
    else:
        pass
    if total_money <= money:
        confirm_buy = input("一共{}元,您确认付款吗？请输入(yes/no):".format(total_money))
        if confirm_buy == "yes":
            balance = money - total_money
            print("付款{}元成功,欢迎下次再来！".format(total_money))
            print("您的余额为{}".format(balance))
            break
        else:
            print("付款失败,若需要请重新购买商品，谢谢！")
            break
    else:
        delete_product_confirm = input("您的余额不足，需要从已购买商品列表中删除一些商品,是否确认去删除(yes/no):")
        if delete_product_confirm == "yes":
                continue
        else:
            print("付款失败,若需要请重新购买商品，谢谢！")
            break



