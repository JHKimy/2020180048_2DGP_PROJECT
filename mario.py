from pico2d import *
import game_world
import game_framework
from fireball import Fireball
import collide_check

class Mario:
    def __init__(self):
        self.x, self.y = 30, 90
        self.gy = 90  # 점프 할때 땅값
        self.frame = 0
        self.image = load_image('mario2.png')
        self.attack_image_l = load_image('attack1.png')
        self.attack_image_r = load_image('attack2.png')
        self.state = 3
        self.dir = 0
        self.dx = 4
        self.face_dir = 1
        self.jump = 0
        self.jumpval = 0
        self.attack = 0
        self.item_mario = 0
        #self.mass = 7
        #self.velocity = 20


    def update(self):
        self.frame = (self.frame + 1) % 3

        if self.state == 2 or self.state == 3:
            self.dx = 0
        else :
            self.dx = 4

        if self.x < 400:
            self.x += self.dir * self.dx

        if self.jump == 1:
            self.y += 7
            self.jumpval += 7
            if self.jumpval > 200:
                self.jumpval = 200
                self.jump = -1
            #self.y += (self.mass * self.velocity * self.velocity) * 0.01
            # if self.velocity <= 0:
            #     self.jump = -1


        elif self.jump == -1:
            #self.y -= (self.mass * self.velocity * self.velocity) * 0.01
            self.y -= 6
            self.jumpval -= 6
            if self.jumpval < 160:
                if self.state == 4:
                    self.state = 6
                elif self.state == 5:
                    self.state = 7

            if self.y < 90:
                self.jump = 0
                self.y = 90
                self.jumpval = 0
                #self.velocity = 20

                if self.state == 6:
                    self.state = 2
                    if self.dir == -1:
                        self.state = 0

                elif self.state == 7:
                    self.state = 3
                    if self.dir == 1:
                        self.state = 1


        elif self.y < 90:
            self.y = 90



        #self.velocity -= 0.5


    def draw(self):

        if self.state == 0 or self.state == 1 :
            self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

        elif self.attack == 1:
            if self.face_dir == -1:
                self.attack_image_l.draw(self.x, self.y)
            elif self.face_dir == 1:
                self.attack_image_r.draw(self.x, self.y)

        else:
            self.image.clip_draw(100, self.state * 100, 100, 100, self.x, self.y)
        
        draw_rectangle(*self.get_bb()) # 충돌처리 사각형 그리기

    def fire_ball(self):
        fireball = Fireball(self.x, self.y, self.face_dir * 5)
        if self.item_mario == 1 :
            game_world.add_object(fireball, 0)


    def get_bb(self):    # 충동처리 사각형 범위
        return self.x - 12, self.y - 35, self.x + 27, self.y + 30