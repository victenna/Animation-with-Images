import turtle,time
from mod_chipo import sprite
wn=turtle.Screen()
turtle.tracer(2)
wn.bgpic('cross1.gif')
image=['01.gif','02.gif','03.gif',\
        '04.gif','05.gif','06.gif',\
        '07.gif','08.gif','09.gif',\
        '010.gif']

chipo=turtle.Turtle()
chipo.showturtle()
chipo.goto(-40,-275)

sprite(chipo,0,image[0])


for m in range(100):
    m1=m%10
    chipo.showturtle()
    sprite(chipo,0,image[m1])
    chipo.fd(10)
    time.sleep(0.2)
