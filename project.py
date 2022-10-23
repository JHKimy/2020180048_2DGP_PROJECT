from pico2d import *

G_WIDTH, G_HEIGHT = 800, 640


x = 30
y = 90


frame = 0
dirX = 0
dirY = 0
state = 3
dir_state = 0

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
                dirX += 1
                state = 1
            elif event.key == SDLK_LEFT:
                dirX -= 1
                state = 0

            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX -= 1
                state = 3
            elif event.key == SDLK_LEFT:
                dirX += 1
                state = 2


open_canvas(G_WIDTH, G_HEIGHT)
TUK_GROUND = load_image('background.png')
character = load_image('mario.png')
running = True

while running:
        clear_canvas()
        TUK_GROUND.draw(G_WIDTH//2, G_HEIGHT//2)
        if state == 0 or state == 1:
            character.clip_draw(frame * 100, state * 100, 100, 100, x, y)
        else :
            character.clip_draw(100, state * 100, 100, 100, x, y)
        update_canvas()
        handle_events()
        frame = (frame + 1) % 3
        x += dirX * 5
        y += dirY * 5
        delay(0.01)


close_canvas()