from header import *
import game_framework
import play_mode

PIXEL_PER_METER = 100
MAP_SPEED_KMPH = 2.0
MAP_SPEED_MPM = MAP_SPEED_KMPH * 1000.0 / 60.0
MAP_SPEED_MPS = MAP_SPEED_MPM / 60.0
MAP_SPEED_PPS = MAP_SPEED_MPS * PIXEL_PER_METER

class Back_ground:
    
    image = None
    
    def __init__(self):
        if Back_ground.image == None:
            self.image = load_image('back_ground_new.png')

        self.x = 0
        self.y = 0
        self.score = 0
        self.buffer = 0
        self.wait_time = 0.0
        self.bad = 0
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.image.w # 배경의 너비
        self.h = self.image.h # 배경의 높이
        self.font = load_font('ENCR10B.TTF', 30)
        self.window_left = 0
        self.window_bottom = 0
    
    def handle_event(self, event):
        pass

    def update(self):
        self.window_left = clamp(0, int(play_mode.boy.x) - 300, self.w - self.cw - 1)
        self.window_bottom = clamp(0, int(play_mode.boy.y) - self.ch // 2, self.h - self.ch - 1)

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.cw, self.ch, 0, 0)
        # self.image.draw(self.x + 1600, self.y, 1600, 600)
        self.font.draw(100, 550, f'speed = {play_mode.boy.speed:02d}', (0, 0, 0))
        self.font.draw(100, 500, f'score = {self.score:02d}', (0, 0, 0))
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        if play_mode.boy.x < 2380:
            return 0 - self.window_left, 0 - self.window_bottom, 2380 - self.window_left , 2730 - self.window_bottom
        elif play_mode.boy.x < 4760:
            return 2380 - self.window_left, 0 - self.window_bottom, 4760 - self.window_left , 2380 - self.window_bottom
        elif play_mode.boy.x < 7134:
            return 4760 - self.window_left, 0 - self.window_bottom, 7134 - self.window_left , 2060 - self.window_bottom
        elif play_mode.boy.x < 9514:
            return 7134 - self.window_left, 0 - self.window_bottom, 9514 - self.window_left , 1715 - self.window_bottom
        elif play_mode.boy.x < 11471:
            return 9514 - self.window_left, 0 - self.window_bottom, 11471 - self.window_left , 1369 - self.window_bottom
        elif play_mode.boy.x < 13452:
            return 11471 - self.window_left, 0 - self.window_bottom, 13452 - self.window_left , 1012 - self.window_bottom
        elif play_mode.boy.x < 15004:
            return 13452 - self.window_left, 0 - self.window_bottom, 15004 - self.window_left , 649 - self.window_bottom
        

    def handle_collision(self, group, other):
        if group == 'boy:back_ground':
            pass

        if group == 'back_ground:rail':
            pass
        

    def handle_not_collision(self, group, other):
        if group == 'boy:back_ground':
            pass

        if group == 'back_ground:rail':
            pass

class City_0:

    image = None

    def __init__(self):
        if City_0.image == None:
            self.image = load_image('city_0.png')

        self.x = get_canvas_width() // 2
        self.y = get_canvas_height() // 2
            
    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        pass

class City_1:

    image = None

    def __init__(self):
        if City_1.image == None:
            self.image = load_image('city_1.png')

        self.x = get_canvas_width() // 2
        self.y = get_canvas_height() // 2
            
    def handle_event(self, event):
        pass

    def update(self):
        if 0 < play_mode.back_ground.window_left < play_mode.back_ground.w - play_mode.back_ground.cw - 1:
            self.x -= MAP_SPEED_PPS * game_framework.frame_time * play_mode.boy.speed * 1.3
        if self.x <= -800:
            self.x = get_canvas_width() // 2

        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        self.image.draw(self.x + 1600, self.y)
        pass

class City_2:

    image = None

    def __init__(self):
        if City_2.image == None:
            self.image = load_image('city_2.png')

        self.x = get_canvas_width() // 2
        self.y = get_canvas_height() // 2
            
    def handle_event(self, event):
        pass

    def update(self):
        if 0 < play_mode.back_ground.window_left < play_mode.back_ground.w - play_mode.back_ground.cw - 1:
            self.x -= MAP_SPEED_PPS * game_framework.frame_time * play_mode.boy.speed * 1.1
        if self.x <= -800:
            self.x = get_canvas_width() // 2

        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        self.image.draw(self.x + 1600, self.y)
        pass

class Star:

    image = None

    def __init__(self):
        if Star.image == None:
            self.image = load_image('star.png')

        self.x = get_canvas_width() // 2
        self.y = get_canvas_height() // 2
            
    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        pass

class Moon:

    image = None

    def __init__(self):
        if Moon.image == None:
            self.image = load_image('moon.png')

        self.x = get_canvas_width() // 2 + 650
        self.y = get_canvas_height() // 2 + 220
            
    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        pass

class Goal:

    image = None

    def __init__(self):
        if Moon.image == None:
            self.image = load_image('goal.png')

        self.x = 14800
        self.y = 750
            
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
        return self.sx - 60, self.sy -100, self.sx + 60, self.sy + 100 
        pass

    def handle_collision(self, group, other):
        if group == 'boy:goal':
            pass

        if group == 'boy:goal':
            pass

    def handle_not_collision(self, group, other):
        if group == 'boy:goal':
            pass

        if group == 'boy:goal':
            pass

