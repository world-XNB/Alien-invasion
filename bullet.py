# _*_ coding:UTF-8 _*_
# 开发者：西~南~北
# 开发时间：2020/11/28   17:03
# 文件名称：bullet
# 开发工具：PyCharm
# 开发用途：alien_invation'bullet

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """"管理飞船所发射的子弹的类"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 在（0,0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # 存储用小数点表示子弹的位置
        self.y = float(self.rect.y)

    def draw_bullet(self):
        """在屏幕上显示子弹。"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹的小数值
        self.y -= self.settings.bullet_speed
        # 更新表示子弹的rect的位置
        self.rect.y = self.y
