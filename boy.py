# 이것은 각 상태들을 객체로 구현한 것임.
TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8
FRAMES_PER_TIME = ACTION_PER_TIME * FRAMES_PER_ACTION

PIXEL_PER_METER = 100
RUN_SPEED_KMPH = 2.0
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000.0 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

from pico2d import *
import game_world
import game_framework

# state event check
# ( state event type, event value )

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def a_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a

def a_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a

def time_out(e):
    return e[0] == 'TIME_OUT'

def meter_out(e):
    return e[0] == 'METER_OUT'

def frame_out(e):
    return e[0] == 'FRAME_OUT'

# time_out = lambda e : e[0] == 'TIME_OUT'

class Start:
    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        boy.bottom = 780
        boy.wait_time = get_time()
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        if boy.x <= 230:
            boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time) % 6
            boy.x += RUN_SPEED_PPS * game_framework.frame_time
            boy.left = int(boy.frame)*200 + 80
        else:
            boy.state_machine.handle_event(('METER_OUT', 0))
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.left, boy.bottom, 80, 80, boy.x, boy.y, 120, 120)
        pass

class UpSpeed:
    @staticmethod
    def enter(boy, e):
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy, e):
        if int(boy.frame) < 13:
            boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time) % 13
            boy.left = int(boy.frame)*80 + 80
        else:
            boy.state_machine.handle_event(('INPUT', e))
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.left, boy.bottom, 80, 80, boy.x, boy.y, 120, 120)
        pass
    

class Idle:

    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time) % 4
        if 0 <= int(boy.frame) < 2:
            boy.left = 0
            boy.bottom = 700
        elif 2 <= int(boy.frame) < 4:
            boy.left = 0
            boy.bottom = 75
        # elif 4 <= int(boy.frame) < 6:
        #     boy.left = 80
        #     boy.bottom = 75

        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.left, boy.bottom, 80, 75, boy.x, boy.y, 120, 120)
        pass



class Run:

    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        boy.wait_time = get_time()
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time) % 12
        boy.left = int(boy.frame)*80 + 80
        boy.bottom = 700
        if get_time() - boy.wait_time > 3.0:
            boy.state_machine.handle_event(('TIME_OUT', 0))
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.left, boy.bottom, 80, 80, boy.x, boy.y, 120, 120)


class Ride:

    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        if int(boy.frame) < 12:
            boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time)
        else:
            boy.state_machine.handle_event(('FRAME_OUT', 0))

        if int(boy.frame) < 9:
            boy.left = int(boy.frame)*81 + 810
            boy.bottom = 151
        else:
            boy.left = int(boy.frame)*81 + 320
            boy.bottom = 380
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.left, boy.bottom, 80, 80, boy.x, boy.y, 120, 120)



class Sleep:

    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    @staticmethod
    def draw(boy):
        if boy.face_dir == -1:
            boy.image.clip_composite_draw(boy.frame * 100, 200, 100, 100,
                                          -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100,
                                          3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)


class StateMachine:
    def __init__(self, boy):
        self.boy = boy
        self.cur_state = Start
        self.transitions = {
            Start: {meter_out: Run},
            Ride: {frame_out: Idle},
            Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out: Sleep, space_down: Idle, a_down: UpSpeed},
            Run: {time_out: Ride},
            Sleep: {right_down: Run, left_down: Run, right_up: Run, left_up: Run}
        }

    def start(self):
        self.cur_state.enter(self.boy, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.boy)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.boy, e)
                self.cur_state = next_state
                self.cur_state.enter(self.boy, e)
                return True
        return False

    def draw(self):
        self.cur_state.draw(self.boy)


class Boy:
    def __init__(self):
        self.x, self.y = 100, 90

        self.frame = 0
        self.action = 0
        self.left = 0
        self.bottom = 0
        self.image = load_image('skater_sprite_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        # if self.frame <= 15:
        #     self.frame = (self.frame + FRAMES_PER_TIME * game_framework.frame_time)
        #     self.action = 460        
        self.state_machine.update()
        pass

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))
        pass

    def draw(self):
        #  self.image.clip_draw(int(self.frame) * 200, self.action, 80, 80, self.x, self.y, 120, 120)
        self.state_machine.draw()
        pass
