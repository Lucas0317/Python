from pycat.core import Window
window=Window()
tiger=window.create_sprite()
tiger.image="tiger.png"
tiger.x=640
tiger.y=321
owl=window.create_sprite()
owl.image="owl.gif"
owl.x=550
owl.y=500
window.run()