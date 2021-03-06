class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 子弹设置
        self.bullet_speed_factor = 3
        #self.bullet_width = 3
        self.bullet_width = 200
        #self.bullet_height = 15
        self.bullet_height = 10
        self.bullet_color = 0, 0, 255

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 100
        # fleet_direction为1表示向右移,为-1表示向左移
        self.fleet_direction = 1
