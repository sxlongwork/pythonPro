import pymysql

db = pymysql.connect(host="152.136.89.241",user="root",password="Huawei123",port=3306)    # 指定数据的连接host,user,password,port,schema

cursor = db.cursor()				# 创建游标,就类似操作的光标

cursor.execute("show databases;")

print(cursor.fetchone())    	# 显示结果的一行,元组显示
print(cursor.fetchmany(2))    	# 显示结果的N行(接着前面的显示2行)，每一行都是一个元组，最后面使用一个大元组包含所有

print(cursor.fetchall())    	# 显示结果的所有行(接着前面的显示剩余的所有行)，每一行都是一个元组，最后面使用一个大元组包含所有


# 新建数据库和表
# cursor.execute("create database aaa;")
# cursor.execute("use aaa;")
# cursor.execute("create table emp(ename varchar(20),sex char(1),sal int)")
# cursor.execute("desc emp")

cursor.close()
db.close()
