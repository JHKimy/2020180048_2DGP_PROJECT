from pico2d import *
import game_world
#from mario import Mario
import play_state

class Fireball:
    image = None

    def __init__(self, x = 300, y = 300, velocity = 1):
        if self.image == None:
            self.image = load_image('fireball.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.face_dir = play_state.char.face_dir
        self.frame = 0
        self.state = 0

    def draw(self):
        if self.face_dir == -1:
            self.image.clip_draw(self.frame * 64, 0, 64, 64, self.x, self.y)
        elif self.face_dir == 1:
            self.image.clip_draw(self.frame * 64, 64, 64, 64, self.x, self.y)

    def update(self):
        self.x += self.velocity
        if self.x < 25 or self.x > 2000 - 25:
            game_world.remove_object(self)

        self.frame = (self.frame + 1) % 5