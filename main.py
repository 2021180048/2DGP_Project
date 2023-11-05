from pico2d import  open_canvas, delay, close_canvas
# import play_mode as start_mode
import play_mode as start_mode
import game_framework

open_canvas()
game_framework.run(start_mode)
close_canvas()