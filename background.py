from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('background.png')

    def draw(self):
        self.image.draw (800 // 2, 640 // 2)