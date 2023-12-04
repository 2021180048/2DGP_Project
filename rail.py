from header import*
import game_framework
import play_mode

PIXEL_PER_METER = 100
RAIL_SPEED_KMPH = 2.0
RAIL_SPEED_MPM = RAIL_SPEED_KMPH * 1000.0 / 60.0
RAIL_SPEED_MPS = RAIL_SPEED_MPM / 60.0
RAIL_SPEED_PPS = RAIL_SPEED_MPS * PIXEL_PER_METER

class Rail_0():

    def __init__(self):
        self.x = 1100
        self.y = 2760   
        self.x1, self.y1, self.x2, self.y2 = 340, -15, 360, 35
        self.image = load_image('rail.png')
        pass

    def handle_event(self, event):
        pass

    def update(self):
        self.sx = self.x - play_mode.back_ground.window_left
        self.sy = self.y - play_mode.back_ground.window_bottom
        pass

    def draw(self):
        self.image.draw(self.sx, self.sy)        
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.sx - self.x1, self.sy - self.y1, self.sx + self.x2, self.sy + self.y2  # 튜플
    
    def handle_collision(self, group, other):
        pass

    def handle_not_collision(self, group, other):
        pass

class Stone_Rail_0():

    def __init__(self):
        self.x = 3500
        self.y = 2430
        self.x1, self.y1, self.x2, self.y2 = 290, -20, 290, 50
        self.image = load_image('stone_rail.png')
        pass

    def handle_event(self, event):
        pass

    def update(self):
        self.sx = self.x - play_mode.back_ground.window_left
        self.sy = self.y - play_mode.back_ground.window_bottom
        pass

    def draw(self):
        self.image.draw(self.sx, self.sy)        
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.sx - self.x1, self.sy - self.y1, self.sx + self.x2, self.sy + self.y2  # 튜플

    def handle_collision(self, group, other):
        pass

    def handle_not_collision(self, group, other):
        pass


    
