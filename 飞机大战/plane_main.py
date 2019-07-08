import pygame
from plane_sprites import *

# 定义屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# 定义刷新帧率
FRAME_PER_SECOND = 60


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):

        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法创建精灵和精灵组
        self.__create_sprites()

    def __create_sprites(self):
        bg1 = BackGround()
        bg2 = BackGround(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

    def start_game(self):
        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SECOND)
            # 时间监听
            self.__event_handler()
            # 检查碰撞
            self.__check_collide()
            # 更新或绘制精灵
            self.__update_sprites()
            # 更新显示
            pygame.display.update()
            pass

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

    def __check_collide(self):
        pass

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()


if __name__ == '__main__':

    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()