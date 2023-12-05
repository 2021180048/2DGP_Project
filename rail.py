from header import *
import game_framework
import play_mode

PIXEL_PER_METER = 100
RAIL_SPEED_KMPH = 2.0
RAIL_SPEED_MPM = RAIL_SPEED_KMPH * 1000.0 / 60.0
RAIL_SPEED_MPS = RAIL_SPEED_MPM / 60.0
RAIL_SPEED_PPS = RAIL_SPEED_MPS * PIXEL_PER_METER

class Rail_0():

    def __init__(self):
        self.x = 1300
        self.y = 2760   
        self.x1, self.y1, self.x2, self.y2 = 310, -20, 310, 30
        self.image = load_image('rail.png')
        pass

    def handle_event(self, event):
        pass

    def update(self):
        if play_mode.boy.x > 11000:
            self.x = 12700
            self.y = 1050
        elif play_mode.boy.x > 7134:
            self.x = 8500
            self.y = 1750
            pass
        self.sx = self.x - play_mode.back_ground.window_left
        self.sy = self.y - play_mode.back_ground.window_bottom
        pass

    def draw(self):
        self.image.draw(self.sx, self.sy)        
        # draw_rectangle(*self.get_bb())
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
        self.y = 2425
        self.x1, self.y1, self.x2, self.y2 = 285, -20, 285, 40
        self.image = load_image('stone_rail.png')
        pass

    def handle_event(self, event):
        pass

    def update(self):

        if play_mode.boy.x > 12000:
            self.x = 14500
            self.y = 690
        elif play_mode.boy.x > 7000:
            self.x = 10500
            self.y = 1410

        self.sx = self.x - play_mode.back_ground.window_left
        self.sy = self.y - play_mode.back_ground.window_bottom
        pass

    def draw(self):
        self.image.draw(self.sx, self.sy)        
        # draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.sx - self.x1, self.sy - self.y1, self.sx + self.x2, self.sy + self.y2  # 튜플

    def handle_collision(self, group, other):
        pass

    def handle_not_collision(self, group, other):
        pass

class Round_Rail_0():

    def __init__(self):
        self.x = 6200
        self.y = 2100
        self.x1, self.y1, self.x2, self.y2 = 310, -30, 330, 45
        self.image = load_image('round_rail.png')
        pass

    def handle_event(self, event):
        pass

    def update(self):

        if play_mode.boy.x > 10000:
            self.x = 15100
            self.y = 700
        elif play_mode.boy.x > 8000:
            self.x = 12300
            self.y = 1060
        self.sx = self.x - play_mode.back_ground.window_left
        self.sy = self.y - play_mode.back_ground.window_bottom
        pass

    def draw(self):
        self.image.draw(self.sx, self.sy)        
        # draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.sx - self.x1, self.sy - self.y1, self.sx + self.x2, self.sy + self.y2  # 튜플

    def handle_collision(self, group, other):
        pass

    def handle_not_collision(self, group, other):
        pass


    
