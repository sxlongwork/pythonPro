from cat import Cat
from mouse import Mouse
from person import Person

"""
多态：一种事物的多种形态
多态的前提是继承和方法重写
"""


# 各有name和eat()
# tom = Cat("tom")
# jerry = Mouse("jerry")
#
# tom.eat()
# jerry.eat()

# 使用继承,父类有name和eat()，子类继承即可
tom = Cat("tom")
# tom.eat()
jerry = Mouse("jerry")
# jerry.eat()

# 人喂各个动物，猫，狗，老鼠等，但要定义每个喂的方法
# per = Person()
# per.feedCat(tom)
# per.feedMouse(jerry)

# 人喂动物，多态表示
per = Person()
per.feedAnimal(tom)
per.feedAnimal(jerry)





