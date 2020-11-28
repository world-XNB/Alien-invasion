# _*_ coding:UTF-8 _*_
# 开发者：西~南~北
# 开发时间：2020/11/28   15:33
# 文件名称：aircraft
# 开发工具：PyCharm
# 开发用途：alien_invation's aircraft
import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置。"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外界矩形
        self.image = pygame.image.load('images/aircraft.bmp')
        self.rect = self.image.get_rect()

        # 对于每膄飞船，都将其放在最底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
