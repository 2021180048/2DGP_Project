from pico2d import *

import game_framework
import game_world
import title_mode
from boy import Boy


# Game object class here

def init():
    global boy

    running = True

    boy = Boy()
    game_world.add_object(boy, 1)


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


def pause():
    # boy.wait_time = 1000000000000000000000000000000000.0
    pass

def resume():
    # boy.wait_time = get_time()
    pass

