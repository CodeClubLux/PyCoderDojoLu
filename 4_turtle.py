#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

from turtle import *
color('red', 'yellow')
count = 0
begin_fill()
while count < 4:
  forward(200)
  left(90)
  count += 1 # == count = count + 1
end_fill()
done()