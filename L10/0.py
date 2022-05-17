from pycat.core import Window,Sprite,Scheduler,KeyCode
w=Window(width=1000,height=600)
class Shark(Sprite):
    def on_create(self):
        self.x=500
        self.y=300
        self.scale=0.25
        self.image="img/shark.png"
        self.wait_sec=1
        self.fire_spd=1
        self.shark_spd=5
        self.point_toward_sprite(penguin)
        self.wait()
    def wait(self):
        self.wait_sec -=0.05
        if self.wait_sec < 0.1:
            self.wait_sec=0.1
        self.image="img/shark open_mouth.png"
        Scheduler.wait(self.wait_sec,self.open_mouth)
    def open_mouth(self):
        self.wait_sec -=0.05
        if self.wait_sec < 0.1:
            self.wait_sec=0.1
        w.create_sprite(Fireball)
        self.fire_spd +=0.5
        Scheduler.wait(self.wait_sec,self.fire_ball)
    def fire_ball(self):
        self.wait_sec -=0.05
        if self.wait_sec < 0.1:
            self.wait_sec=0.1
        self.image="img/shark bite.png"
        Scheduler.wait(self.wait_sec,self.bite)
    def bite(self):
        self.wait_sec -=0.05
        if self.wait_sec < 0.1:
            self.wait_sec=0.1
        self.point_toward_sprite(penguin)
        self.move_forward(self.shark_spd)
        self.shark_spd +=5
        Scheduler.wait(self.wait_sec,self.wait)
class Fireball(Sprite):
    def on_create(self):
        self.x=shark.x
        self.y=shark.y
        self.scale=0.25
        self.image="img/fireball.gif"
        self.point_toward_sprite(penguin)
    def on_update(self, dt):
        self.move_forward(shark.fire_spd)
        self.point_toward_sprite(penguin2)
        if self.is_touching_window_edge():
            self.delete()
class Penguin(Sprite):
    def on_create(self):
        self.x=200
        self.y=300
        self.scale=0.25
        self.life =1
        self.image="img/penguin.png"
    def on_update(self, dt):
        lab.text="P1:Life"+str(self.life)
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
            self.rotation=0
            self.goto_random_position()
        if self.is_touching_any_sprite():
            if self.life <1:
                w.close()
            else:
                self.life -=1
class Penguin2(Sprite):
    def on_create(self):
        self.x=200
        self.y=300
        self.scale=0.25
        self.life =1
        self.image="img/penguin.png"
    def on_update(self, dt):
        lab.text="P2:Life"+str(self.life)
        if w.is_key_pressed(KeyCode.D):
            self.x +=10
            self.rotation=0 
        if w.is_key_pressed(KeyCode.A):
            self.x -=10 
            self.rotation=180 
        if w.is_key_pressed(KeyCode.W):
            self.y +=10
            self.rotation=0 
        if w.is_key_pressed(KeyCode.S):
            self.y -=10 
            self.rotation=180 
        if w.is_key_pressed(KeyCode.SPACE):
            self.rotation=0
            self.goto_random_position()
        if self.is_touching_any_sprite():
            if self.life <1:
                w.close()
            else:
                self.life -=1
lab=w.create_label()
penguin = w.create_sprite(Penguin)
Penguin2 = w.create_sprite(Penguin2)
shark   = w.create_sprite(Shark)
w.run()

