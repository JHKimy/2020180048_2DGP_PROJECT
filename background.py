from pico2d import *
import game_world
import game_framework
from mario import Mario
import play_state

class Background:
    def __init__(self):
        self.image = load_image('background.png')
        self.canvas_width = get_canvas_width()
        self.window_left = 0

    def update(self):
        self.window_left = clamp(0, int(play_state.char.x) - self.canvas_width // 2, 3000 - self.canvas_width)
        pass

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, 0, 800, 640, 0, 0)
        #self.image.draw(800//2, 640//2)