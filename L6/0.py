from turtle import speed
from pycat.core import Window,Sprite,RotationMode,Scheduler
w=Window(background_image="media/underwater_04.png")
class UFO(Sprite):
    def on_create(self):
        self.image="media/saucer.png"
        self.scale=0.5
        self.y=540
        self.rotation_mode=RotationMode.RIGHT_LEFT
        self.score=0
    def on_update(self, dt):
        self.move_forward(10)
        if self.is_touching_window_edge():
            self.rotation +=180
class Alien(Sprite):
    def on_create(self):
        self.image="media/1.png"
        self.scale=0.5
        self.y=100
        self.rotation_mode=RotationMode.RIGHT_LEFT
        self.is_clicked=False
        self.y_speed=0

    def on_left_click(self):
        self.is_clicked =True
    def on_update(self, dt):
        if self.is_clicked:
            self.y +=10
            if self.is_touching_sprite(ufo):
                ufo.score+=1
                self.delete()
                print(ufo.score)
            if self.is_touching_window_edge():
                ufo.score-=1
                self.delete()
                print(ufo.score)
        else:
            self.move_forward(10)
            if self.is_touching_window_edge():
                self.rotation +=180
            self.y+=self.y_speed
            self.y_speed-=0.5
            if self.y <100:
                self.y_speed=10
        








def create_alien():
    w.create_sprite(Alien)
Scheduler.update(create_alien,0.25)
w.create_sprite(Alien)
ufo = w.create_sprite(UFO)
w.run()