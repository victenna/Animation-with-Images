import turtle,time
car=turtle.Turtle()
turtle.tracer(2)
car.up()
car.hideturtle()
wn=turtle.Screen()
wn.setup(800,800)
turtle.bgcolor('light blue')
wn.bgpic('street.gif')

#car image========================================

cars=['car2.gif','car3.gif','car4.gif']
car=turtle.Turtle() #car turtle
for i in range(3):
    wn.addshape(cars[i])
car.up()
car.setposition(-400,-210)
car.setheading(12)


#boy image===========================================
image1=['man1.gif','man2.gif','man3.gif','man4.gif','man5.gif','man6.gif'] 
image2=['boy21.gif','boy22.gif','boy23.gif','boy24.gif','boy25.gif','boy26.gif'] 
image3=['boy41.gif','boy42.gif','boy43.gif','boy44.gif','boy45.gif','boy46.gif']

t11=turtle.Turtle() #boy turtle
t12=turtle.Turtle() #boy turtle
t13=turtle.Turtle() #boy turtle

X1=180
Y1=-20
def boy_(turtle,X,Y,img):
    wn.addshape(img)
    turtle.shape(img)
    turtle.up()
    turtle.goto(X,Y)
    turtle.showturtle()

  
    
boy_(t11,180,-20,image1[0])
boy_(t12,230,-10,image2[0])
boy_(t13,130,-40,image3[0])

 
#sign image for pedestrians===============================
sign=['w_no.gif','w_yes.gif']
t2=turtle.Turtle() #sign turtle
t2.hideturtle()
t2.up()
t2.setposition(90,20)
t2.showturtle()
def sign_(img1):
    wn.addshape(img1)
    t2.shape(img1)
sign_(sign[1])

#traffic light image=============================================
light=['red_light.gif','yellow_light.gif','green_light.gif']
t3=turtle.Turtle() #traffic light
t3.hideturtle()
t3.up()
t3.setposition(350,150)
t3.showturtle()
def light_(img2):
    wn.addshape(img2)
    t3.shape(img2)
light_(light[2])

turtle.tracer(2)

# function man walks===========================

deltaX=5 #determines walking direction
deltaY=-2.5 #determines walking direction

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
        light_(light[2])
        sign_(sign[0])
        if car.xcor==-152:
            car.shape(car[0])
    if car.xcor()>-152:
        
        if r<30:
            car.shape(cars[0])
            r=r+1
            light_(light[1])
            sign_(sign[0])
                    
        if r>=29 and r<81:
            r=r+1
            q1=q%6
            light_(light[0])
            sign_(sign[1])
            r1=r-29
                       
            boy_(t11,180+r1*deltaX,-20+r1*deltaY,image1[q1])
            boy_(t12,230+r1*deltaX,-10+r1*deltaY,image2[q1])
            boy_(t13,130+r1*1.2*deltaX,-40+1.2*r1*deltaY,image3[q1])
            time.sleep(0.05)
  
        if r>=81:
            car.shape(cars[q0])
            move=1
            car.fd(10*move)
            light_(light[2])
            sign_(sign[0])
                        
    if car.xcor()>500:
        q=-1
        boy_(t11,180,-20,image1[0])
        boy_(t12,230,-10,image2[0])
        boy_(t13,130,-40,image3[0])
        r=0
        car.hideturtle()
        car.setposition((-400,-210))
        car.showturtle()

