from pico2d import *
import game_world
import game_framework
import mario
import play_state
import start_image
import finish_image

class Background:
    def __init__(self):
        self.image = load_image('background.png')
        self.canvas_width = get_canvas_width()

        self.width = 4000
        self.height = 640

        self.x = 3000//2
        self.y = 640//2



        #self.window_left = 0

    def update(self):
        # if  self.x >= 0:
        #     self.x = 0

        if self.x >= -700:     # 맵의 x가 -700이 되면 맵 이동 멈춤
            if play_state.char.x > 400 and play_state.char.dir > 0:
                self.x -= play_state.char.dx     # 캐릭터의 이동힘값을 계속 뺴줌 == 맵이 왼쪽으로 이동

            elif play_state.char.dir < 0:
                self.x += play_state.char.dx


        clamp(0,self.x,3000//2) # 맵 한정값

        # if self.x < -700:
        #     play_state.char.x += 4

        if self.x == -700:  # 맵에 캐릭터 dx값 계속 들어가서 -700되면 게임 끝
            delay(1)
            game_framework.change_state(finish_image)



            # play_state.char.frame = (play_state.char.frame+1) % 3
            # play_state.char.state = 3
            # play_state.char.image.clip_draw(self.frame, self.state * 100, 100, 100, self.x, self.y)







        # self.x = - play_state.char.x
        # if play_state.char.x > 700:
        #     self.x = - play_state.char.x


        #self.window_left = clamp(0, int(play_state.char.x) - self.canvas_width // 2, 3000 - self.canvas_width)


    def draw(self):
        #self.image.clip_draw_to_origin(self.window_left, 0, 800, 640, 0, 0)
        #self.image.draw(800//2, 640//2)
        self.image.draw(self.x, self.y, self.width, self.height)