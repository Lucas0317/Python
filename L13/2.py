from random import randint
from pycat.core import Window,Sprite,Color,Scheduler

w=Window(width=1000,height=600)
class Spot(Sprite):
    def on_create(self):
        self.position=w.mouse_position
        #for i in range(10):
            #self.y +=10
            #w.create_sprite(Spot)
        self.scale=randint(5,10)
        self.rotation=randint(0,359)
        self.add_tag('p')
    def on_update(self, dt):
        self.move_forward(randint(1,10))
        if self.is_touching_window_edge():
            self.delete()

class God(Sprite):
    def on_left_click_anywhere(self):
        c=Color.random_rgb()
        for i in range(100):
            spot=w.create_sprite(Spot, color=c)
w.create_sprite(God)
w.run()