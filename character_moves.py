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
    for y in range(90, 550, 5):
        draw_boy(50, y)
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


def move_left_edge():
    print("Moving left edge")
    x = 150
    y = 90
    end_x = x + 500 * math.cos(math.radians(60))
    end_y = y + 500 * math.sin(math.radians(60))

    while x <= end_x and y <= end_y:
        draw_boy(x, y)
        x += 5
        y += 5 * math.tan(math.radians(60))
        delay(0.01)


def move_right_edge():
    print("Moving right edge")
    x = 150 + 500 * math.cos(math.radians(60))
    y = 90 + 500 * math.sin(math.radians(60))
    end_x = x + 500 * math.cos(math.radians(60))
    end_y = y - 500 * math.sin(math.radians(60))

    while x <= end_x and y >= end_y:
        draw_boy(x, y)
        x += 5
        y -= 5 * math.tan(math.radians(60))
        delay(0.01)



def move_bottom_edge():
    print("Moving bottom edge")
    for x in range(650, 150, -5):
        draw_boy(x, 90)
        delay(0.01)


def move_triangle():
    print("Moving triangle")

    move_left_edge()
    move_right_edge()
    move_bottom_edge()
    pass


while True:
    # move_circle()
    # move_rectangle()
    move_triangle()
    break
    pass

close_canvas()
