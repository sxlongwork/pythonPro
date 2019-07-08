import pymysql

# 指定数据的连接host,user,password,port,schema
db_connect = pymysql.connect(host="152.136.89.241", user="root", password="Huawei123", port=3306)
cursor = db_connect.cursor()


def initdata():
    """初始化数据库和数据表

    :return:
    """

    # 新建数据库和表
    cursor.execute("create database db_student default charset=utf8;")
    cursor.execute("use db_student;")
    cursor.execute("create table t_student(name varchar(30),stu_num varchar(10)"
                   ",class_num varchar(10),age varchar(3), sex enum('man', 'woman'));")


def destroy():
    """ 删除数据库

    :return:
    """
    cursor.execute("drop database db_student;")


def findstubynum(stu_num):
    """根据学号查询学生

    :param stu_num: 学生学号
    :return:
    """
    cursor.execute("select * from t_student where stu_num = %s;" % stu_num)
    data = cursor.fetchall()
    return data
    # if len(data) == 0:
    #     return False
    # else:
    #     return True


def addstu(stu_dict):
    """添加学生信息

    :param stu_dict: 学生信息字典
    :return:
    """
    name = stu_dict['name']
    stu_num = stu_dict['stu_num']
    class_num = stu_dict['class_num']
    age = stu_dict['age']
    sex = stu_dict['sex']
    stu_data = (name, stu_num, class_num, age, sex)
    # print(stu_data)
    # cursor.execute("insert into t_student values (%s, %s, %s, %d, %s);" % data)
    cursor.execute("insert into t_student(name,stu_num,class_num,age,sex) values (%s, %s, %s, %s, %s);", stu_data)
    db_connect.commit()


def searchall():
    """查询所有学生信息

    :return: 返回查询结果
    """
    cursor.execute("select * from t_student order by name;")
    data = cursor.fetchall()

    return data


def findbyname(name):
    """根据学生姓名查找学生

    :param name: 学生姓名
    :return:
    """
    cursor.execute("select * from t_student where name = '%s';" % name)
    data = cursor.fetchall()
    return data
