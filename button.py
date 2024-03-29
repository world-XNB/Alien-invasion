# _*_ coding:UTF-8 _*_
# 开发者：西~南~北
# 开发时间：2020/11/29   13:48
# 文件名称：button
# 开发工具：PyCharm
# 开发用途：alien invation's button

import pygame.font


class Button:
    def __init__(self, ai_game, msg):
        """初始化按钮的属性"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 设置按钮的尺寸和属性
        self.width, self.height = 200, 50
        self.button_color = (200, 100, 200)
        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 48)

        # 创建按钮的rect对象，并使其居中。
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只需要创建一次
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """将msg为图像，并使按钮居中。"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制一个有颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
