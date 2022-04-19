from random import randint
from pycat.core import Window,Sprite,Scheduler
w=Window(width=450,height=600)


class Ape(Sprite):
    def on_create(self):
        self.x=225
        self.y=300
        self.scale=3
        self.image="img/ape_waiting.png"
        self.wait()
    def wait(self):
        
        Scheduler.wait(1,self.beating_right)
    def beating_right(self):
        self.image="img/ape_angry1.png"
        Scheduler.wait(0.25,self.beating_left)
    def beating_left(self):
        self.image="img/ape_angry2.png"
        Scheduler.wait(0.25,self.beating_right2)
    def beating_right2(self):
        self.image="img/ape_angry1.png"
        Scheduler.wait(0.25,self.beating_left2)
    def beating_left2(self):
        self.image="img/ape_angry2.png"
        Scheduler.wait(0.25,self.create)
    def create(self):
        self.image="img/ape_waiting.png"
        w.create_sprite(Barrel)
        Scheduler.wait(0.25,self.wait)
class Barrel(Sprite):
    def on_create(self):
        self.x=225
        self.y=300
        self.scale=2
        self.image="img/barrel1.png"
        self.rotation=randint(0,180)
    def on_update(self, dt):
        self.move_forward(2)
        if self.is_touching_window_edge():
            self.delete()
        
w.create_sprite(Ape)



w.run()