#Chipo2 with module
import turtle,time
from mod2_chipo import sprite
from mod2_chipo import shapes
wn=turtle.Screen()
wn.setup(1000,800)
wn.bgpic('cross1.gif')
im=[]
shapes(im)
print(im)
chipo=turtle.Turtle()
chipo.showturtle()
chipo.up()
chipo.goto(-40,-275)
sprite(chipo,0,im[0])

m=0
while True:
    m=m+1
    m1=m%10
    chipo.showturtle()
    sprite(chipo,0,im[m1])
    chipo.fd(10)
    X,Y=chipo.position()
    time.sleep(0.2)
    if X>500:
        chipo.hideturtle()
        chipo.goto(-40,-275)
        chipo.showturtle()


