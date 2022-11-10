from pico2d import *
import background
import collide_check
import game_world
import game_framework

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


frame_num = 4


#1 이벤트 정의
RD, LD, RU, LU, Z, ZU, TIMER = range(7)
event_name = ['RD', 'LD', 'RU', 'LU', 'Z', 'ZU','TIMER']

key_event_table = {

    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYDOWN, SDLK_z)    :  Z,
    (SDL_KEYUP, SDLK_RIGHT)  : RU,
    (SDL_KEYUP, SDLK_LEFT)   : LU,
    (SDL_KEYUP, SDLK_z)      : ZU

}

#2 : 상태의 정의
class IDLE:
    @staticmethod
    def enter(self,event):
        self.dir = 0
        self.timer = 1000

    def exit(self, event):
        # if event == C:
        #     self.fire_ball()
        pass

    def do(self):
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(1 * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(0 * 100, 200, 100, 100, self.x, self.y)


PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir = 1
        elif event == LD:
            self.dir = -1
        elif event == RU:
            self.dir = 1
        elif event == LU:
            self.dir = -1

    def exit(self, event):
        self.face_dir = self.dir
        # if event == SPACE:
        #     self.fire_ball()

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % frame_num
        self.frame = (self.frame + 1) % frame_num
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 800)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(int(self.frame)*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(int(self.frame)*100, 100, 100, 100, self.x, self.y)

class ZUMP:
    def enter(self, event):
        if self.isjump == False:
            self.isjump = True
            if event == Z:
                if self.jump == 0:
                    self.jump = 1

        # if event == Z:
        #     if self.jump == 0:
        #         self.jump = 1
        # elif event == ZU:
        #     self.jump = 0
    def exit(self, event):
        # self.face_dir = self.dir
        pass

    def do(self):
        # if self.jump == 1:
        # self.y += (self.mass * self.velocity * self.velocity) / 0.01
        if self.jump == 1:
            if self.face_dir == 1:
                self.state = 5
            if self.face_dir == -1:
                self.state = 4
            # self.y += 7
            self.y += (self.mass * self.velocity * self.velocity) * 0.01

            # if self.y >= 270:
            #     self.jump = -1
            if self.velocity < 0:
                self.jump = -1

        elif self.jump == -1:
            # self.y -= 6
            self.y -= (self.mass * self.velocity * self.velocity) * 0.01

            if self.y <= 250:

                if self.face_dir == 1:
                    self.state = 7
                elif self.face_dir == -1:
                    self.state = 6
            if self.y <= 90:
                self.jump = 0
                self.isjump = False
                self.y = 90
                self.velocity = 20

        else:
             self.y = 90

        self.frame = (self.frame + 1) % 1

        self.x = clamp(0, self.x, 1600)

        self.velocity -= 1

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, self.state*100, 100, 100, self.x, self.y)



next_state = {
    IDLE:  {RU: IDLE,  LU: IDLE,  RD: RUN,  LD: RUN, Z: ZUMP, ZU: IDLE},
    RUN:   {RU: IDLE, LU: IDLE, RD: RUN, LD: RUN, Z: ZUMP, ZU: IDLE},
    ZUMP:   {RU: IDLE, LU: IDLE, RD: RUN, LD: RUN, Z: ZUMP, ZU: IDLE}
}




class Mario:
    def __init__(self):
        self.x, self.y = 30, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.jump = 0
        self.state = 0
        self.image = load_image('mario2.png')

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self,None)

        self.jump = 0
        self.isjump = False

        self.mass = 7
        self.velocity = 20

    def get_bb(self):
        return self.x - 10, self.y - 40, self.x + 20, self.y + 20

    def update(self):

        self.cur_state.do(self)

        if self.isjump == True:
            pass

        elif self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self,event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
            self.cur_state.enter(self, event)

        if(collide_check.collide(self,background.Background())):
            self.y = 170

    def draw(self):
        self.cur_state.draw(self)
#        self.font.draw(self.x - 60, self.y + 50, f'(Time: {get_time():.2f})', (255, 255, 0))

    #draw_rectangle(*self.get_bb())

    def add_event(self, event):
        self.event_que.insert(0,event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

