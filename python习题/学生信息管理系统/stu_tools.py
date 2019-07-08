import db_tools



def showmenu():
    """显示菜单"""
    print('*' * 50)
    print('欢迎使用学生信息管理系统')
    print('1 添加学生')
    print('2 查询全部')
    print('3 查询学生')
    print()

    print('0 退出系统')

    print('*' * 50)


def addstu():

    # 用户输入学生信息
    name = input('请输入你的姓名:')
    stu_num = input('请输入你的学号:')
    class_num = input('请输入你的班级:')
    age = input('请输入你的年龄:')
    sex = input('请输入你的性别:')

    # 根据学号查询该学生是否已经在数据表中,在数据表中返回True;不在数据库中返回false
    data = db_tools.findstubynum(stu_num)

    # 将学生信息存储在字典中
    if len(data) != 0:
        print('该学生信息已经在数据库中，请重新选择')
    else:
        stu_dict = {'name': name, 'stu_num': stu_num, 'class_num': class_num, 'age': age, 'sex': sex}
        db_tools.addstu(stu_dict)
        print('添加学生信息成功')


def showall():
    # 查询所有学生信息
    all_data = db_tools.searchall()
    if len(all_data) == 0:
        print("当前系统中没有任何的学生信息")
    else:
        showinfo(all_data)


def search():
    """查询学生

    :return:
    """
    while True:
        print('-' * 50)
        print("1 按姓名查找")
        print("2 按学号查找")
        print('-' * 50)
        user_select = input("请选择查找方式:")

        if user_select in ('1', '2'):

            # 按学生姓名查找
            if user_select == '1':
                user_name = input("请输入你要查找的姓名:")

                data = db_tools.findbyname(user_name)
            # 按学号查找
            else:
                user_num = input("请输入你要查找的学号:")
                data = db_tools.findstubynum(user_num)

            if len(data) == 0:
                print("没有找到你要查询的学生")
            else:
                showinfo(data)
            break
        else:
            print("【ERROR】  输入有误请重新选择")


def showinfo(data):
    print("%s\t\t%s\t\t%s\t\t%s\t\t%s" % ("姓名", "学号", "班级编号", "年龄", "性别"))
    print('-' * 50)
    for stu_tup in data:
        name = stu_tup[0]
        stu_num = stu_tup[1]
        class_num = stu_tup[2]
        age = stu_tup[3]
        sex = stu_tup[4]
        print("%s\t\t%s\t\t%s\t\t%s\t\t%s" % (name, stu_num, class_num, age, sex))
    print('-' * 50)

