from turtle import goto, position, speed
from pycat.core import Window,Sprite,KeyCode
from random import randint

w=Window()
class Owl(Sprite):
    def on_create(self):
        self.image="img/owl.gif"
        self.scale=0.1
        self.x=620 
        self.y=680
    def on_update(self, dt):
        if w.is_key_pressed(KeyCode.UP):
            self.y +=10
        if w.is_key_pressed(KeyCode.RIGHT):
            self.x +=10 
        if w.is_key_pressed(KeyCode.LEFT):
            self.x -=10 
        if w.is_key_pressed(KeyCode.DOWN):
            self.y -=10 
        if self.is_touching_any_sprite():
            print("you lose!")
            w.close()
class Eagle(Sprite):
    def on_create(self):
        self.image="img/eagle.gif"
        self.scale=0.1
        self.goto_random_position()
        while self.is_touching_any_sprite():
            self.goto_random_position()
        
    def on_update(self, dt):
        self.move_forward(4)
        if w.is_key_down(KeyCode.W):
            self.rotation=90
        if w.is_key_down(KeyCode.D):
            self.rotation=0
        if w.is_key_down(KeyCode.A):
            self.rotation=180
        if w.is_key_down(KeyCode.S):
            self.rotation=270


class Fireball(Sprite):
    def on_create(self):
        self.scale=0.2
        self.image="img/fireball.gif"
        self.goto_random_position()
        while self.is_touching_any_sprite():
            self.goto_random_position()
        
w.create_sprite(Owl)
w.create_sprite(Eagle)
for i in range(50):
    w.create_sprite(Fireball)
w.run()


