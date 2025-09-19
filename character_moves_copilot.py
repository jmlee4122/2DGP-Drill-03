from pico2d import *
import math

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')

def draw_character(x: float, y: float):
    clear_canvas_now()
    grass.draw_now(400, 30)
    boy.draw_now(x, y)
    delay(0.01)

def move_rectangle():
    print("Moving in Rectangle")
    # bottom line
    for x in range(50, 750, 5):
        draw_character(x, 90)
    # right line
    for y in range(90, 550, 5):
        draw_character(750, y)
    # top line
    for x in range(750, 50, -5):
        draw_character(x, 550)
    # left line
    for y in range(550, 90, -5):
        draw_character(50, y)

def move_triangle():
    print("Moving in Triangle")
    # left edge
    x, y = 150, 90
    angle = 60
    for i in range(100):
        draw_character(x, y)
        x += 5 * math.cos(math.radians(angle))
        y += 5 * math.sin(math.radians(angle))

    # right edge
    for i in range(100):
        draw_character(x, y)
        x += 5 * math.cos(math.radians(angle))
        y -= 5 * math.sin(math.radians(angle))

    # bottom edge
    for x in range(int(x), 150, -5):
        draw_character(x, 90)

def move_circle():
    print("Moving in Circle")
    cx, cy = 400, 300  # center of circle
    radius = 200
    for deg in range(360):
        x = cx + radius * math.cos(math.radians(deg))
        y = cy + radius * math.sin(math.radians(deg))
        draw_character(x, y)

while True:
    move_rectangle()
    move_triangle()
    move_circle()

close_canvas()
