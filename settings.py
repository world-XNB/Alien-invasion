# _*_ coding:UTF-8 _*_
# 开发者：西~南~北
# 开发时间：2020/11/28   14:56
# 文件名称：settings
# 开发工具：PyCharm
# 开发用途：alien_invation's setting
class Settings:
    """"存储《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置。"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # 飞船设置
        self.ship_speed = 1
        self.ship_limit = 3
        # 子弹设置
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction为1向右移动，为-1向左移动
        self.fleet_direction = 1
