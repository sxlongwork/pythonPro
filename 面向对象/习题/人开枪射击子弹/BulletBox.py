# 弹夹类
class BulletBox(object):
    def __init__(self, count):
        self.__bulletCount = count

    def setBulletCount(self, count):
        self.__bulletCount = count

    def getBulletCount(self):
        return self.__bulletCount
