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
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外界矩形
        self.image = pygame.image.load('images/aircraft.bmp')
        self.rect = self.image.get_rect()

        # 对于每膄飞船，都将其放在最底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船的属性x存储小数值
        self.x = float(self.rect.x)
        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置。"""
        # 更新飞船而不是rectd对象的值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # 根据self.x更新rect对象
        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
