from pico2d import *
import game_world
import play_state
from mario import Mario
import collide_check


# 버섯 아이템
class Item:
    image = None

    def __init__(self, x = 0, y = 0, velocity = 1):

        if self.image == None:
            self.image = load_image('item.png')
        self.x, self.y, self.velocity = x, y+25, velocity

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y += self.velocity
        if self.y > 225:
            self.velocity = 0

        if play_state.char.x > 400 and play_state.char.dir == 1:
            self.x -= play_state.char.dx
        elif play_state.char.x > 400 and play_state.char.dir < 0:
            self.x += play_state.char.dx

        #self.x -= play_state.char.dx
        if play_state.char.x < self.x:
            if play_state.char.x >= self.x - 10 and play_state.char.y >= self.y:
                game_world.remove_object(self)
                play_state.char.item_mario = 1

        elif play_state.char.x > self.x:
            if play_state.char.x <= self.x + 10 and play_state.char.y >= self.y:
                game_world.remove_object(self)
                play_state.char.item_mario = 1

        # if play_state.char.x >= self.x - 10 and play_state.char.y >= self.y :
        #     if play_state.char.x < self.x
        #     game_world.remove_object(self)


    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20