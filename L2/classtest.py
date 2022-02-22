from pycat.core import Window,Sprite
from random import randint
w=Window()

class Owl(Sprite):
    def on_create(self):
        self.image="owl.gif"
        self.set_random_color()
        self.goto_random_position()
        self.opacity= randint(0, 255)
class Fireball(Sprite):
    def on_create(self):
        self.image="fireball.gif"
        self.set_random_color()
        self.goto_random_position()
        self.opacity= randint(0, 255)

for i in range(99):
    w.create_sprite(Owl)
    w.create_sprite(Fireball) 
w.run()