from pico2d import *

class Background:
    def __init__(self):
        self.x = 400
        self.y = 90
        self.image = load_image('background.png')

    def get_bb(self):
        return self.x - 40, self.y - 40, self.x + 40, self.y + 40

    def update(self):
        pass

    def draw(self):
        self.image.draw (800 // 2, 640 // 2)
        draw_rectangle(*self.get_bb())

