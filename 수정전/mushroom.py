from pico2d import *

class Mushroom:
    def __init__(self):
        self.x = 500
        self.y = 80
        self.frame = 0
        self.image = load_image('monster1.png')
        self.state = 0
        self.dirX = 2
        self.dirY = 0

    def get_bb(self):
        return self.x - 10, self.y - 40, self.x + 20, self.y + 20
    def update(self):
        # self.frame = (self.frame + 1) % 3
        self.x -= self.dirX * 1
        if self.x < 300:
            self.x = 300
            self.dirX = -2
        elif self.x > 500:
            self.x = 500
            self.dirX = 2

    def draw(self):
        self.image.clip_draw(0, 0, 48, 58, self.x, self.y)
        draw_rectangle(*self.get_bb())