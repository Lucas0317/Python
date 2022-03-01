from pycat.core import Window,Sprite
from random import Random, randint, random
w=Window()

class Owl(Sprite):
    def on_create(self):
        self.image="img/owl.gif"
        self.x=0 
        self.y=300
    def on_update(self, dt):
        self.x +=13
        if self.x>=w.width:
            print("owl win")
            w.close()


class Fireball(Sprite):
    def on_create(self):
        self.image="img/fireball.gif"
        self.x=400
        self.y=450
    def on_update(self, dt):
        self.x +=8
        if self.x>=w.width:
            print("fireball win")
            w.close()
class tiger(Sprite):
    def on_create(self):
        self.image="img/tiger.png"
        self.x=750
        self.y=150
    def on_update(self, dt):
        self.x +=505
        if self.x>=w.width:
            print("tiger win")
            w.close()


w.create_sprite(Owl)
w.create_sprite(Fireball) 
w.create_sprite(tiger) 
w.run()