from pico2d import *
import game_framework
import play_state
import play_state2

image = None

def enter():

    play_state.kk = 0
    global image
    global sound
    image = load_image('gameover.png')
    sound = load_music('die.wav')
    sound.set_volume(64)
    sound.play()


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
            game_framework.change_state(play_state)
            play_state.kk = None
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
            game_framework.change_state(play_state2)
            play_state2.kk = None


def update():
    pass

def pause():
    pass

def resume():
    pass