from header import *
import game_framework
import game_world
import play_mode
from back_ground import Back_ground
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8
FRAMES_PER_TIME = ACTION_PER_TIME * FRAMES_PER_ACTION

DEGREE_PER_TIME = 500

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

def down_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN

def down_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_DOWN

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def space_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_SPACE

def a_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a

def a_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a

def s_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_s

def s_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_s

def d_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d

def d_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d

def time_out(e):
    return e[0] == 'TIME_OUT'

def meter_out(e):
    return e[0] == 'METER_OUT'

def frame_out(e):
    return e[0] == 'FRAME_OUT'

def falling(e):
    return e[0] == 'FALLING'

def bad_finish(e):
    return e[0] == 'BAD_FINISH'

def good_finish(e):
    return e[0] == 'GOOD_FINISH'

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
        boy.wait_time = get_time()
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time) % 12
        boy.left = int(boy.frame) * 81 + 80
        boy.bottom = 75 * 5

        if get_time() - boy.wait_time > 0.7 and game_world.objects[0][0].speed < 10:
            game_world.objects[0][0].speed += 1
            game_world.objects[1][0].speed += 1
            boy.wait_time += (get_time() - boy.wait_time)
           


    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.left, boy.bottom, 80, 80, boy.x, boy.y, 120, 120)
        pass

class Idle:

    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        boy.radian = 0
        boy.rail_collision = 1
        boy.back_ground_collision = 1
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        if boy.back_ground_collision != 1 and boy.rail_collision != 1:
            boy.state_machine.handle_event(('FALLING', 0))
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
        boy.image.clip_composite_draw(boy.left, boy.bottom, 80, 75, boy.radian, '', boy.x, boy.y, 120, 120)
        pass

class Run:

    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        game_world.objects[0][0].speed += 1
        game_world.objects[1][0].speed += 1
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
        if get_time() - boy.wait_time > 2.0:
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

class Jump:

    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        boy.back_ground_collision = 0
        boy.rail_collision = 0
        boy.landing_collision = 0
        boy.seed_y = boy.y
        boy.ok = True
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time)

        if int(boy.frame) < 9:
            boy.left = int(boy.frame) * 80 + (82 * 10)
            boy.bottom = 75 * 2

        if boy.y - boy.seed_y >= 150:
            boy.state_machine.handle_event(('FALLING', 0))
        else:
            boy.y += JUMP_SPEED_PPS * game_framework.frame_time
            boy.rail_collision = 0
            boy.landing_collision = 0
            boy.back_ground_collision = 0 #스페이스바 씺힘 때문
            pass

    @staticmethod
    def draw(boy):
        # boy.image.clip_draw(boy.left, boy.bottom, 80, 75, boy.x, boy.y, 120, 120)
        boy.image.clip_composite_draw(boy.left, boy.bottom, 80, 75, boy.radian, '', boy.x, boy.y, 120, 120)

class Falling:
    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        boy.wait_time = get_time()
        boy.land = 0
        boy.ok = True
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time)
        boy.dicide_landing()
        boy.gravity()

        if int(boy.frame) < 7:
            boy.left = int(boy.frame) * 81 + (81 * 13)
            boy.bottom = 75 * 2
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.left, boy.bottom, 80, 80, boy.x, boy.y, 120, 120)
        pass

class Railing:
    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        boy.rail_collision = 0
        boy.back_ground_collision = 0
        boy.radian = 0
        game_world.objects[0][0].buffer += 10
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time)

        if boy.rail_collision == 0 and boy.back_ground_collision == 0:
            boy.gravity()

        if boy.rail_collision == 1:
            if int(boy.frame) % 2 == 0:
                boy.radian = 3.141592/180 * 1
            else:
                boy.radian = 3.141592/180 * 0

        if boy.back_ground_collision == 1:
            boy.state_machine.handle_event(('BAD_FINISH', 0))

        if int(boy.frame) < 2:
            boy.left = int(boy.frame) * 81 + (81 * 0)
            boy.bottom = 75 * 3
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_composite_draw(boy.left, boy.bottom, 80, 80, boy.radian, '', boy.x, boy.y, 120, 120)
        pass

class Bad_Finish:
    @staticmethod
    def enter(boy, e):
        boy.degree = 0
        boy.frame = 0
        boy.rail_collision = 0
        boy.back_ground_collision = 0
        boy.wait_time = get_time()
        game_world.objects[0][0].buffer = 0
        if(game_world.objects[0][0].speed > 1):
            game_world.objects[0][0].speed -= 1
            game_world.objects[1][0].speed -= 1
        
        if(game_world.objects[0][0].score >= 10):
            game_world.objects[0][0].score -= 10
        else:
            game_world.objects[0][0].score = 0
        pass

    @staticmethod
    def exit(boy, e):
        boy.bad = 0
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time)

        if get_time() - boy.wait_time > 0.7:
            boy.state_machine.handle_event(('TIME_OUT', 0))

        if int(boy.frame) < 5:
            boy.left = 0 * 81
            boy.bottom = 79 * 11
        elif 5 <= int(boy.frame):
            boy.left = 0 * 81
            boy.bottom = 79 * 12

        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.left, boy.bottom, 80, 80, boy.x, boy.y, 120, 120)
        pass

