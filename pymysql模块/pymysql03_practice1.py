import pymysql

# 192.168.211.103
# 链接时出现链接不上，需要注意：
# 1.远程主机的防火墙要关闭
# 2.远程主机的mysql要设置客户端可以链接，grant all on *.* to 'root'@'223.104.3.157' identified by 'Huawei123'
db = pymysql.connect(host='152.136.89.241', user='root', password='Huawei123', port=3306)

cursor = db.cursor()

# cursor.execute("show databases;")d

# cursor.execute("use bank;")
# cursor.execute("create database userinfo;")
cursor.execute("use db_student;")
# cursor.execute("create table user(name varchar(20),sex char(5),age int, phone varchar(20));")
cursor.execute("select * from t_student;")
stu_data = ('xiaoming', '001', 'class01', '23', 'man')
cursor.execute("insert into t_student(name,stu_num,class_num,age,sex) values (%s, %s, %s, %s, %s);", stu_data)
db.commit()
name = 'aa'
stu_num = '11'
cursor.execute("select * from t_student where name = '%s';" % name)
# cursor.execute("select * from t_student where stu_num = %s;" % stu_num)
data = cursor.fetchall()

if len(data) == 0:
    print("it's empty.")
else:
    print(data)


# print(cursor.fetchall())

cursor.close()
db.close()