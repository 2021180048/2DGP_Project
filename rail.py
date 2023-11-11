from header import*

PIXEL_PER_METER = 100
RAIL_SPEED_KMPH = 2.0
RAIL_SPEED_MPM = RAIL_SPEED_KMPH * 1000.0 / 60.0
RAIL_SPEED_MPS = RAIL_SPEED_MPM / 60.0
RAIL_SPEED_PPS = RAIL_SPEED_MPS * PIXEL_PER_METER

class Rail():

    def __init__(self):
        self.x = 1200
        self.y = 180
        self.x1, self.y1, self.x2, self.y2 = 100, 25, 100, 20
        self.image = load_image('rail.png')
        pass

    def handle_event(self, event):
        pass

    def update(self):
        self.x -= 0.01
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x - self.x1, self.y - self.y1, self.x + self.x2, self.y + self.y2  # 튜플
    
