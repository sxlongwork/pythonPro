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