from pico2d import *
import game_world
import game_framework


class Mushroom:
    def __init__(self):
        self.x = 500
        self.y = 80
        self.frame = 0
        self.image = load_image('monster1.png')
        self.state = 0
        self.dir = 2

    def update(self):
        # self.frame = (self.frame + 1) % 3
        self.x -= self.dir * 1
        if self.x < 300:
            self.x = 300
            self.dir = -2
        elif self.x > 500:
            self.x = 500
            self.dir = 2


    def draw(self):
        self.image.clip_draw(0, 0, 48, 58, self.x, self.y)