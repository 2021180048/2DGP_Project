from boy import *


def a_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a

def a_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a


class Start:
    @staticmethod
    def enter(back_ground, e):
        pass

    @staticmethod
    def exit(back_ground, e):
        pass

    @staticmethod
    def do(back_ground):
        back_ground.x -= RUN_SPEED_PPS * game_framework.frame_time
        if int(back_ground.x) <= -400:
            back_ground.x = 400
        pass

    @staticmethod
    def draw(back_ground):
        back_ground.image.draw(back_ground.x, back_ground.y, 800, 600)
        back_ground.image.draw(back_ground.x + 800, back_ground.y, 800, 600)
        pass


class Move:
    @staticmethod
    def enter(back_ground, e):
        pass

    @staticmethod
    def exit(back_ground, e):
        pass

    @staticmethod
    def do(back_ground):
        back_ground.x -= RUN_SPEED_PPS * game_framework.frame_time * 1.2
        if int(back_ground.x) <= -400:
            back_ground.x = 400

        pass

    @staticmethod
    def draw(back_ground):
        back_ground.image.draw(back_ground.x, back_ground.y, 800, 600)
        back_ground.image.draw(back_ground.x + 800, back_ground.y, 800, 600)

        pass


class StateMachine:
    def __init__(self, back_ground):
        self.back_ground = back_ground
        self.cur_state = Start
        self.transitions = {
            Start: {a_down: Move},
            Move: {a_up: Start},
        }

    def start(self):
        self.cur_state.enter(self.back_ground, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.back_ground)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.back_ground, e)
                self.cur_state = next_state
                self.cur_state.enter(self.back_ground, e)
                return True
        return False

    def draw(self):
        self.cur_state.draw(self.back_ground)


class Back_ground:
    
    image = None
    
    def __init__(self):
        self.x = 400
        self.y = 300
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        
        if Back_ground.image == None:
            self.image = load_image('back_ground.jpg')
    
    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))
        pass

    def update(self):
        self.state_machine.update()
        pass

    def draw(self):
        self.state_machine.draw()
        pass
