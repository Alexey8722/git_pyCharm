import turtle


SCREEN_WIDGT = 600
SCREEN_HEIGHT = 600
TARGET_LEFT_X = 100
TARGET_LEFT_Y = 250
TARGET_WIDTH = 25
FORCE_FACTER = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

turtle.setup(SCREEN_WIDGT,SCREEN_HEIGHT)

turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LEFT_X,TARGET_LEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

turtle.goto(0,0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)
turtle.done()
angel = float(input("Введите угол выстрела снаряда:"))
force = float(input("Введите пусковую силу(1-10:"))