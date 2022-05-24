from pycat.core import Color, Sprite, Window,KeyCode, Scheduler
from random import randint
w = Window(width=1000,height=1000)


class Player(Sprite):

    def on_create(self):
        self.color = Color.AMBER
        self.scale = 30
        self.speed = 10
        self.x=500
        self.y=500
    def on_update(self, dt):
        if w.is_key_pressed(KeyCode.W):
            self.y += self.speed
        if w.is_key_pressed(KeyCode.S):
            self.y -= self.speed
        if w.is_key_pressed(KeyCode.A):
            self.x -= self.speed
        if w.is_key_pressed(KeyCode.D):
            self.x += self.speed
        if self.is_touching_any_sprite_with_tag("p"):
            w.close()
        if self.is_touching_any_sprite_with_tag("eb"):
            w.close()
    def on_left_click_anywhere(self):
        w.create_sprite(Bullet)


class Bullet(Sprite):
    def on_create(self):
        self.color = Color.RED
        self.scale = 5
        self.position=player.position
        self.add_tag("b")
        self.point_toward_mouse_cursor()

    def on_update(self, dt):
        self.move_forward(10)
        if self.is_touching_window_edge():
            self.delete()

class Enemy(Sprite):
    def on_create(self):
        self.goto_random_position()
        self.scale=(randint(30,50))
        self.set_random_color()
        self.add_tag("p")
        self.time = 0
    
    def on_update(self, dt):
        self.time += dt
        if self.time > 2:
            self.time = 0
            bullet = w.create_sprite(Enemybullet)
            bullet.position = self.position
            bullet.point_toward_sprite(player)
    
        self.point_toward_sprite(player)
        self.move_forward(randint(2,5))
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_any_sprite_with_tag("b"):
            self.delete()

class Enemybullet(Sprite):
    def on_create(self):
        self.color = Color.GREEN
        self.scale = 5
        self.add_tag("eb")

    def on_update(self, dt):
        self.move_forward(10)
        if self.is_touching_window_edge():
            self.delete()


def spawn_enemies():
    for i in range(randint(2,5)):
        w.create_sprite(Enemy)


Scheduler.update(spawn_enemies, (randint(1,3)))

player = w.create_sprite(Player)
w.run()
























