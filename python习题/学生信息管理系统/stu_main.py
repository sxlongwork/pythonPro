import stu_tools
import db_tools


def main():

    # 销毁所有数据
    db_tools.destroy()

    #  初始化数据,学生系统数据库和学生信息数据表
    db_tools.initdata()

    while True:

        #  菜单展示
        stu_tools.showmenu()

        # 判断用户的输入
        user_action = input("请选择你的操作:")
        if user_action in ('1', '2', '3'):

            # 添加学生信息
            if user_action == '1':
                stu_tools.addstu()

            # 显示全部
            elif user_action == '2':
                stu_tools.showall()

            # 查询学生
            else:
                stu_tools.search()
        # 退出系统
        elif user_action == '0':
            print('欢迎再次使用【学生信息管理系统】')
            break
        else:
            print('【ERROR】  您的选择有误，请重新选择......')



if __name__ == '__main__':
    main()