class Good_Finish:

    @staticmethod
    def enter(boy, e):
        boy.degree = 0
        boy.frame = 0
        boy.rail_collision = 0
        boy.back_ground_collision = 0
        boy.radian = 0
        boy.wait_time = get_time()
        game_world.objects[0][0].score += game_world.objects[0][0].buffer
        game_world.objects[0][0].buffer = 0
        pass

    @staticmethod
    def exit(boy, e):
        boy.good = 0
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time)

        if get_time() - boy.wait_time > 0.35:
            boy.state_machine.handle_event(('TIME_OUT', 0))

        if int(boy.frame) < 4:
            boy.left = int(boy.frame) * 93 + (93 * 13)
            boy.bottom = 0
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.left, boy.bottom, 80, 80, boy.x, boy.y, 120, 120)
        pass

class Hard_Flip:

    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        boy.flag = False
        boy.ok = True
        boy.land = 0
        game_world.objects[0][0].buffer += 30
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time * 0.8)

        if int(boy.frame) < 10:
            boy.left = int(boy.frame) * 100 + (100 * 3)
            boy.bottom = 0
        pass

        if boy.flag == True:
            boy.gravity()
        else:
            boy.y += JUMP_SPEED_PPS * game_framework.frame_time

        if boy.y-boy.seed_y >= 150:
            boy.flag = True

        boy.dicide_landing()

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.left, boy.bottom, 80, 80, boy.x, boy.y, 120, 120)
        pass

class Flip:

    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        boy.flag = False
        boy.ok = True
        boy.land = 0
        game_world.objects[0][0].buffer += 20
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time * 0.6)

        if int(boy.frame) < 8:
            boy.left = int(boy.frame) * 81 + (81 * 16)
            boy.bottom = 77 * 4
        pass

        if boy.flag == True:
            boy.gravity()
            pass

        if boy.flag == False:
            boy.y += JUMP_SPEED_PPS * game_framework.frame_time

        if boy.y-boy.seed_y >= 150:
            boy.flag = True

        boy.dicide_landing()

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.left, boy.bottom, 80, 70, boy.x, boy.y, 120, 120)
        pass

class Backside_180:

    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        boy.flag = False
        boy.ok = True
        boy.land = 0
        game_world.objects[0][0].buffer += 20
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time * 0.6)

        if int(boy.frame) < 8:
            boy.left = int(boy.frame) * 81 + (81 * 8)
            boy.bottom = 77 * 4
        pass

        if boy.flag == True:
            boy.gravity()
            pass

        if boy.flag == False:
            boy.y += JUMP_SPEED_PPS * game_framework.frame_time

        if boy.y-boy.seed_y >= 150:
            boy.flag = True

        boy.dicide_landing()

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.left, boy.bottom, 80, 70, boy.x, boy.y, 120, 120)
        pass

class Lie:

    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time)

        if int(boy.frame) < 7:
            boy.left = int(boy.frame) * 197
            boy.bottom = 77 * 8 + 2
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.left, boy.bottom, 80, 70, boy.x, boy.y, 120, 120)
        pass

class Lie_Up:

    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time)

        if int(boy.frame) < 7:
            boy.left = (6 - int(boy.frame)) * 197
            boy.bottom = 77 * 8 + 2
        else:
            boy.state_machine.handle_event(("FRAME_OUT",0))
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.left, boy.bottom, 80, 70, boy.x, boy.y, 120, 120)
        pass

class Fall:

    @staticmethod
    def enter(boy, e):
        game_world.objects[0][0].speed = 0
        game_world.objects[1][0].speed = 0
        boy.frame = 0
        boy.wait_time = get_time()
        game_world.objects[0][0].buffer = 0
        if(game_world.objects[0][0].score >= 50):
            game_world.objects[0][0].score -= 50
        else:
            game_world.objects[0][0].score = 0
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time)

        if int(boy.frame) < 14:
            boy.left = int(boy.frame) * 199
            boy.bottom = 77 * 6
        elif 14 <= int(boy.frame) <15:
            boy.left = (int(boy.frame)-14) * 197 + (80 * 2)
            boy.bottom = 77 * 3

        if get_time() - boy.wait_time > 2.0:
            boy.state_machine.handle_event(("TIME_OUT",0))
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.left, boy.bottom, 80, 70, boy.x, boy.y, 120, 120)
        pass

