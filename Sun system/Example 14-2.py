#Solar Planet Motion
import turtle

wn=turtle.Screen()
wn.setup(1300,1300)
wn.bgpic('sky.gif')
wn.bgcolor('black')
wn.tracer(20)

Img=['Sun.gif','mercury.gif','venus.gif','earth.gif','Mars.gif',\
     'Jupiter.gif','Saturn.gif','Uranus.gif','Neptune.gif','Moon.gif']

planet=[]
turtle.hideturtle()

for n in range(10):
    planet.append(turtle.Turtle())
    planet[n].up()
    wn.addshape(Img[n])
    planet[n].shape(Img[n])
    if n==0:
        planet[0].setposition(0,0)
    elif n==9:
        planet[n].goto(0,-310)
    else:
        planet[n].goto(0,-120-70*(n-1))
    
while True:
    for m in range (1,10):

        planet[m].circle(120+70*(m-1),0.8-0.1*(m-1))
        planet[9].hideturtle()    
        planet[9].goto(planet[3].xcor(),planet[3].ycor())
        planet[9].fd(45)
        planet[9].showturtle()
        planet[9].left(0.1)
            
