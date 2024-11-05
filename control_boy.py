from pico2d import *
import random
import game_world
from grass import *
from boy import *
from front_grass import *

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            if event.type == SDL_KEYDOWN or SDL_KEYUP:
                boy.add_event(event) # input 이벤트를 boy 에게 전달하고 있다.

def reset_world():
    global running
    global grass
    global boy
    global front_grass

    running = True

    grass = Grass() # 영속 객체
    game_world.add_object(grass, 0)

    boy = Boy() # 영속 객체
    game_world.add_object(boy, 1)

    front_grass = FrontGrass()
    game_world.add_object(front_grass, 2)

def update_world():
    game_world.update_world()

def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()

open_canvas()
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)

# finalization code
close_canvas()