class Wake_Up:

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
        boy.frame = (boy.frame + FRAMES_PER_TIME * game_framework.frame_time * 0.3)

        if int(boy.frame) <4:
            boy.left = int(boy.frame) * 197 + (80 * 2)
            boy.bottom = 77 * 3
        if get_time() - boy.wait_time > 1.5:
            boy.state_machine.handle_event(("TIME_OUT",0))
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.left, boy.bottom, 80, 70, boy.x, boy.y, 120, 120)
        pass

class Rotation:

    @staticmethod
    def enter(boy, e):
        boy.degree = 0
        boy.flag = False
        boy.ok = True
        boy.land = 0
        game_world.objects[0][0].buffer += 40
        pass

    @staticmethod
    def exit(boy, e):
        pass

    @staticmethod
    def do(boy):
        boy.degree = (boy.degree + DEGREE_PER_TIME * game_framework.frame_time)

        if boy.degree < 360:
            boy.radian = (boy.degree * math.pi/180)
            boy.left = 95 * 2
            boy.bottom = 0
        pass
        if boy.flag == True:
            boy.gravity()
            pass

        if boy.flag == False:
            boy.y += JUMP_SPEED_PPS * game_framework.frame_time

        if boy.y-boy.seed_y >= 150:
            boy.flag = True

        boy.dicide_landing()


    @staticmethod
    def draw(boy):
        # boy.image.clip_draw(boy.left, boy.bottom, 80, 70, boy.x, boy.y, 120, 120)
        boy.image.clip_composite_draw(boy.left, boy.bottom, 80, 70, boy.radian, '', boy.x, boy.y, 110, 110)
        pass

class StateMachine:
    def __init__(self, boy):
        self.boy = boy
        self.cur_state = Idle
        self.transitions = {
            Start: {meter_out: Run},
            Ride: {frame_out: Idle},
            Idle: {right_down: UpSpeed, space_down: Jump, falling: Falling, down_down: Lie},
            UpSpeed: {frame_out: Idle, right_up: Idle},
            Run: {time_out: Ride},
            Jump: {meter_out: Idle, falling: Falling, d_down: Hard_Flip, a_down: Flip, s_down: Backside_180, left_down: Rotation},
            Falling: {meter_out: Idle, down_down: Railing, bad_finish: Bad_Finish, good_finish: Good_Finish},
            Railing: {down_up: Falling, space_down: Jump, bad_finish: Bad_Finish},
            Bad_Finish: {time_out: Idle},
            Good_Finish: {time_out: Idle},
            Hard_Flip: {good_finish: Good_Finish, bad_finish: Bad_Finish},
            Flip: {good_finish: Good_Finish, bad_finish: Bad_Finish},
            Backside_180: {good_finish: Good_Finish, bad_finish: Bad_Finish},
            Lie: {down_up: Lie_Up},
            Lie_Up: {frame_out: Idle},
            Fall: {time_out: Wake_Up},
            Wake_Up: {time_out: Run},
            Rotation: {good_finish: Good_Finish, bad_finish: Fall}
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
        self.x, self.y = 150, 200
        self.x1, self.y1, self.x2, self.y2 = 25, 50, 30, -40
        self.frame = 0
        self.left = 0
        self.bottom = 0
        self.dir = 0
        self.back_ground_collision = 0
        self.landing_collision = 0
        self.down_speed = 0
        self.event = None
        self.ok = False
        self.land = 0
        self.seed_y = 0
        self.degree = 0
        self.image = load_image('skater_sprite_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()
        pass

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))
        self.event = event
        pass

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x - self.x1, self.y - self.y1, self.x + self.x2, self.y + self.y2  # 튜플
    
    def handle_collision(self, group, other):
        if group == 'boy:rail':
            self.rail_collision = 1
            pass

        if group == 'boy:back_ground':
            self.back_ground_collision = 1
            pass

        if group == 'boy:landing':
            self.landing_collision = 1
            pass

    def handle_not_collision(self, group, other):
        if group == 'boy:rail':
            self.rail_collision = 0
            pass

        if group == 'boy:back_ground':
            self.back_ground_collision = 0
            pass

        if group == 'boy:landing':
            self.landing_collision = 0
            pass

    def gravity(self):
        self.y -= JUMP_SPEED_PPS * game_framework.frame_time * 0.8

    def dicide_landing(self):
        if self.back_ground_collision == 1:
            if self.land == 1:
                self.state_machine.handle_event(('GOOD_FINISH', 0))
            if self.land == 0:
                self.state_machine.handle_event(('BAD_FINISH', 0))

    
    def event_landing(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE and self.ok == True:
            if self.landing_collision == 1:
                self.land = 1
                pass
            if self.landing_collision == 0:
                self.land = 0
                pass
            self.ok = False