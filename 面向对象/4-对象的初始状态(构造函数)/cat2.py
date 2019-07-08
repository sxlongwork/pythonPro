class Cat:

    def __init__(self, name):

        self.name = name

    def eat(self):
        print('%s 吃鱼' % self.name)


cat = Cat('TOM')
cat.eat()

jery = Cat('jery')
jery.eat()