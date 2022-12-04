from pico2d import *
import game_framework
import start_image
import game_world
import collide_check
import gameover_image
import finish_image
import play_state2



from mario import Mario
from enemy import Mushroom
from enemy import Turtle
from background import Background

from geographic_objects import Brick
from geographic_objects import Bricks3
from geographic_objects import Chimney

from item import Itembox
from flag import Flag
from collide_box import Collide_box
from collide_box import Collide_box2








char = None
back = None
enemy1 = None



#스테이지 정해주는 변수
stage = 1




# 콜리드 박스 확인하기위한 b키를 위한 변수
cb = 0

# 파이어볼이 없어짐에 따라 적도 사라지게 하게 하기 위한 변수
kk = 0



def handle_events():
    global running
    global dir
    global state
    global cb
    global stage
    events = get_events()

    for event in events:


        # b키로 콜리드 박스 체크
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_b:
                if cb == 0:
                    cb = 1
                elif cb == 1:
                    cb = 0
        # esc키로 나가기
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:

            #if event.key == SDLK_RIGHT and char.is_jumping != 1:
            if event.key == SDLK_RIGHT :
                char.dir = 1
                char.state = 1
                char.face_dir = 1

                if char.jump == 1: #######################
                    char. state = 5
                    char.dir = 1
                    char.face_dir = 1

            #elif event.key == SDLK_LEFT and char.is_jumping != 1:
            elif event.key == SDLK_LEFT :
                char.dir = -1
                char.state = 0
                char.face_dir = -1

                if char.jump == 1: #######################
                    char. state = 4
                    char.dir = -1
                    char.face_dir = -1


            elif event.key == SDLK_z:

                char.jump_sound.play()
                #char.is_jumping = 1

                if char.jump == 0:
                    char.jump = 1

                    if char.face_dir == -1:
                        char.state = 4
                    elif char.face_dir == 1:
                        char.state = 5



            elif event.key == SDLK_c:
                    char.fire_sound.play()
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
    global char, back, enemy1, chimney1, bricks, chimneys, \
        itembox, bricks_3n, flag, collide_box, enemy2, \
        collide_box2, collide_box3, collide_box_fall

    back = Background()
    char = Mario()
    char.gy = 100

    enemy1 = Mushroom(500, 90)
    enemy2 = Turtle(2700,90)

    collide_box = Collide_box(500,90) # 굼바 위치 제한용
    collide_box2 = Collide_box(3000, 90) # 거북이 위치 제한용
    collide_box3 = Collide_box(2550, 90) # 거북이 위치 제한용

    collide_box_fall = Collide_box2(2000, 0) # 바닥 닿으면 게임 오버


    brick_3n1 = Bricks3(450, 180)
    brick1 = Brick(450, 300)

    itembox = Itembox(700, 180)

    chimney1 = Chimney(1000,115)
    brick_3n2 = Bricks3(1250,250)
    chimney2 = Chimney(1500,115)

    brick2 = Brick(1700,250)
    brick3 = Brick(1900,300)
    brick4 = Brick(2100,250)
    brick5 = Brick(2300,300)


    chimney3 = Chimney(2500,115)
    brick_3n3 = Bricks3(3100,180)
    brick6 = Brick(3300, 250)
    brick7 = Brick(3500, 350)
    brick8 = Brick(3700, 400)
    brick_3n4 = Bricks3(3950,470)

    flag = Flag(3950,540)





    bricks = [brick1,brick2,brick3,brick4,brick5,brick6,brick7,brick8]
    bricks_3n = [brick_3n1, brick_3n2, brick_3n3,brick_3n4]


    chimneys = [chimney1,chimney2,chimney3]





    game_world.add_object(back, 0)
    game_world.add_object(char, 1)
    game_world.add_object(enemy1, 2)
    game_world.add_object(collide_box, 0)
    game_world.add_object(collide_box2, 0)
    game_world.add_object(collide_box3, 0)
    game_world.add_object(collide_box_fall, 0)

    game_world.add_object(enemy2, 3)

    #game_world.add_object(brick1, 0)
    #game_world.add_object(brick2, 0)
    #game_world.add_object(brick3, 0)
    game_world.add_objects(bricks, 0)

    game_world.add_objects(bricks_3n, 0)


    game_world.add_objects(chimneys, 0)

    game_world.add_object(itembox, 0)

    game_world.add_object(flag, 0)



def exit():
    game_world.clear()
    char.dx = 0


