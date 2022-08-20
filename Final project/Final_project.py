from pycat.core import Color, Sprite, Window,KeyCode, Scheduler,Label
from random import randint

w = Window(width=1000,height=1000)

class Shop(Sprite):
    def on_create(self):
        self.scale = 0.5
        self.x=100
        self.y=100
        self.image="img/Shop (1).png"
        self.back=w.create_sprite(ShopBack)
        self.heart=w.create_sprite(HeartUp)
        self.bullet=w.create_sprite(BulletUp)
        self.speed_up=None
    def on_update(self, dt):
        if self.is_touching_sprite(player):
            self.back.is_visible=True
            self.heart.is_visible=True
            self.bullet.is_visible=True
            if self.speed_up is None:
                self.speed_up=w.create_sprite(SpeedUp) 


class ShopBack(Sprite):
    def on_create(self):
        self.scale =1000
        self.x=500
        self.y=500
        self.is_visible=False
        self.layer=4
    
    def on_left_click(self):
        self.is_visible=False
        

class SpeedUp(Sprite):
    def on_create(self):
        self.scale =0.5
        self.x=200
        self.y=750
        self.image="img/faster-icon-png-1.png"
        self.layer=5
    def on_left_click(self):
        if self.is_visible and player.money >=5:
            player.speed+=1
            player.money-=5
            self.delete()
            shop.speed_up=None
    def on_left_click_anywhere(self):
        self.delete()
        shop.speed_up=None
class HeartUp(Sprite):
    def on_create(self):
        self.scale =0.3
        self.x=600
        self.y=750
        self.image="img/life.png"
        self.layer=5
        self.is_visible=False
    def on_left_click(self):
        if self.is_visible and player.money >=10:
            player.life+=10
            player.money-=10
    def on_left_click_anywhere(self):
        self.is_visible=False
class BulletUp(Sprite):
    def on_create(self):
        self.scale =0.3
        self.x=500
        self.y=300
        self.image="img/Picture1.png"
        self.layer=5
        self.is_visible=False
    def on_left_click(self):
        if self.is_visible and player.money >=50:
            player.bullet_n+=1
            player.money-=50
    def on_left_click_anywhere(self):
        self.is_visible=False

class Player(Sprite):

    def on_create(self):
        self.scale =0.3
        self.speed =10
        self.life=100
        self.x=500
        self.y=500
        self.money=0
        self.image="img/costume2.png"
        self.bullet_n=1
    def on_update(self,dpeed):
        if w.is_key_pressed(KeyCode.W):
            self.y += self.speed
            print(self.speed)
        if w.is_key_pressed(KeyCode.S):
            self.y -= self.speed
        if w.is_key_pressed(KeyCode.A):
            self.x -= self.speed
        if w.is_key_pressed(KeyCode.D):
            self.x += self.speed
        if self.life<=1:
            end_game(Lose)
    def on_left_click_anywhere(self):
        for i in range(self.bullet_n):
            w.create_sprite(Bullet)
class PlayerLife(Label):
    def on_create(self):
        self.scale=5
        self.color = Color.GREEN
        self.text="100"
    def on_update(self, dt):
        self.text=str(player.life)
        self.position=player.position
class PlayerMoney(Label):
    def on_create(self):
        self.scale=5
        self.color = Color.BLUE 
        self.text="0"
        self.layer=5
        self.x=50
        self.y=950
    def on_update(self, dt):
        self.text=str(player.money)
class Bullet(Sprite):
    def on_create(self):
        self.color = Color.RED
        self.scale = 5
        self.position=player.position
        self.add_tag("b")
        self.point_toward_mouse_cursor()
        self.rotation+=(randint(-10,10))
        

    def on_update(self, dt):
        self.move_forward(10)
        if self.is_touching_sprite(enemy_castle):
            self.delete()
            enemy_castle.life-=5
            print(enemy_castle.life)
            player.money+=1
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_sprite(shop.back):
            self.delete()
        if self.is_touching_any_sprite_with_tag("b_e"):
            self.rotation+=180
            if self.is_touching_sprite(player):
                player.life-=10
                self.delete()
        enemies_hit = self.get_touching_sprites_with_tag("Enemy")
        if enemies_hit:
            self.delete()
            for e in enemies_hit:
                e.delete()
                player.money+=2



class EnemyCastle(Sprite):
    def on_create(self):
        self.x=900
        self.y=500
        self.scale=1
        self.image="img/zombie.png"
        self.life=2000
    def on_update(self, dt):
        if self.life<=1:
            end_game(Win)
class EnemyCastleLife(Label):
    def on_create(self):
        self.x=900
        self.y=950
        self.scale=5
        self.color = Color.RED
        self.text="0"
    def on_update(self, dt):
        self.text=str(enemy_castle.life)
            
            
class Enemy(Sprite):
    def on_create(self):
        self.x =950
        self.y =(randint(1,1000))
        self.scale=0.5
        self.set_random_color()
        self.time = 0
        self.add_tag("Enemy")
        self.image="img/costume4.png"

    
    def on_update(self, dt):
        self.time += dt
        if self.time > 1:
            self.time = 0
            bullet = w.create_sprite(EnemyBullet)
            bullet.position = self.position
            bullet.point_toward_sprite(player)
        if self.is_touching_sprite(shop.back):
            self.delete()
    
        self.point_toward_sprite(player)
        self.move_forward(randint(2,5))
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_sprite(player):
            self.delete()
            player.life-=10
            player.money=max(0,player.money-2)
            print(player.life)


class EnemyBullet(Sprite):
    def on_create(self):
        self.color = Color.GREEN
        self.scale = 5
        self.add_tag("b_e")
    def on_update(self, dt):
        self.move_forward(10)
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_sprite(player):
            self.delete()
            player.life-=5
            player.money=max(0,player.money-1)
        if self.is_touching_sprite(shop.back):
            self.delete()
        if self.is_touching_any_sprite_with_tag("b"):
            self.rotation+=180
            if self.is_touching_sprite(enemy):
                self.delete()
                enemy.delete()

def spawn_enemies():
    for i in range(randint(2,5)):
        enemy=w.create_sprite(Enemy)

def end_game(cls):
    Scheduler.cancel_update(spawn_enemies)
    w.delete_all_sprites()
    w.delete_all_labels()
    w.create_sprite(cls)



class Win(Sprite):
    def on_create(self):
        self.scale = 1
        self.x=500
        self.y=500
        self.image="img/win.png"
    def on_left_click(self):
        w.close()
class Lose(Sprite):
    def on_create(self):
        self.scale = 1
        self.x=500
        self.y=500
        self.image="img/lose.png"
    def on_left_click(self):
        w.close()



Scheduler.update(spawn_enemies, (randint(1,3)))
w.create_label(EnemyCastleLife)
w.create_label(PlayerLife)
w.create_label(PlayerMoney)
player = w.create_sprite(Player)
shop = w.create_sprite(Shop)
enemy_castle = w.create_sprite(EnemyCastle)
for i in range((randint(1,3))):
    enemy=w.create_sprite(Enemy)
w.run()


