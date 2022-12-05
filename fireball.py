from pico2d import *
import game_world
import play_state
import play_state2
import collide_check

class Fireball:
    image = None

    def __init__(self, x = 300, y = 300, velocity = 1):
        if self.image == None:
            self.image = load_image('fireball.png')
        self.x, self.y, self.velocity = x, y, velocity

        self.face_dir = play_state.char.face_dir

        #스테이지가 2로 넘어가면
        if play_state.stage == 2:
            self.face_dir = play_state2.char.face_dir############

        self.frame = 0
        self.state = 0

    def draw(self):
        if self.face_dir == -1:
            self.image.clip_draw(self.frame * 64, 0, 64, 64, self.x, self.y)
        elif self.face_dir == 1:
            self.image.clip_draw(self.frame * 64, 64, 64, 64, self.x, self.y)
        if play_state.cb == 1 or play_state2.cb == 1:
            draw_rectangle(*self.get_bb())
    def update(self):
        
        # 파이어볼이 적에게 닿으면 삭제, 적도 삭제하기위한 kk 변수에 1 대입
        if collide_check.collide(self, play_state.enemy1): 
            game_world.remove_object(self)
            play_state.kk = 1
        if collide_check.collide(self, play_state.enemy2):
            game_world.remove_object(self)
            play_state.kk = 2

        # 스테이지 2
        if play_state.stage == 2:
            if collide_check.collide(self, play_state2.enemy1):
                game_world.remove_object(self)
                play_state2.kk = 1

            if collide_check.collide(self, play_state2.enemy2):
                game_world.remove_object(self)
                play_state2.kk = 2

            if collide_check.collide(self, play_state2.enemy3):
                game_world.remove_object(self)
                play_state2.kk = 3

            if collide_check.collide(self, play_state2.enemy4):
                game_world.remove_object(self)
                play_state2.kk = 4



        self.x += self.velocity

        if play_state.stage == 1:
            if play_state.char.x > 400 and play_state.char.dir == 1:
                self.x -= play_state.char.dx
            elif play_state.char.x > 400 and play_state.char.dir < 0:
                self.x += play_state.char.dx

        if play_state.stage == 2:
            if play_state.char.x > 400 and play_state2.char.dir == 1:
                self.x -= play_state2.char.dx
            elif play_state.char.x > 400 and play_state2.char.dir < 0:
                self.x += play_state2.char.dx





        if self.x < 25 or self.x > 800 - 25:
            game_world.remove_object(self)

        self.frame = (self.frame + 1) % 5

    def get_bb(self):
        return self.x - 23, self.y - 10, self.x + 23, self.y + 10