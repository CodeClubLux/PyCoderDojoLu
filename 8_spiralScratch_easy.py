#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

import turtle
import random

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

# We do not need to set x, y to 0,0 because this is always the default position when starting a turtle program

increase = 0

width = myWin.window_width()
height = myWin.window_height()

degrees = int(input("Please provide an angle: "))
steps = int(input("Please tell me how many steps you want to go? (1-10) "))

# By default color mode is 1.0
#myWin.colormode(255)

while True:
  if steps > 0:
    myTurtle.pencolor((random.random(), random.random(), random.random()))
    #myTurtle.pencolor((random.randrange(255), random.randrange(255), random.randrange(255)))
    myTurtle.forward(steps)
    myTurtle.right(degrees)
    steps += steps
    print(myTurtle.position())

myWin.exitonclick()