from pico2d import *
import game_world
import play_state


class Mushroom:
    def __init__(self , x , y):
        self.mx = x
        self.my = y
        self.frame = 0
        self.image = load_image('goomba.png')
        self.state = 0
        self.dir = 1
        self.mdx = 2
        self.moving_x = 0
        self.moving = 0
        #self.cx = self.mx - background.Background.window_left

    def update(self):
        self.frame = (self.frame+1) % 12


        if play_state.kk == 1:
            game_world.remove_object(self)
            self.mx = 7000

        self.mx += self.dir * self.mdx


        if play_state.char.x > 400 and play_state.char.dir == 1:
            self.mx -= play_state.char.dx
        elif play_state.char.x > 400 and play_state.char.dir < 0:
            self.mx += play_state.char.dx

    def draw(self):
        self.image.clip_draw(self.frame * 55, 0, 55, 55, self.mx, self.my)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.mx - 25, self.my - 25, self.mx + 25, self.my + 25



class Turtle:
    def __init__(self, x, y):
        self.mx = x
        self.my = y
        self.frame = 0
        self.image = load_image('turtle.png')
        self.state = 0
        self.dir = 1
        self.mdx = 2
        self.moving_x = 0
        self.moving = 0
            # self.cx = self.mx - background.Background.window_left

    def update(self):
        self.frame = (self.frame + 1) % 12

        if play_state.kk == 2:
            game_world.remove_object(self)
            self.mx = 7000

        self.mx += self.dir * self.mdx


        if play_state.char.x > 400 and play_state.char.dir == 1:
            self.mx -= play_state.char.dx
        elif play_state.char.x > 400 and play_state.char.dir < 0:
            self.mx += play_state.char.dx



    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 70, 0, 70, 70, self.mx, self.my)
        elif self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) * 70, 0, 70, 70, 0, 'h', self.mx, self.my,70,70)

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.mx - 25, self.my - 25, self.mx + 25, self.my + 25