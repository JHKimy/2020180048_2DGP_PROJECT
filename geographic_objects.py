from pico2d import *
import game_world
import game_framework
import play_state
from mario import Mario


class Brick:
    def __init__(self,x,y):
        self.image = load_image('brick.png')
        self.ox = x
        self.oy = y

    def update(self):
        if play_state.char.x > 400 and play_state.char.dir == 1:
            self.ox -= play_state.char.dx
        elif play_state.char.x > 400 and play_state.char.dir < 0:
            self.ox += play_state.char.dx

    def draw(self):
        self.image.draw(self.ox, self.oy)
        if play_state.cb == 1 :
            draw_rectangle(*self.get_bb())

    def get_bb(self):  # 충동처리 사각형 범위
        return self.ox - 23, self.oy - 23, self.ox + 23, self.oy + 23


class Bricks3:
    def __init__(self,x,y):
        self.image = load_image('3bricks.png')
        self.ox = x
        self.oy = y

    def update(self):
        if play_state.char.x > 400 and play_state.char.dir == 1:
            self.ox -= play_state.char.dx
        elif play_state.char.x > 400 and play_state.char.dir < 0:
            self.ox += play_state.char.dx

    def draw(self):
        self.image.draw(self.ox, self.oy)
        if play_state.cb == 1:
            draw_rectangle(*self.get_bb())

    def get_bb(self):  # 충동처리 사각형 범위
        return self.ox - 80, self.oy - 23, self.ox + 80, self.oy + 23





class Chimney:
    def __init__(self,x,y):
        self.image = load_image('chimney.png')
        self.ox = x
        self.oy = y

    def update(self):
        if play_state.char.x > 400 and play_state.char.dir == 1:
            self.ox -= play_state.char.dx
        elif play_state.char.x > 400 and play_state.char.dir < 0:
            self.ox += play_state.char.dx

    def draw(self):
        self.image.draw(self.ox, self.oy)
        if play_state.cb == 1:
            draw_rectangle(*self.get_bb())

    def get_bb(self):  # 충동처리 사각형 범위
        return self.ox - 45, self.oy - 50, self.ox + 45, self.oy + 50