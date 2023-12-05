from header import *
from boy import Boy
from back_ground import *
from rail import *
from landing import Landing
import game_world
import game_framework
import title_mode


def init():
    global boy
    global back_ground
    global landing

    boy = Boy()
    game_world.add_object(boy, 2)

    back_ground = Back_ground()
    game_world.add_object(back_ground, 1)

    city_0 = City_0()
    game_world.add_object(city_0, 0)

    star = Star()
    game_world.add_object(star, 0)

    moon = Moon()
    game_world.add_object(moon, 0)

    city_1 = City_1()
    game_world.add_object(city_1, 0)

    city_2 = City_2()
    game_world.add_object(city_2, 0)    

    goal = Goal()
    game_world.add_object(goal, 0)

    landing = Landing()
    game_world.add_object(landing, 0)

    rail_0 = Rail_0()
    game_world.add_object(rail_0, 1)

    stone_rail_0 = Stone_Rail_0()
    game_world.add_object(stone_rail_0, 1)

    round_rail_0 = Round_Rail_0()
    game_world.add_object(round_rail_0, 1)

    game_world.add_collision_pair('boy:rail', boy, rail_0)
    
    game_world.add_collision_pair('boy:stone_rail', boy, stone_rail_0)

    game_world.add_collision_pair('boy:round_rail', boy, round_rail_0)

    game_world.add_collision_pair('boy:back_ground', boy, back_ground)

    game_world.add_collision_pair('boy:landing', boy, landing)

    game_world.add_collision_pair('boy:goal', boy, goal)

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
        elif event.type == SDL_KEYDOWN and (event.key == SDLK_ESCAPE):
            close_canvas()
            open_canvas(1600,600)
            game_framework.change_mode(title_mode)
        else:
            boy.handle_event(event)
def pause():
    pass

def resume():
    pass

