import turtle,time
wn=turtle.Screen()
wn.setup(850,800)
wn.bgpic('cross1.gif')
turtle.tracer(2)
image0=['01.gif','02.gif','03.gif',\
        '04.gif','05.gif','06.gif',\
        '07.gif','08.gif','09.gif',\
        '010.gif']
t=turtle.Turtle()
t.up()
t.hideturtle()
t.goto(-40,-275)
t.showturtle()
t.penup()
k=0
while True:
    k=k+1
    k1=k%10
    wn.addshape(image0[k1])
    t.shape(image0[k1])
    t.fd(10)
    X,Y=t.position()
    time.sleep(0.2)
    if X>500:
        t.hideturtle()
        t.goto(-40,-275)
        t.showturtle()
