from pico2d import *
import game_framework
import start_image
import random


class Background:
    def __init__(self):
        self.image = load_image('background.png')

    def draw(self):
        self.image.draw(800 // 2, 640 // 2)


class Mario:
    def __init__(self):
        self.x, self.y = 30, 90
        self.frame = 0
        self.image = load_image('mario2.png')
        self.state = 3
        self.dirX = 0
        self.dirY = 0
        self.jump = 0


    def update(self):
        self.frame = (self.frame + 1) % 3
        self.x += self.dirX * 5

        if self.jump == 1:
            self.y += 7
            if self.y >= 270:
                self.jump = -1


        elif self.jump == -1:
            self.y -= 6
            if self.y <= 250:
                if char.state == 4:
                    char.state = 6
                elif char.state == 5:
                    char.state = 7
            if self.y <= 90:
                self.jump = 0
                if self.state == 6:
                    self.state = 2
                elif self.state == 7:
                    self.state = 3

        else:
            self.y = 90

    def draw(self):

        if self.state == 0 or self.state == 1:
            self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(100, self.state * 100, 100, 100, self.x, self.y)



class monster1:
    def __init__(self):
        self.x = 500
        self.y = 80
        self.frame = 0
        self.image = load_image('monster1.png')
        self.state = 0
        self.dirX = 2
        self.dirY = 0

    def update(self):
        # self.frame = (self.frame + 1) % 3
        self.x -= self.dirX * 1
        if self.x < 300:
            self.x = 300
            self.dirX = -2
        elif self.x > 500:
            self.x = 500
            self.dirX = 2

    def draw(self):
        self.image.clip_draw(0 , 0, 48, 58, self.x, self.y)





def handle_events():
    global running
    global dirX
    global dirY
    global state
    events = get_events()

    for event in events:

        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                char.dirX += 1
                char.state = 1
            elif event.key == SDLK_LEFT:
                char.dirX -= 1
                char.state = 0
            elif event.key == SDLK_z:
                if char.jump == 0:
                    char.jump = 1
                    if char.state == 0 or char.state == 2:
                        char.state = 4
                    elif char.state == 1 or char.state == 3:
                        char.state = 5

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                char.dirX -= 1
                char.state = 3
            elif event.key == SDLK_LEFT:
                char.dirX += 1
                char.state = 2
            # elif event.key == SDLK_z:
            #     if char.state == 4:
            #         char.state = 6
            #     elif char.state == 5:
            #         char.state = 7

        if char.x < 30:
            char.dirX = 0
            if char.state == 1:
                char.dirX += 1


        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(start_image)


def enter():
    global char, back, running, enemy
    char = Mario()
    enemy = monster1()
    back = Background()
    running = True


def exit():
    global char, back, enemy
    del char
    del enemy
    del back


def update():
    char.update()
    enemy.update()


def draw():
    clear_canvas()
    back.draw()
    char.draw()
    enemy.draw()
    update_canvas()
    delay(0.01)

    # def handle_events(self):
    #     self.running
    #     self.dirX
    #     self.dirY
    #     self.state
    #     self.events = get_events()
    #
    #     for event in self.events:
    #         if event.type == SDL_QUIT:
    #             self.running = False
    #         elif event.type == SDL_KEYDOWN:
    #             if event.key == SDLK_RIGHT:
    #                 self.dirX += 1
    #                 self.state = 1
    #             elif event.key == SDLK_LEFT:
    #                 self.dirX -= 1
    #                 self.state = 0
    #
    #             elif event.key == SDLK_ESCAPE:
    #                 self.running = False
    #
    #         elif event.type == SDL_KEYUP:
    #             if event.key == SDLK_RIGHT:
    #                 self.dirX -= 1
    #                 self.state = 3
    #             elif event.key == SDLK_LEFT:
    #                 self.dirX += 1
    #                 self.state = 2

    # handle_events()
    # delay(0.01)

# open_canvas(800, 640)
#
# char = Mario()
# back = Background()
# char.running = True
#
# while char.running:
#     clear_canvas()
#     back.draw()
#     char.draw()
#     update_canvas()
#     char.handle_events()
#     char.update()
#     delay(0.01)
#
# close_canvas()
