from pico2d import *
import game_framework
import start_image
import game_world
import collide_check



from mario import Mario
from enemy import Mushroom
from background import Background

from geographic_objects import Brick
from geographic_objects import Chimney

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
                char.dir = 1
                char.state = 1
                char.face_dir = 1

            elif event.key == SDLK_LEFT:
                char.dir = -1
                char.state = 0
                char.face_dir = -1

            elif event.key == SDLK_z:
                if char.jump == 0:
                    char.jump = 1

                    if char.face_dir == -1:
                        char.state = 4

                    elif char.face_dir == 1:
                        char.state = 5

            elif event.key == SDLK_c:
                    char.attack = 1
                    char.fire_ball()

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
    global char, back, enemy1, brick1, brick2, brick3, chimney1, bricks

    back = Background()
    char = Mario()
    #enemy1 = Mushroom(500, 80)

    brick1 = Brick(400,180)
    brick2 = Brick(450,180)
    brick3 = Brick(500,180)
    brick4 = Brick(450,300)

    brick5 = Brick(500,200)
    brick6 = Brick(500,200)
    brick7 = Brick(500,200)
    brick8 = Brick(500,200)

    bricks = [brick1,brick2,brick3,brick4]


    chimney1 = Chimney(1000,115)


    game_world.add_object(back, 0)
    game_world.add_object(char, 1)
    #game_world.add_object(enemy1, 1)


    #game_world.add_object(brick1, 0)
    #game_world.add_object(brick2, 0)
    #game_world.add_object(brick3, 0)
    game_world.add_objects(bricks, 0)

    game_world.add_object(chimney1, 0)


def exit():
    game_world.clear()


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for bk in bricks:
        if collide_check.collide(char, bk):
            char.jump = 0
            char.jumpval = 0
            # if char.face_dir==1:
            #     char.state = 3
            # elif char.face_dir==-1:
            #     char.state = 2

        if char.y < bk.oy :
            if collide_check.collide(char, bk):
                char.jump = -1

        if collide_check.collide(char, bk):
            if char.x > bk.ox+25 :
                char.jump = -1
            # elif char.x < bk.ox-40:
            #     char.jump = -1





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