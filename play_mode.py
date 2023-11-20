from header import *
from boy import Boy
from back_ground import Back_ground
from rail import Rail
from landing import Landing
import game_world
import game_framework
import title_mode


def init():
    global boy
    global back_ground
    global rail
    global landing
    running = True

    boy = Boy()
    game_world.add_object(boy, 2)

    back_ground = Back_ground()
    game_world.add_object(back_ground, 0)

    landing = Landing()
    game_world.add_object(landing, 0)

    rail = Rail()
    game_world.add_object(rail, 1)

    game_world.add_collision_pair('boy:rail', boy, rail)

    game_world.add_collision_pair('boy:back_ground', boy, back_ground)

    game_world.add_collision_pair('boy:landing', boy, landing)

    game_world.add_collision_pair('back_ground:rail', back_ground, rail)

def finish():
    game_world.clear()
    pass

def update():
    game_world.update()
    game_world.handle_collisions()

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
            boy.decide_landing(event)
def pause():
    pass

def resume():
    pass

