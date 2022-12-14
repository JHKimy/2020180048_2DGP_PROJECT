from pico2d import *
import play_state
import play_state2

class Flag:
    def __init__(self,x,y):
        self.image = load_image('flag.png')
        self.ox = x
        self.oy = y

    def update(self):
        if play_state.char.x > 400 and play_state.char.dir == 1:
            self.ox -= play_state.char.dx
        elif play_state.char.x > 400 and play_state.char.dir < 0:
            self.ox += play_state.char.dx

        if play_state.stage == 2:
            if play_state2.char.x > 400 and play_state2.char.dir == 1:
                self.ox -= play_state2.char.dx
            elif play_state2.char.x > 400 and play_state2.char.dir < 0:
                self.ox += play_state2.char.dx

    def draw(self):
        self.image.draw(self.ox, self.oy)
        if play_state.cb == 1 or play_state2.cb == 1:
            draw_rectangle(*self.get_bb())

    def get_bb(self):  # 충동처리 사각형 범위
        return self.ox - 23, self.oy - 50, self.ox + 23, self.oy + 50