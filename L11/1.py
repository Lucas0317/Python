from pycat.core import Window,Sprite,Scheduler,KeyCode,Color,Label
w=Window(width=1000,height=600)
image=["img/1.jpg","img/2.jpg","img/P9bXQ8165649_1611804.png","img/bird.jpg"]
w.background_image=image[0]
class Next(Sprite):
    def on_create(self):
        self.color=Color.GREEN
        self.scale=50
        self.x=800
        self.y=300
        self.img=0
    def on_left_click(self):
        self.img +=1
        if self.img == len(image):
            self.img =0
        w.background_image=image[self.img]
class Last(Sprite):
    def on_create(self):
        self.color=Color.RED
        self.scale=50
        self.x=200
        self.y=300
        self.img=0
    def on_left_click(self):
        next.img -=1
        if next.img ==-1:
            next.img =len(image)-1
        w.background_image=image[next.img]
class Click_time(Label):
    def on_create(self):
        self.color=Color.PURPLE
next=w.create_sprite(Next)
w.create_sprite(Last)
w.run()