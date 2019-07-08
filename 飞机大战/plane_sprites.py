import pygame
from plane_main import SCREEN_RECT


class GameSprite(pygame.sprite.Sprite):
    """
    游戏精灵
    """

    def __init__(self, image, speed=1):

        # 调用父类的初始化方法
        super().__init__()

        # 定义对象属性
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕上垂直移动
        self.rect.y += self.speed


class BackGround(GameSprite):
    """游戏背景精灵"""
    def __init__(self, is_alt=False):
        super().__init__('./images/background.png')
        if is_alt:
            self.rect.y = -self.rect.height


    def update(self):
        # 调用父类update方法
        super().update()
        # 判断是否移除屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.y
