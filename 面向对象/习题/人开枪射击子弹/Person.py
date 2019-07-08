# 弹夹类
class BulletBox(object):
    def __init__(self, count):
        self.__bulletCount = count

    def setBulletCount(self, count):
        self.__bulletCount = count

    def getBulletCount(self):
        return self.__bulletCount


# Gun类
class Gun(object):
    def __init__(self,bulletBox):
        self.bulletBox = bulletBox

    def shoot(self):
        if self.bulletBox.getBulletCount() == 0:
            print("没有子弹了")
        else:
            self.bulletBox.setBulletCount(self.bulletBox.getBulletCount() -1)
            print("剩余子弹：%d" % self.bulletBox.getBulletCount())


class Person(object):
    def __init__(self, gun):
        self.__gun = gun

    def fire(self):
        self.__gun.shoot()

    def setGun(self, gun):
        self.__gun = gun

# 初始化弹夹，设定子弹数
bul = BulletBox(5)

# 初始化枪
gun = Gun(bul)

# 人射击子弹
per = Person(gun)
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