def update():
    for game_object in game_world.all_objects():
        game_object.update()


    # 벽돌과 캐릭터 충돌 처리
    for bk in bricks:

        if collide_check.collide(char, bk):
            char.jump = 0
            char.jumpval = 0

        if char.y < bk.oy:
            if collide_check.collide(char, bk):
                char.jump = -1

        if collide_check.collide(char, bk):
            if char.x > bk.ox + 20:
                char.jump = -1

        if collide_check.collide(char, bk):
            if char.x < bk.ox -35:
                char.jump = -1

        # 중간 뚫리는 버그 수정
        if collide_check.collide(char, bk):
            if char.y > bk.oy + 20 :
                char.y = bk.oy + 55
            else :
                char.jump = -1









    # 3개짜리 벽돌 충돌 처리
    for bk3 in bricks_3n:
        if char.y < bk3.oy:
            if collide_check.collide(char, bk3):
                char.jump = -1

        if collide_check.collide(char, bk3):
            if char.y > bk3.oy+20:
                char.jump = 0
                char.jumpval = 0

        if collide_check.collide(char, bk3):
            if char.x > bk3.ox + 80:
                char.jump = -1
            elif char.x < bk3.ox - 80:
                char.jump = -1

        if char.y < bk3.oy:
            if collide_check.collide(char, bk3):
                char.jump = -1

        if collide_check.collide(char, bk3):
            if char.y > bk3.oy:
                char.jump = 0
                char.jumpval = 0

        if collide_check.collide(char, bk3):
            if char.x > bk3.ox + 80:
                char.jump = -1
            elif char.x < bk3.ox - 80:
                char.jump = -1

        # 중간 뚫리는 버그 수정
        if collide_check.collide(char, bk3):
            if char.y > bk3.oy + 50:
                char.y = bk3.oy + 55
            else:
                char.jump = -1

        # 점프 후 착지 모습 버그 수정






    # 굴뚝과 충돌처리
    for ch in chimneys:

        # if char.y > ch.oy+30:
        #     if collide_check.collide(char, ch):
        #         char.y = ch.oy + 87
        #         char.jump = 0
        #         char.jumpval = 0


        if collide_check.collide(char, ch):
            if char.y < ch.oy:
                char.dx = 0
                if char.jump == 1:
                    char.x = char.x -1
                    char.dx = 4

                if char.face_dir ==-1 :
                    char.dx = 4

            if char.y > ch.oy:
                char.jump = 0
                char.jumpval = 0

        # 굴뚝 위에서 밑으로 떨어질때
        if collide_check.collide(char, ch):
            if char.x > ch.ox + 40 :
                 char.jump = -1

        # 굴뚝의 오른쪽 통과 x
        if collide_check.collide(char, ch):
            if ch.oy > char.y :
                if char.x > ch.ox + 40:
                    char.dx = 0
                    if char.state ==1:
                        char. dx = 4
                    if char.jump == 1:
                        char.dx = 4


        if collide_check.collide(char, ch):
            if char.y > ch.oy:
                if char.x < ch.ox - 50 :
                    char.jump = -1



        # 굼바와 굴뚝 충돌처리
        if collide_check.collide(enemy1, ch):
            enemy1.dir = -1

        # 굼바와 충돌박스 충돌처리
    if collide_check.collide(enemy1, collide_box):
        enemy1.dir = 1
        # 거북이와 충돌박스 충돌처리
    if collide_check.collide(enemy2, collide_box2):
        enemy2.dir = -1
        # 거북이와 충돌박스 충돌처리
    if collide_check.collide(enemy2, collide_box3):
        enemy2.dir = 1

    if collide_check.collide(char, collide_box_fall):
        game_framework.change_state(gameover_image)


    # 아이템 박스 충돌처리
    if char.y < itembox.oy:
        if collide_check.collide(char, itembox):
            char.jump = -1
            itembox.tick_Itembox = 1
            itembox.itembox_sound.play()

    if collide_check.collide(char, itembox):
        if char.y > itembox.oy:
            char.jump = 0
            char.jumpval = 0

    if collide_check.collide(char, itembox):
        if char.x > itembox.ox + 25:
            char.jump = -1
        elif char.x < itembox.ox -35:
            char.jump =-1

    if itembox.tick_Itembox == 1:
        itembox.item()
        itembox.tick_Itembox = -1

    # 중간 뚫리는 버그 수정
    if collide_check.collide(char, itembox):
        if char.y > itembox.oy + 20:
            char.y = itembox.oy + 55
        else:
            char.jump = -1




    if collide_check.collide(char, enemy1):
        game_framework.change_state(gameover_image)


    # 깃발과 캐릭터 충돌처리
    if collide_check.collide(char, flag):
        delay(0.5)
        game_framework.change_state(play_state2)





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
