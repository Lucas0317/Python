from random import randint
from pycat.core import Window,Sprite,Color,Scheduler

w=Window(width=1000,height=600)
class Spot(Sprite):
    def on_create(self):
        self.x=500
        self.y=200
        self.scale=randint(5,10)
        self.rotation=randint(45,315)
        self.add_tag('p')
    def on_update(self, dt):
        self.move_forward(1)
        if self.is_touching_window_edge():
            self.delete()
w=Window(width=1000,height=600)
class Button(Sprite):
    def on_create(self):
        self.x=700
        self.y=300
        self.scale=10
    def on_left_click(self):
        lst=w.get_sprites_with_tag("p")
        for x in lst:
            x.color=Color.random_rgb()

        
w.create_sprite(Button)
for i in range(100):
    w.create_sprite(Spot)
w.run()