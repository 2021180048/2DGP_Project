from header import*
import game_framework
import play_mode

def init():
    global image
    global image_2
    global image_3
    global image_4

    image = load_image('Title_Screen.png')
    image_2 = load_image('city_0.png')
    image_3 = load_image('city_1.png')
    image_4 = load_image('city_2.png')
    pass


def finish():
    pass


def update():
    pass


def draw():
    clear_canvas()
    image_2.draw(800, 300)
    image_3.draw(800, 300)
    image_4.draw(800, 300)
    image.draw(800, 300, 600, 600)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_mode(play_mode)
    pass
