from header import*
import game_framework
import play_mode

def init():
    global image
    image = load_image('Title_Screen.png')
    pass


def finish():
    pass


def update():
    pass


def draw():
    clear_canvas()
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
