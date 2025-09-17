from pico2d import *

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')


def move_top():
    print("Moving top")
    for x in range(50, 750, 5):
        draw_boy(x, 550)
    pass


def move_right():
    print("Moving right")
    for y in range(550, 90, -5):
        draw_boy(750, y)
    pass


def move_bottom():
    print("Moving bottom")
    for x in range(750, 50, -5):
        draw_boy(x, 90)
    pass


def move_left():
    print("Moving left")
    pass


def move_rectangle():
    print("Moving rectangle")

    move_top()
    move_right()
    move_bottom()
    move_left()

    pass


def move_circle():
    print("Moving circle")
    r = 200
    for deg in range(360):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300

        draw_boy(x, y)
    pass


def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)


while True:
    # move_circle()
    move_rectangle()
    break
    pass

close_canvas()
