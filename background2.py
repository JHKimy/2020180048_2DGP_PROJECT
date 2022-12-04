from pico2d import *
import game_framework
import play_state2
import finish_image

class Background:
    def __init__(self):
        self.image = load_image('background2.png')
        self.canvas_width = get_canvas_width()

        self.width = 6000
        self.height = 640

        self.x = 5000//2
        self.y = 640//2
        self.bgm = load_music('background_music2.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()


    def update(self):
        if self.x >= -3000:     # 맵의 x가 -700이 되면 맵 이동 멈춤
            if play_state2.char.x > 400 and play_state2.char.dir > 0:
                self.x -= play_state2.char.dx     # 캐릭터의 이동힘값을 계속 뺴줌 == 맵이 왼쪽으로 이동

            elif play_state2.char.dir < 0:
                self.x += play_state2.char.dx


        if self.x == -2500:  # 맵에 캐릭터 dx값 계속 들어가서 -700되면 게임 끝
            delay(1)
            game_framework.change_state(finish_image)




    def draw(self):
        #self.image.clip_draw_to_origin(self.window_left, 0, 800, 640, 0, 0)
        #self.image.draw(800//2, 640//2)
        self.image.draw(self.x, self.y, self.width, self.height)