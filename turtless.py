import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
n = 80
h = 0
for i in range (302):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    if i< 50:
        c = colorsys.hsv_to_rgb(h, 0.2, 0.8)
    elif i< 100:
        c = colorsys.hsv_to_rgb(h, 0.4, 0.8)
    elif i< 150:
        c = colorsys.hsv_to_rgb(h, 1, 0.4)
    elif i< 200:
        c = colorsys.hsv_to_rgb(h, 0.6, 0.4)
    h += 1/n
    t.color(c)
    t.left(104)
    t.forward(i*3)
    for j in range (3):
        t.left(5)
        t.forward(i*2)
        t.left(52)
