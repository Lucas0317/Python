from pycat.core import Window
from pycat.extensions.turtle import Turtle
w=Window()
t = w.create_sprite(Turtle,y=280,x=640)


t.pen_width=10
def draw_a_circle(size):
    for i in range(36):
        t.move_forward(size)
        t.rotation+=10
        for i in range(36):
            t.move_forward(size)
            t.rotation+=10

draw_a_circle(int(input("size?")))   

w.run()
