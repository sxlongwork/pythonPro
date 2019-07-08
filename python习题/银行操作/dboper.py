
import pymysql

class DbOper(object):
    host = ""
    user = ""
    passwd = ""
    port = 3306
    db = None
    dbInfoPath = "dbinfo.conf"

    def connect(self):
        DbOper.getInfo(self)
        # print(self.host, self.user, self.passwd, self.port)
        try:
            db = pymysql.connect(host=self.host, user=self.user, password=self.passwd, port=self.port)
        except :
            print("connect to host {} mysql failed".format(self.host))
            exit()
        return db

    def getInfo(self):
        f = None
        try:
            f = open(self.dbInfoPath, mode="r")
            data = f.readlines()
            DbOper.host = data[0].strip().split("=")[1]
            DbOper.user = data[1].strip().split("=")[1]
            DbOper.passwd = data[2].strip().split("=")[1]
            DbOper.port = int(data[3].strip().split("=")[1])
        except:
            print("open faile {} failed".format(self.dbInfoPath))
        finally:
            if f != None:
                f.close()
    def initdata(self):
        conn =DbOper.connect(self)
        cursor = conn.cursor()
        cursor.execute("create database db_bank;")
        cursor.execute("use db_bank;")
        cursor.execute("create table t_user(name varchar(20),sex char(5),age int, phone varchar(20));")
        cursor.close()
        conn.close()

