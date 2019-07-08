import pygame
from plane_sprites import *

# init()为初始化方法，执行该方法会加载pygame的是所有模块，便于后面调用
pygame.init()

# pygane,Rect(x,y,width,height)类是用来创建矩形区域的类,(x, y)为原点位置，width为宽，height为高，调用该类不需要提前执行init()
# hero_rect = pygame.Rect(100, 100, 150, 250)
# 初始化游戏窗口
screen = pygame.display.set_mode((480, 700))

# 加载背景图
# 1.将图像加载到内存
bg = pygame.image.load('./images/background.png')
# 2.使用游戏窗口对象加载图像,(0,0)为图片位置
screen.blit(bg, (0, 0))
# 3，使用pygame.display.update()方法更新使图像显示
# pygame.display.update()

# 绘制英雄图像
hero = pygame.image.load('./images/hero.png')
screen.blit(hero, (200, 500))
# 可以让screen对象完成所有的blit后再调用update()更新
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 英雄的矩形区域对象
hero_rect = pygame.Rect(200, 500, 100, 124)

# 创建敌机精灵
enemy = GameSprite('./images/enemy.png')
# 创建敌机精灵组
enemygroup = pygame.sprite.Group(enemy)

# 游戏循环，游戏真正的开始
while True:

    # 设置帧率，让循环内的代码每秒执行多少次
    clock.tick(60)

    # 捕获事件,针对用户的操作时间进行不同的处理
    for event in pygame.event.get():

        # 判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            # 卸载所有模块
            pygame.quit()
            # 退出程序
            exit()

    # 修改英雄的位置
    hero_rect.y -= 1

    # 判断飞机的位置，当飞机到顶端时将飞机移动到屏幕底端
    if hero_rect.y <= -124:
        hero_rect.y = 700

    # 重新绘制所有图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    enemygroup.update()
    enemygroup.draw(screen)

    # 调用update方法更新屏幕显示
    pygame.display.update()

    pass

# 卸载加载到内存中的所有模块，退出游戏
pygame.quit()