# _*_ coding:UTF-8 _*_
# 开发者：西~南~北
# 开发时间：2020/11/29   14:39
# 文件名称：scoreboard
# 开发工具：PyCharm
# 开发用途：alien_invation's score

import pygame.font
from pygame.sprite import Group

from aircraft import Ship


class Scoreboard:
    """显示得分信息的类"""

    def __init__(self, ai_game):
        """初始化显示得分涉及的属性"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # 准备初始化得分图像
        self.prep_score()
        self.prep_heigh_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """"将得分转换为为一幅渲染图像"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        scre_str = str(self.stats.score)
        self.score_image = self.font.render(scre_str, True, self.text_color, self.settings.bg_color)

        # 在屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_heigh_score(self):
        """"将最高分渲染为图像"""
        heigh_score = round(self.stats.heigh_score, -1)
        heigh_score_str = "{:,}".format(heigh_score)
        self.heigh_score_image = self.font.render(heigh_score_str, True, self.text_color, self.settings.bg_color)

        # 将最高分放在屏幕顶部中央
        self.heigh_score_rect = self.heigh_score_image.get_rect()
        self.heigh_score_rect.centerx = self.screen_rect.centerx
        self.heigh_score_rect.top = self.score_rect.top

    def prep_level(self):
        """将等级渲染为图像"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # 将等级放在得分下面
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """显示还余下多少艏飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """在屏幕上显示得分和等级"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.heigh_score_image, self.heigh_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_heigh_score(self):
        """检查是否诞生了新的最高得分。"""
        if self.stats.score > self.stats.heigh_score:
            self.stats.heigh_score = self.stats.score
            self.prep_heigh_score()
