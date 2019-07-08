class Gun:
    def __init__(self, model, bullet_count):
        self.model = model
        self.bullet_count = bullet_count

    def shoot(self):
        if self.bullet_count <= 0:
            print('没有子弹了，无法射击')
        else:
            self.bullet_count -= 1
            print('射击成功,剩余子弹数量为%d' % self.bullet_count)

    def add_bullet(self, num):
        self.bullet_count += num
        print('添加了%d颗子弹，当前有%d颗子弹' % (num, self.bullet_count))

class Soldier:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def fire(self):
        self.gun.shoot()

gun = Gun('AK-47', 5)
xusanduo = Soldier('许三多', gun)
xusanduo.fire()
xusanduo.fire()
xusanduo.fire()
xusanduo.fire()
xusanduo.fire()
xusanduo.fire()
gun.add_bullet(3)
xusanduo.fire()