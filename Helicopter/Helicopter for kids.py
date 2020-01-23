import turtle,time,random
wn=turtle.Screen()
wn.bgpic('road.gif')
t1=turtle.Turtle()
t1.up()
image1='helicopter1.gif'
wn.addshape(image1)
t1.shape(image1)
t1.hideturtle()
t1.goto(0,0)
t2=turtle.Turtle()
image2='helicopter2.gif'
wn.addshape(image2)
t2.shape(image2)
t2.up()
t2.hideturtle()
t2.goto(0,300)

turtle.tracer(2)
turtle.bgcolor('brown')
dx=2
Xposition=0
Yposition=0
dy=2
t1.showturtle()
for i in range (100):
    t1.goto(0,Yposition)
    Yposition=Yposition+dy
    time.sleep(0.015)
   

while True:
    time.sleep(0.005)
    Xposition=Xposition+dx
    
    if Xposition>480:
        dx=dx*-1
    if Xposition<-480:
        dx=dx*-1

    if dx>0:
        t2.hideturtle()
        t1.showturtle()
        t1.goto(Xposition,200)
    if dx<0:
        t1.hideturtle()
        t2.showturtle()
        t2.goto(Xposition,200)
    
   
            
    
        

