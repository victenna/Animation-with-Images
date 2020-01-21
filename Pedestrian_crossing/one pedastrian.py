import turtle,time
wn=turtle.Screen()
wn.setup(800,800)
turtle.bgcolor('light blue')
wn.bgpic('street.gif')
turtle.tracer(2)

#car ========================================
car=turtle.Turtle()
cars=['car2.gif','car3.gif','car4.gif']
for i in range(3):
    wn.addshape(cars[i])
car.up()
car.setposition(-400,-210)
car.setheading(12)

#light========================================
light=turtle.Turtle()
lights=['red_light.gif','yellow_light.gif','green_light.gif']
for i in range(3):
    wn.addshape(lights[i])
light.up()
light.setposition(350,150)
light.shape(lights[2])
#sign===================================
sign=turtle.Turtle()
signs=['w_no.gif','w_yes.gif']
for i in range(2):
    wn.addshape(signs[i])
sign.up()
sign.setposition(90,20)
sign.shape(signs[1])    

#man============================================
man=turtle.Turtle()
mans=['man1.gif','man2.gif','man3.gif','man4.gif','man5.gif','man6.gif']
for i in range(6):
    wn.addshape(mans[i])
man.shape(mans[3])
man.up()
man.goto(180,-20)

deltaX=5 #determines direction 0f walking (X coordinate)
deltaY=-2.5 #determines  direction of walking (Y coordinate)
q=-1
move=1
r=0
while True:
    q=q+1
    q0=q%3
    time.sleep(0.03)
    if car.xcor()<-151:
        car.shape(cars[q0])
        move=1
        car.fd(10*move)
        light.shape(lights[2])
        sign.shape(signs[0])

    if car.xcor()>-152:
        
        if r<30:
            car.shape(cars[0])
            r=r+1
            light.shape(lights[1])
            sign.shape(signs[0])
                    
        if r>=29 and r<81:
            r=r+1
            q1=q%6
            light.shape(lights[0])
            sign.shape(signs[1])
            r1=r-29
            man.shape(mans[q1])
            man.goto(180+r1*deltaX,-20+r1*deltaY)
            time.sleep(0.1)
  
        if r>=81:
            car.shape(cars[q0])
            move=1
            car.fd(10*move)
            light.shape(lights[2])
            sign.shape(signs[0])
                       
    if car.xcor()>500:
        q=-1
        man.shape(mans[3])
        man.hideturtle()
        man.goto(180,-20)
        man.showturtle()
        r=0
        car.hideturtle()
        car.setposition((-400,-210))
        car.showturtle()

