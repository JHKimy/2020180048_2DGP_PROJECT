from pico2d import *
import game_framework
import start_image

from mario import Mario
from background import Background
from mushroom import Mushroom


background = None
mario = None
mushroom = None

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

        if char.x < 30:
            char.dirX = 0
            if char.state == 1:
                char.dirX += 1


        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(start_image)


# 초기화
def enter():
    global char, back, running, enemy
    char = Mario()
    enemy = Mushroom()
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

def pause():
    pass

def resume():
    pass




def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
