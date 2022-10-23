from pico2d import *
import game_framework
import def_obj

image = None

def enter():
    global image
    image = load_image('start.png')

def exit():
    global image
    del image

def draw():
    clear_canvas()
    image.draw(800//2, 640//2)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(def_obj)
def update():
    pass

def pause():
    pass

def resume():
    pass