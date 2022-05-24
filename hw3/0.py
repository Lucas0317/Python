from pycat.core import Window,Sprite
from random import randint
w=Window()
class Square(Sprite):
    def on_create(self):
        self.goto_random_position()
        self.scale=randint(10,75)
        self.set_random_color()

for i in range(100):
    w.create_sprite(Square)
w.run()