from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

def handle_events():
    global running, x, y, points

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            points.append((event.x, TUK_HEIGHT - 1 - event.y))
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def draw_line(p1, p2):
    global framex, framey, running
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    if x1 > x2:
        framey = 0
    else:
        framey = 1

    for i in range(0, 100 + 1, 4):
        t = i / 100
        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2
        framex = (framex + 1) % 8
        clear_canvas()
        tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        for m in range(0, len(points)):
            cursor.draw(points[m][0], points[m][1])
        character.clip_draw(framex * 100, framey * 100, 100, 100, x, y)
        delay(0.05)
        update_canvas()
        handle_events()
        if running == False:
            exit()
    pass

running = True
framex = 0
framey = 1

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2

now = [(TUK_WIDTH // 2, TUK_HEIGHT // 2)]
points = []
while True:
    if len(points) >= 1:
        draw_line(now[0], points[0])
        now[0] = points[0]
        del points[0]
    else:
        framex = (framex + 1) % 8
        clear_canvas()
        tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        character.clip_draw(framex * 100, framey * 100, 100, 100, now[0][0], now[0][1])
        delay(0.05)
        update_canvas()
        handle_events()
        if running == False:
            exit()

close_canvas()