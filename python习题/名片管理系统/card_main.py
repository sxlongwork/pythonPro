import card_tools


def main():
    while True:

        # 显示菜单功能
        card_tools.show_menu()

        user_action = input("请选择你要使用的功能:")
        # 判断用户输入
        if user_action in ['1', '2', '3']:

            if user_action == '1':
                card_tools.card_add()

            elif user_action == '2':
                card_tools.show_all()

            elif user_action == '3':
                card_tools.search()
        # 退出系统
        elif user_action == '0':
            print('欢迎再次使用【名片管理系统】')
            break
        # 输入有误重新输入
        else:
            print('输入有误，请重新输入')


if __name__ == '__main__':
    main()