from header import *
import game_framework

PIXEL_PER_METER = 100
MAP_SPEED_KMPH = 2.0
MAP_SPEED_MPM = MAP_SPEED_KMPH * 1000.0 / 60.0
MAP_SPEED_MPS = MAP_SPEED_MPM / 60.0
MAP_SPEED_PPS = MAP_SPEED_MPS * PIXEL_PER_METER

class Back_ground:
    
    image = None
    
    def __init__(self):
        self.x = 800
        self.y = 300
        self.x1, self.y1, self.x2, self.y2 = 800, 300, 800, -150
        self.speed = 0
        self.score = 0
        self.buffer = 0
        self.wait_time = 0.0
        self.bad = 0
        self.font = load_font('ENCR10B.TTF', 30)

        if Back_ground.image == None:
            self.image = load_image('back_ground.jpg')
    
    def handle_event(self, event):
        pass

    def update(self):
        self.x -= MAP_SPEED_PPS * game_framework.frame_time * self.speed
        if int(self.x) <= -800:
            self.x = 800
        pass

    def draw(self):
        self.image.draw(self.x, self.y, 1600, 600)
        self.image.draw(self.x + 1600, self.y, 1600, 600)
        self.font.draw(100, 550, f'speed = {self.speed:02d}', (0, 0, 0))
        self.font.draw(100, 500, f'score = {self.score:02d}', (0, 0, 0))


        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return 800 - self.x1, 300 - self.y1, 800 + self.x2, 300 + self.y2  # 튜플

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
