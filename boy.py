from header import *
import game_framework

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8
FRAMES_PER_TIME = ACTION_PER_TIME * FRAMES_PER_ACTION

PIXEL_PER_METER = 100

RUN_SPEED_KMPH = 3.0
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000.0 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

JUMP_SPEED_KMPH = 15.0
JUMP_SPEED_MPM = JUMP_SPEED_KMPH * 1000.0 / 60.0
JUMP_SPEED_MPS = JUMP_SPEED_MPM / 60.0
JUMP_SPEED_PPS = JUMP_SPEED_MPS * PIXEL_PER_METER

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
        boy.wait_time = get_time()
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time) % 6
        boy.x += RUN_SPEED_PPS * game_framework.frame_time
        boy.left = int(boy.frame)*200 + 80
        boy.bottom = 780
        if get_time() - boy.wait_time > 2.5:
            boy.state_machine.handle_event(('METER_OUT', 0))
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.left, boy.bottom, 80, 80, boy.x, boy.y, 120, 120)
        pass

class UpSpeed:

    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time) % 12
        boy.left = int(boy.frame) * 81 + 80
        boy.bottom = 75 * 5

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.left, boy.bottom, 80, 80, boy.x, boy.y, 120, 120)
        pass

class Idle:

    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        boy.radian = 0
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time) % 4
        boy.left = 0
        boy.bottom = 78 * 9
        
        if 0 <= int(boy.frame) < 2:
            boy.radian = 3.141592/180 * 1
        elif 2 <= int(boy.frame) < 4:
            boy.radian = 3.141592/180 * 0
        pass

    @staticmethod
    def draw(boy):
        # boy.image.clip_draw(boy.left, boy.bottom, 80, 75, boy.x, boy.y, 120, 120)
        boy.image.clip_composite_draw(boy.left, boy.bottom, 80, 75, boy.radian, '', boy.x, boy.y, 120, 120)
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
        boy.left = 0
        boy.bottom = 0
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time)
        
        if int(boy.frame) == 12:
            boy.state_machine.handle_event(('FRAME_OUT', 0))
            pass

        if int(boy.frame) < 8:
            boy.left = int(boy.frame)* 81 + (81 * 10)
            boy.bottom = 151
        elif int(boy.frame) < 12:
            boy.left = int(boy.frame-8)* 81 + (81 * 13)
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

class Jump:

    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        boy.bottom = 75 * 2
        boy.left = 0
        boy.dir = 1
        boy.wait_time = get_time()
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        if int(boy.frame) < 9:
            boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time)

        if int(boy.frame) < 9:
            boy.left = int(boy.frame) * 80 + (82 * 10)
            boy.bottom = 75 * 2

        boy.y += JUMP_SPEED_PPS * game_framework.frame_time * boy.dir

        if get_time() - boy.wait_time > 0.35:
            boy.dir = -1

        # if int(boy.y) > 320:
        #     boy.dir = -1
        # if int(boy.y) < 200:
        #     boy.dir = 0
        #     boy.y = 200
        if int(boy.y) <= 200:
            boy.dir = 0
            boy.state_machine.handle_event(("METER_OUT", 0))

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.left, boy.bottom, 80, 75, boy.x, boy.y, 120, 120)

class StateMachine:
    def __init__(self, boy):
        self.boy = boy
        self.cur_state = Start
        self.transitions = {
            Start: {meter_out: Run},
            Ride: {frame_out: Idle},
            Idle: {a_down: UpSpeed, space_down: Jump},
            UpSpeed: {frame_out: Idle, a_up: Idle},
            Run: {time_out: Ride},
            Jump: {meter_out: Idle},
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
        self.x, self.y = 50, 200
        self.x1, self.y1, self.x2, self.y2 = 25, 50, 30, 50
        self.frame = 0
        self.action = 0
        self.left = 0
        self.bottom = 0
        self.dir = 0
        self.image = load_image('skater_sprite_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()
        pass

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))
        pass

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x - self.x1, self.y - self.y1, self.x + self.x2, self.y + self.y2  # 튜플
