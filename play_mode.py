from header import *
from boy import Boy
from back_ground import Back_ground
from rail import Rail
import game_world
import game_framework
import title_mode

def init():
    global boy
    global back_ground
    running = True

    boy = Boy()
    game_world.add_object(boy, 2)

    back_ground = Back_ground()
    game_world.add_object(back_ground, 0)

    rail = Rail()
    game_world.add_object(rail,1)

    

def finish():
    game_world.clear()
    pass

def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        else:
            boy.handle_event(event)
            back_ground.handle_event(event)

def pause():
    pass

def resume():
    pass

