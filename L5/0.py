
from cProfile import label
from pycat.core import Window,Sprite,KeyCode,RotationMode,Scheduler
w=Window(background_image="img/forest_background.jpg")
class Eagle(Sprite):
    def on_create(self):
        self.image="img/eagle.gif"
        self.scale=0.5
        self.goto_random_position()
        self.y=80
        self.rotation_mode=RotationMode.RIGHT_LEFT
        self.score=0
        self.add_tag("eag")
        self.set_random_color()

    def on_update(self, dt):
        if w.is_key_pressed(KeyCode.RIGHT):
            self.x +=10
            self.rotation=0 
        if w.is_key_pressed(KeyCode.LEFT):
            self.x -=10 
            self.rotation=180 
        if w.is_key_pressed(KeyCode.UP):
            self.y +=10
            self.rotation=0 
        if w.is_key_pressed(KeyCode.DOWN):
            self.y -=10 
            self.rotation=180 
        if w.is_key_pressed(KeyCode.SPACE):
            self.goto_random_position()
            self.y=80
        if w.is_key_down(KeyCode.B):
            w.create_sprite(Eagle)
            self.set_random_color()

            
class Gem(Sprite):
    def on_create(self):
        self.image="img/gem_shiny04.png"
        self.scale=0.3
        self.goto_random_position()
        self.y=w.height
        
    def on_update(self, dt):
        self.y -=10
        self.rotation+=5
        self.set_random_color()
        if self.y<0:
            self.delete()
        if self.is_touching_any_sprite_with_tag("eag"):
            eagle.score+=2
            print(eagle.score)
            self.delete()
            lab.text="score"+str(eagle.score)
            
            
class Gem1(Sprite):
    def on_create(self):
        self.image="img/gem_shiny01.png"
        self.scale=0.1
        self.goto_random_position()
        self.y=w.height
    def on_update(self, dt):
        self.y -=15
        self.rotation+=5
        if self.y<0:
            self.delete()
        if self.is_touching_any_sprite_with_tag("eag"):
            eagle.score-=3
            print(eagle.score)
            self.delete()
            lab.text="score"+str(eagle.score)


eagle=w.create_sprite(Eagle)
lab=w.create_label()
def create():
    w.create_sprite(Gem)
    w.create_sprite(Gem1)
Scheduler.update(create,0.5)

    

w.run()
