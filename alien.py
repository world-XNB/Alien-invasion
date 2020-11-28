# _*_ coding:UTF-8 _*_
# 开发者：西~南~北
# 开发时间：2020/11/28   20:12
# 文件名称：alien
# 开发工具：PyCharm
# 开发用途：alien

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_game):
        """"初始化外星人并设置其初始位置。"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.x = float(self.rect.x)

    def check_edges(self):
        """"如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """向右或向右移动外星人"""
        self.x += (self.settings.alien_speed*self.settings.fleet_direction)
        self.rect.x = self.x

    def center_ship(self):
        """让飞船在屏幕低端居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x =float(self.rect.x)
