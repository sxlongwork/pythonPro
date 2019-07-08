import dboper

class Person(object):
    dbop = dboper.DbOper()
    db = dbop.connect()

    def register(self, user):
        # print(user.name, user.sex, user.age, user.phonenumber)
        cursor = Person.searchbyname(self, user)
        userinfo = cursor.fetchall()
        if len(userinfo) == 0:
            print("=====")
            data = [(user.name, user.sex, user.age, user.phonenumber)]
            # cursor.execute("insert into user(name, sex, age, phone) values('{}','{}','{}','{}'); ".format(user.name, user.sex, user.age, user.phonenumber))
            cursor.executemany("insert into t_user(name, sex, age, phone) values(%s,%s,%s,%s);", data)
            self.db.commit()
        else:
            print("this user has already registered.")
        cursor.close()

    def login(self, user):
        cursor = Person.searchbyname(self, user)
        userinfo = cursor.fetchall()
        if len(userinfo) == 0:
            print("this user is not registered.pls register first.")
        else:
            user.state = "online"
            print("login success.")

    def searchbyname(self, user):
        cursor = self.db.cursor()
        cursor.execute("use db_bank;")
        cursor.execute("select * from t_user where name='{}';".format(user.name))
        return cursor

    def deletebyname(self,user):
        cursor = self.db.cursor()
        cursor.execute("use db_bank;")
        cursor.execute("delete from t_user where name='{}';".format(user.name))
        cursor.execute("select * from t_user where name='{}';".format(user.name))
        userinfo = cursor.fetchall()
        if len(userinfo) == 0:
            flag = True
        else:
            flag = False
        return flag

