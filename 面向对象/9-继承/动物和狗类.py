class Animal:
    def eat(self):
        print("eat...")

    def drink(self):
        print("drink")


class Dog(Animal):
    """
    Dog类继承Animal类，就拥有Aninal类的属性和方法
    """
    def bark(self):
        print("barking...")


dog = Dog()
dog.eat()
dog.drink()
dog.bark()