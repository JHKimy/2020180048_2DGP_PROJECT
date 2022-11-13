from pico2d import *
import game_framework
import start_image
import game_world

from mario import Mario
from mushroom import Mushroom
from background import Background

char = None
back = None
enemy = None




def handle_events():
    global running
    global dir
    global state
    events = get_events()

    for event in events:

        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                char.dir += 1
                char.state = 1
                char.face_dir = 1
            elif event.key == SDLK_LEFT:
                char.dir -= 1
                char.state = 0
                char.face_dir = -1

            elif event.key == SDLK_z:
                if char.jump == 0:
                    char.jump = 1
                    if char.face_dir == -1:
                        char.state = 4
                    elif char.face_dir==1:
                        char.state = 5

            elif event.key == SDLK_c:
                    char.attack = 1
                    char.fire_ball()

            # elif event.key == SDLK_c and SDLK_RIGHT :
            #     char.attack = 1
            #
            # elif event.key == SDLK_c and SDLK_RIGHT :
            #     char.attack = 1

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                char.dir -= 1
                char.state = 3
                char.face_dir = 1
            elif event.key == SDLK_LEFT:
                char.dir += 1
                char.state = 2
                char.face_dir = -1
            elif event.key == SDLK_c:
                char.attack = 0


        char.x = clamp(30, char.x, 2970)


        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(start_image)


def enter():
    global char, back, enemy
    char = Mario()
    enemy = Mushroom()
    back = Background()
    game_world.add_object(back, 0)
    game_world.add_object(char, 1)
    game_world.add_object(enemy, 2)


def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
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