from pycat.core import Window,Sprite,KeyCode

w=Window()

class Owl(Sprite):
    def on_create(self):
        self.image="img/owl.gif"
        self.x=0 
        self.y=300
    def on_update(self, dt):
        if w.is_key_down(KeyCode.NUM_0):
            self.x +=6
        elif w.is_key_pressed(KeyCode.BACKSPACE):
            self.x +=5
        if self.x>=w.width:
            print("owl win")
            w.close()


class Fireball(Sprite):
    def on_create(self):
        self.image="img/fireball.gif"
        self.x=0
        self.y=450
    def on_update(self, dt):
        if w.is_key_up(KeyCode._1):
            self.x +=7
        elif w.is_key_pressed(KeyCode._2):
            self.x +=4           
        if self.x>=w.width:
            print("fireball win")
            w.close()
class Tiger(Sprite):
    def on_create(self):
        self.image="img/tiger.png"
        self.x=0
        self.y=150
    def on_update(self, dt):
        self.x +=5
        if w.is_key_pressed(KeyCode.SPACE):
            self.x=5
        if self.x>=w.width:
            print("tiger win")
            w.close()


w.create_sprite(Owl)
w.create_sprite(Fireball) 
w.create_sprite(Tiger) 
w.run()