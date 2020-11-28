# _*_ coding:UTF-8 _*_
# 开发者：西~南~北
# 开发时间：2020/11/28   21:45
# 文件名称：game_starts
# 开发工具：PyCharm
# 开发用途：跟踪游戏统计信息

class GameStates:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()
        # 游戏刚启动时处于活动状态
        self.game_active = True

    def reset_stats(self):
        """初始化在游戏运行期间可能的变化的统计信息"""
        self.ships_left = self.settings.ship_limit
