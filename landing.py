from header import *
import game_framework


class Landing:
    def __init__(self):
        self.x = 800
        self.y = 300
        self.x1, self.y1, self.x2, self.y2 = 800, 300, 800, -100

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return 800 - self.x1, 300 - self.y1, 800 + self.x2, 300 + self.y2  # 튜플

    def handle_collision(self, group, other):
        if group == 'boy:landing':
            pass

    def handle_not_collision(self, group, other):
        if group == 'boy:landing':
            pass