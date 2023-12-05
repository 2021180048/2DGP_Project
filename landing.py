from header import *
import game_framework
import play_mode


class Landing:
    def __init__(self):
        self.y = 40

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        # draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):

        if play_mode.boy.x < 2380:
            return 0 - play_mode.back_ground.window_left, 0 - play_mode.back_ground.window_bottom, 2380 - play_mode.back_ground.window_left , 2730 - play_mode.back_ground.window_bottom + self.y
        elif play_mode.boy.x < 4760:
            return 2380 - play_mode.back_ground.window_left, 0 - play_mode.back_ground.window_bottom, 4760 - play_mode.back_ground.window_left , 2380 - play_mode.back_ground.window_bottom + self.y
        elif play_mode.boy.x < 7134:
            return 4760 - play_mode.back_ground.window_left, 0 - play_mode.back_ground.window_bottom, 7134 - play_mode.back_ground.window_left , 2060 - play_mode.back_ground.window_bottom + self.y
        elif play_mode.boy.x < 9514:
            return 7134 - play_mode.back_ground.window_left, 0 - play_mode.back_ground.window_bottom, 9514 - play_mode.back_ground.window_left , 1715 - play_mode.back_ground.window_bottom + self.y
        elif play_mode.boy.x < 11471:
            return 9514 - play_mode.back_ground.window_left, 0 - play_mode.back_ground.window_bottom, 11471 - play_mode.back_ground.window_left , 1369 - play_mode.back_ground.window_bottom + self.y
        elif play_mode.boy.x < 13452:
            return 11471 - play_mode.back_ground.window_left, 0 - play_mode.back_ground.window_bottom, 13452 - play_mode.back_ground.window_left , 1012 - play_mode.back_ground.window_bottom + self.y
        elif play_mode.boy.x < 16300:
            return 13452 - play_mode.back_ground.window_left, 0 - play_mode.back_ground.window_bottom, 16300 - play_mode.back_ground.window_left , 649 - play_mode.back_ground.window_bottom + self.y

    def handle_collision(self, group, other):
        if group == 'boy:landing':
            pass

    def handle_not_collision(self, group, other):
        if group == 'boy:landing':
            pass