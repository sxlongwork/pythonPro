class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "%s的体重是%.2f公斤" % (self.name, self.weight)

    def eat(self):
        print('%s吃东西了' % self.name)

        #self.weight = self.weight + 1
        self.weight += 1

    def run(self):
        print('%s跑步了' % self.name)
        # self.weight = self.weight - 0.5
        self.weight -= 0.5


xiaoming = Person('xiaoming', 75.0)
xiaoming.eat()
# print(xiaoming)
xiaoming.run()
print(xiaoming)

xiaomei = Person('xiaomei', 45.0)
xiaomei.run()
xiaomei.eat()
print(xiaomei)
