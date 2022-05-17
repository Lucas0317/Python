from pycat.core import Window,Sprite,Scheduler,KeyCode,Color
w=Window(width=1000,height=600)
image=["img/1.jpg","img/2.jpg","img/P9bXQ8165649_1611804.png","img/bird.jpg"]
#w.background_image=image[2]
class Button1(Sprite):
    def on_create(self):
        self.color=Color.RED
        self.scale=50
        self.x=200
        self.y=200
    def on_left_click(self):
        w.background_image=image[0]
class Button2(Sprite):
    def on_create(self):
        self.color=Color.YELLOW
        self.scale=50
        self.x=400
        self.y=200
    def on_left_click(self):
        w.background_image=image[1]
class Button3(Sprite):
    def on_create(self):
        self.color=Color.BLUE
        self.scale=50
        self.x=600
        self.y=200
    def on_left_click(self):
        w.background_image=image[2]
class Button4(Sprite):
    def on_create(self):
        self.color=Color.PURPLE
        self.scale=50
        self.x=800
        self.y=200
    def on_left_click(self):
        w.background_image=image[3]

w.create_sprite(Button1)
w.create_sprite(Button2)
w.create_sprite(Button3)
w.create_sprite(Button4)


w.run()