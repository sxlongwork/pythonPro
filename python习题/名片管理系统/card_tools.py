
card_list = []


def show_menu():
    """菜单展示"""
    print('*' * 50)
    print('1.新增名片')
    print('2.显示全部')
    print('3.搜索名片')
    print()
    print('0.退出系统')
    print('*' * 50)


def card_add():
    """新增名片方法"""
    # 用户输入信息
    name_str = input('请输入你的姓名:')
    age_str = input('请输入你的年龄:')
    phone_str = input('请输入你的电话号:')
    qq_str = input('请输入你的QQ:')

    # 将用户信息存储在字典中
    card_dict = {'name': name_str, 'age': age_str, 'phone': phone_str, 'qq': qq_str}

    # 将字典加入到card_list中
    card_list.append(card_dict)

    # 提示用户添加成功
    print('添加名片成功')


def show_all():
    """展示所有用户信息"""
    # 列表为空，则提示用户当前没有用户名片
    if len(card_list) == 0:
        print("当前没有任何用户名片")
    else:
        # 展示名片信息表头
        print("姓名\t\t年龄\t\t电话号码\t\tQQ号码")

        # 分隔符
        print('-'*50)
        # 列表不为空。则展示用户信息
        for card_dict in card_list:
            user_data = (card_dict['name'], card_dict['age'], card_dict['phone'], card_dict['qq'])
            print("%s\t\t%s\t\t%s\t\t%s" % user_data)


def search():
    """根据用户名搜索用户"""
    search_key = input("请输入你要搜索的用户名:")

    for card_dict in card_list:

        # 如果搜到则展示用户信息
        if search_key == card_dict['name']:

            # 展示名片信息表头
            print("姓名\t\t年龄\t\t电话号码\t\tQQ号码")

            # 分隔符
            print('-' * 50)
            # 列表不为空。则展示用户信息
            user_data = (card_dict['name'], card_dict['age'], card_dict['phone'], card_dict['qq'])
            print("%s\t\t%s\t\t%s\t\t%s" % user_data)

            # 分隔符
            print('-' * 50)

            # 处理名片
            deal_card(card_dict)

            break

    else:
        # 没有搜到，则给出提示
        print('你搜索的用户不再当前名片系统中')


def deal_card(card_dict):
    """搜索到用户后对用户的修改/删除操作"""

    # 循环用户的选择，输入有误可以重新选择
    while True:
        user_select = input("请输入你要进行的操作【1】修改 【2】删除 【3】返回上级菜单:")

        # 修改用户名片
        if user_select == '1':
            name = user_input(card_dict['name'],'请输入你要修改的用户名[直接回车不修改]:')
            age = user_input(card_dict['age'], '请输入你要修改的年龄[直接回车不修改]:')
            phone = user_input(card_dict['phone'], '请输入你要修改的电话号[直接回车不修改]:')
            qq = user_input(card_dict['qq'], '请输入你要修改的QQ[直接回车不修改]:')
            card_dict['name'] = name
            card_dict['age'] = age
            card_dict['phone'] = phone
            card_dict['qq'] = qq

            break
        # 删除名片
        elif user_select == '2':
            card_list.remove(card_dict)
            print("删除名片成功")
            break
        #
        elif user_select == '3':
            break
        else:
            print('输入有误')
            continue


def user_input(card_value, tips):
    """自定义用户输出功能，直接回车则返回字典原有的值，输入内容则返回内容"""
    # 提示用户输入
    result = input(tips)

    if len(result) == 0:
        return card_value
    else:
        return result
