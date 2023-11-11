from header import*
import game_framework

PIXEL_PER_METER = 100
RAIL_SPEED_KMPH = 2.0
RAIL_SPEED_MPM = RAIL_SPEED_KMPH * 1000.0 / 60.0
RAIL_SPEED_MPS = RAIL_SPEED_MPM / 60.0
RAIL_SPEED_PPS = RAIL_SPEED_MPS * PIXEL_PER_METER

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT

def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT

def a_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a

def a_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a

def time_out(e):
    return e[0] == 'TIME_OUT'

class Start:
    @staticmethod
    def enter(rail, e):
        rail.speed = 0
        rail.wait_time = get_time()
        pass

    @staticmethod
    def exit(rail, e):
        rail.speed = 0
        pass

    @staticmethod
    def do(rail):
        if get_time() - rail.wait_time > 2.5:
            rail.state_machine.handle_event(('TIME_OUT', 0))
        pass

    @staticmethod
    def draw(rail):
        rail.image.draw(rail.x, rail.y)
        pass

class Move:
    @staticmethod
    def enter(rail, e):       
        pass

    @staticmethod
    def exit(rail, e):
        pass

    @staticmethod
    def do(rail):
        rail.x -= RAIL_SPEED_PPS * game_framework.frame_time * rail.speed
        if int(rail.x) <= -200:
            rail.x = 1600            

        pass

    @staticmethod
    def draw(rail):
        rail.image.draw(rail.x, rail.y)
        pass


class Upspeed:
    @staticmethod
    def enter(rail, e):
        rail.wait_time = get_time()
        pass

    @staticmethod
    def exit(rail, e):
        pass

    @staticmethod
    def do(rail):
        rail.x -= RAIL_SPEED_PPS * game_framework.frame_time * rail.speed
        
        if get_time() - rail.wait_time > 0.5:
            rail.speed += 1.0
            rail.wait_time += get_time()
        pass

    @staticmethod
    def draw(rail):
        rail.image.draw(rail.x, rail.y)
        pass


class StateMachine:
    def __init__(self, rail):
        self.rail = rail
        self.cur_state = Move
        self.transitions = {
            Start: {time_out: Move},
            Move: {right_down: Upspeed},
            Upspeed: {right_up: Move},
        }

    def start(self):
        self.cur_state.enter(self.rail, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.rail)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.rail, e)
                self.cur_state = next_state
                self.cur_state.enter(self.rail, e)
                return True
        return False

    def draw(self):
        self.cur_state.draw(self.rail)

class Rail():

    def __init__(self):
        self.x = 1200
        self.y = 180
        self.speed = 0.0
        self.wait_time = 0.0        
        self.x1, self.y1, self.x2, self.y2 = 160, -10, 180, 20
        self.image = load_image('rail.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        pass

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))
        pass

    def update(self):
        self.state_machine.update()
        pass

    def draw(self):
        self.state_machine.draw()
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x - self.x1, self.y - self.y1, self.x + self.x2, self.y + self.y2  # 튜플
    
    def handle_collision(self, group, other):
        if group == 'boy:rail':
            pass

    def handle_not_collision(self, group, other):
        if group == 'boy:rail':
            pass

    
