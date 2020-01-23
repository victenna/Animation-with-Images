import turtle,time,random
wn=turtle.Screen()
wn.bgpic('road.gif')
t=turtle.Turtle()
t1=turtle.Turtle()
t1.up()
image1='helicopter11.gif'
wn.addshape(image1)
t1.shape(image1)
t1.hideturtle()
t1.goto(0,0)
t2=turtle.Turtle()
image2='helicopter21.gif'
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
t1.hideturtle()

imag1=['helicopter11.gif','helicopter12.gif'] 
imag2=['helicopter21.gif','helicopter22.gif']

def helic(img):
    wn.addshape(img)
    t.shape(img)

t.hideturtle()
t.up()
t.speed(1)
t.goto(0,200)
t.setheading(0)
t.showturtle()
i=0
q=1
    
while True:
    time.sleep(0.05)
    X=t.xcor()
    
    
    i1=i%2
    if q>0:
        helic(imag1[i1])
        t.fd(5)
    i=i+1
    time.sleep(0.02)
    
    if X>=480:
        q=-1
    if q<0:
        helic(imag2[i1])
        t.fd(-5)

    if X<-480:
        q=1
    if q>0:
        helic(imag1[i1])
        t.fd(5)
    
  
        

