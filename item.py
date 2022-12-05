from pico2d import *
import play_state
import collide_check
import play_state
from itemM import Item
import game_world


class Itembox:
    def __init__(self, x, y):
        self.image = load_image('itembox.png')
        self.image2 = load_image('used_itembox.png')
        self.ox = x
        self.oy = y
        self.tick_Itembox = 0
        self.item_limit = 0
        self.itembox_sound = load_wav('itembox.wav')
        self.itembox_sound.set_volume(80)

    def update(self):
        if play_state.char.x > 400 and play_state.char.dir == 1:
            self.ox -= play_state.char.dx
        elif play_state.char.x > 400 and play_state.char.dir < 0:
            self.ox += play_state.char.dx


    def draw(self):
        if self.tick_Itembox == 1 or self.tick_Itembox == -1:
            self.image2.draw(self.ox, self.oy)
        else:
            self.image.draw(self.ox, self.oy)
        if play_state.cb == 1:
            draw_rectangle(*self.get_bb())

    # 충동처리 사각형 범위
    def get_bb(self):
        return self.ox - 23, self.oy - 23, self.ox + 23, self.oy + 23

    def item(self):
        item = Item(self.ox, self.oy, 1)
        if self.item_limit == 0:
            game_world.add_object(item, 0)
            self.item_limit = 1

