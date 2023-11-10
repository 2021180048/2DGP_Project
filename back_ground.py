from boy import *

class Start:
    @staticmethod
    def enter(boy, e):
        boy.frame = 0
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
            boy.bottom = 780
        else:
            boy.state_machine.handle_event(('METER_OUT', 0))
        pass

    @staticmethod
    def draw(boy):
        boy.image.clip_draw(boy.left, boy.bottom, 80, 80, boy.x, boy.y, 120, 120)
        pass


class StateMachine:
    def __init__(self, back_ground):
        self.back_ground = back_ground
        self.cur_state = Start
        self.transitions = {
            Start{}
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
        self.x = 800//2
        self.y = 600//2
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        
        if Back_ground.image == None:
            self.image = load_image('back_ground.jpg')
    
    def handle_event(self, e):
        pass

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y, 1600, 600)
        pass
