from pycat.core import Window,Sprite,Color,Label
w=Window(width=450,height=600)

class Button1(Sprite):
    def on_create(self):
        self.x=150
        self.y=100
        self.scale=75
        self.color=Color.GREEN
    def on_left_click(self):
        time.is_active= not time.is_active

class Button2(Sprite):
    def on_create(self):
        self.x=300
        self.y=100
        self.scale=75
        self.color=Color.RED
    def on_left_click(self):
        time.text="00.00"
        time.time=0
class Button3(Sprite):
    def on_create(self):
        self.x=225
        self.y=200
        self.scale=100
        self.color=Color.YELLOW
    def on_left_click(self):
        print(round(time.time,2))
class Time(Label):
    def on_create(self):
        self.x=175
        self.y=500
        self.text="00.00"
        self.time = 0
        self.is_active=False
    def on_update(self, dt):
        if self.is_active:
            self.time +=dt
            self.text=str(round(self.time,2))
        



w.create_sprite(Button1)
w.create_sprite(Button2)
w.create_sprite(Button3)
time=w.create_label(Time)
w.run()