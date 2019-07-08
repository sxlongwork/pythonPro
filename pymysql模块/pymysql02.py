'''
# 比如在10.1.1.12(测试服务器)上安装数据库，然后对10.1.1.11(开发人员)授权
# mysql
MariaDB [mysql]> create database aaadb;

MariaDB [mysql]> grant all on aaadb.* to 'aaa'@'10.1.1.11' identified by '123';

MariaDB [mysql]> flush privileges;
'''
import pymysql

my_connect = pymysql.connect(host="152.136.89.241", user="root", password="Huawei123", port=3306)
# my_connect = pymysql.connect(host="192.168.211.103", user="root", password="Huawei123", port=3306, db="bank")

cursor = my_connect.cursor()

cursor.execute("show databases;")

data = cursor.fetchall()
print(data)

# 远程新建数据库和表，及插入数据方法
# cursor.execute("create table hosts(ip varchar(15),password varchar(10),hostgroup tinyint)")
# # 插入数据方法一
# cursor.execute("insert into hosts(ip,password,hostgroup) values('10.1.1.22','123456',1)")
#
# # 插入数据方法二
# insertsql = '''
#     insert into hosts
#     (ip,password,hostgroup)
#     values
#     ('10.1.1.23','123456',1),
#     ('10.1.1.24','123456',1),
#     ('10.1.1.25','123',2),
#     ('10.1.1.26','1234',2),
#     ('10.1.1.27','12345',2);
# '''
# cursor.execute(insertsql)
#
# # 插入数据方法三
# data = [
#     ('10.1.1.28','12345',2),
#     ('10.1.1.29','12345',3),
#     ('10.1.1.30','12345',3),
#     ('10.1.1.31','12345',3),
#     ('10.1.1.32','12345',3),
#     ('10.1.1.33','12345',3),
#     ('10.1.1.34','12345',3),
# ]
# cursor.executemany("insert into hosts(ip,password,hostgroup) values(%s,%s,%s);",data)
#
# my_connect.commit()					# 这里做完DML需要commit提交，否则数据库没有实际插入数据
#
# cursor.execute("select * from hosts;")
#
# print(cursor.fetchall())    # 上面不提交，这里也可以看得到


cursor.close()
my_connect.close()
