from header import *
import game_framework
import play_mode
import title_mode

def init():
    global image
    global image_2
    global running

    running = True
    image = load_image('about.png')
    image_2=load_image('white.png')
    pass


def finish():
    pass


def update():
    pass


def draw():
    clear_canvas()
    image_2.draw(800, 300)
    image.draw(800, 300)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_RETURN:
            game_framework.change_mode(play_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)

    pass
