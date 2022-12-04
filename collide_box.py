from pico2d import *
import play_state
import play_state2


class Collide_box:
    def __init__(self,x,y):
        self.image = load_image('collide_box.png')
        self.ox = x
        self.oy = y

    def update(self):
        if play_state.char.x > 400 and play_state.char.dir == 1:
            self.ox -= play_state.char.dx
        elif play_state.char.x > 400 and play_state.char.dir < 0:
            self.ox += play_state.char.dx

        if play_state.stage == 2 :
            if play_state2.char.x > 400 and play_state2.char.dir == 1:
                self.ox -= play_state2.char.dx
            elif play_state2.char.x > 400 and play_state2.char.dir < 0:
                self.ox += play_state2.char.dx

    def draw(self):
        self.image.draw(self.ox, self.oy)
        if play_state.cb == 1 or play_state2.cb == 1:
            draw_rectangle(*self.get_bb())

    def get_bb(self):  # 충동처리 사각형 범위
        return self.ox - 30, self.oy - 30, self.ox + 30, self.oy + 30


class Collide_box2:
    def __init__(self,x,y):
        self.image = load_image('collide_fall.png')
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
        return self.ox - 500, self.oy - 80, self.ox + 450, self.oy + 75



# 스테이지 2 땅 1
class Collide_box3:
    def __init__(self,x,y):
        self.image = load_image('collide_fall.png')
        self.ox = x
        self.oy = y

    def update(self):
        if play_state2.char.x > 400 and play_state2.char.dir == 1:
            self.ox -= play_state2.char.dx
        elif play_state2.char.x > 400 and play_state2.char.dir < 0:
            self.ox += play_state2.char.dx

    def draw(self):
        self.image.draw(self.ox, self.oy)
        if play_state.cb == 1 or play_state2.cb == 1:
            draw_rectangle(*self.get_bb())

    def get_bb(self):  # 충동처리 사각형 범위
        return self.ox - 300, self.oy - 300, self.ox + 347, self.oy + 210


class Collide_box4:
    def __init__(self,x,y):
        self.image = load_image('collide_fall.png')
        self.ox = x
        self.oy = y

    def update(self):
        if play_state2.char.x > 400 and play_state2.char.dir == 1:
            self.ox -= play_state2.char.dx
        elif play_state2.char.x > 400 and play_state2.char.dir < 0:
            self.ox += play_state2.char.dx

    def draw(self):
        self.image.draw(self.ox, self.oy)
        if play_state.cb == 1 or play_state2.cb == 1:
            draw_rectangle(*self.get_bb())

    def get_bb(self):  # 충동처리 사각형 범위
        return self.ox - 2000, self.oy - 80, self.ox + 4000, self.oy+10