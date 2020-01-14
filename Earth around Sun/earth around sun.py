import turtle
import random
turtle.tracer(4)
t=turtle.Turtle()
wn=turtle.Screen()
wn.screensize(1200,800,'dark blue')
#t.speed(10)
import time

# Function design of sky stars
def star(x,y,size):
    t.up()
    t.goto(x,y)
    t.down()
    t.color('white','white')
    t.begin_fill()
    t.left(36)
    for i in range(5):
        t.fd(size)
        t.left(144)
    t.end_fill()

#Draw 50 random located stars with different size  
for i in range(50):
    starX=random.randint(-400,400)
    starY=random.randint(-400,400)
    starsize=random.randint(10,20)
    star(starX,starY,starsize)
t.hideturtle()

turtle.tracer(10)

sun=turtle.Turtle()
sun.penup()
image1='sun6.gif'
wn.addshape(image1)
sun.shape(image1)
sun.setposition(0,0)

earth=turtle.Turtle()
earth.up()
image2='earth6.gif'
wn.addshape(image2)
earth.shape(image2)

earth.goto(0,-200)
earth.showturtle()

while True:
    earth.circle(200,1)
    time.sleep(0.02)
