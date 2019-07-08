class User(object):
    def __init__(self, name, sex, age, phonenumbre):
        self.name = name;
        self.age = age
        self.sex = sex
        self.phonenumber = phonenumbre
        self.state = None

    def __str__(self):
        return "{}-{}-{}-{}".format(self.name, self.sex, self.age, self.phonenumber)

