from header import*
import game_framework

PIXEL_PER_METER = 100
RAIL_SPEED_KMPH = 2.0
RAIL_SPEED_MPM = RAIL_SPEED_KMPH * 1000.0 / 60.0
RAIL_SPEED_MPS = RAIL_SPEED_MPM / 60.0
RAIL_SPEED_PPS = RAIL_SPEED_MPS * PIXEL_PER_METER

class Rail():

    def __init__(self):
        self.x = 1200
        self.y = 180
        self.speed = 0
        self.wait_time = 0.0        
        self.x1, self.y1, self.x2, self.y2 = 160, -10, 180, 20
        self.image = load_image('rail.png')
        pass

    def handle_event(self, event):
        pass

    def update(self):
        self.x -= RAIL_SPEED_PPS * game_framework.frame_time * self.speed
        if int(self.x) <= -800:
            self.x = 1600
        pass

    def draw(self):
        self.image.draw(self.x, self.y)        
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x - self.x1, self.y - self.y1, self.x + self.x2, self.y + self.y2  # 튜플
    
    def handle_collision(self, group, other):
        if group == 'boy:rail':
            pass

        if group == 'back_ground:rail':
            pass

    def handle_not_collision(self, group, other):
        if group == 'boy:rail':
            pass

        if group == 'back_ground:rail':
            pass

    
