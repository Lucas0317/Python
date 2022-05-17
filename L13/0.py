from random import randint
from pycat.core import Window,Sprite

w=Window(width=1000,height=600)
class Spot(Sprite):
    def on_create(self):
        self.x=500
        self.y=200
        self.scale=randint(5,10)
        self.set_random_color()
        self.rotation=randint(45,315)
    def on_update(self, dt):
        self.move_forward(10)
        if self.is_touching_window_edge():
            self.delete()

for i in range(5000):
    w.create_sprite(Spot)
w.run()