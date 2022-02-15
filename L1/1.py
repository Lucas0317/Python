from os import O_WRONLY
from zipapp import create_archive
from pycat.core import Window
window=Window()
answer=input("what animal do yo like? ")
animal=window.create_sprite()
a=window.create_sprite()
b=window.create_sprite()
c=window.create_sprite()
d=window.create_sprite()
e=window.create_sprite()
f=window.create_sprite()
animal.x=620
animal.y=320
b.x=1000
b.y=200
c.x=1000
c.y=540
d.x=700
d.y=536
e.x=543
e.y=324
f.x=423
f.y=234
a.x=876
a.y=580

if answer=="owl":
    animal.image="owl.gif"
if answer=="tiger":
    animal.image="tiger.png"
if answer=="elephant":
    animal.image="elephant.png"
if answer=="pig":
    animal.image="pig.png"
if answer=="rat":
    animal.image="rat.png"
if answer=="rooster":
    animal.image="rooster.png"  
if answer=="wildcat":
    animal.image="wildcat.png"
if answer=="all":
    a.image="wildcat.png"
    b.image="rooster.png"
    c.image="rat.png"
    d.image="pig.png" 
    e.image="elephant.png"
    f.image="tiger.png"
    animal.image="owl.gif"
window.run()