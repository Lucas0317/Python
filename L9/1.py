from random import randint
from pycat.core import Window,Sprite,Scheduler
w=Window(width=450,height=600)


class Ape(Sprite):
    def on_create(self):
        self.x=225
        self.y=300
        self.scale=3
        self.state=1
        self.time=0
        self.image="img/ape_waiting.png"
    def on_update(self, dt):
        self.time += dt
        if self.state==1:
            if self.time>2:
                self.state=2
                self.time=0
        elif self.state==2:
            self.image="img/ape_angry1.png"
            
            if self.time>0.3:
                self.state=3
                self.time=0
        elif self.state==3:
            self.image="img/ape_angry2.png"
            if self.time>0.3:
                self.state=4
                self.time=0
        elif self.state==4:
            self.image="img/ape_waiting.png"
            w.create_sprite(Barrel)
            self.state=1
            self.time=0




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