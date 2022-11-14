from pico2d import *
import game_world
import game_framework
import mario
import play_state

class Background:
    def __init__(self):
        self.image = load_image('background.png')
        self.canvas_width = get_canvas_width()

        self.width = 3000
        self.height = 640
        #
        self.x = 3000//2
        self.y = 640//2

        #self.window_left = 0

    def update(self):

        if self.x > -700:

            if play_state.char.x > 400 and play_state.char.dir > 0:
                self.x -= play_state.char.dx

            elif play_state.char.dir < 0:
                    self.x += play_state.char.dx


        if self.x < -700:
            play_state.char.x += 4







        # self.x = - play_state.char.x
        # if play_state.char.x > 700:
        #     self.x = - play_state.char.x


        #self.window_left = clamp(0, int(play_state.char.x) - self.canvas_width // 2, 3000 - self.canvas_width)


    def draw(self):
        #self.image.clip_draw_to_origin(self.window_left, 0, 800, 640, 0, 0)
        #self.image.draw(800//2, 640//2)
        self.image.draw(self.x, self.y, self.width, self.height)