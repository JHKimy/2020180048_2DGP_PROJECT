from pico2d import *

class Mario:
    def __init__(self):
        self.x, self.y = 30, 90
        self.frame = 0
        self.image = load_image('mario2.png')
        self.state = 3
        self.dirX = 0
        self.dirY = 0
        self.jump = 0


    def update(self):
        self.frame = (self.frame + 1) % 3
        self.x += self.dirX * 5

        if self.jump == 1:
            self.y += 7
            if self.y >= 270:
                self.jump = -1


        elif self.jump == -1:
            self.y -= 6
            if self.y <= 250:
                if self.state == 4:
                    self.state = 6
                elif self.state == 5:
                    self.state = 7
            if self.y <= 90:
                self.jump = 0
                if self.state == 6:
                    self.state = 2
                elif self.state == 7:
                    self.state = 3

        else:
            self.y = 90

    def draw(self):

        if self.state == 0 or self.state == 1:
            self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(100, self.state * 100, 100, 100, self.x, self.y)