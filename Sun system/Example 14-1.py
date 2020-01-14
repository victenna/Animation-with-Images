import turtle
import random
wn=turtle.Screen()
wn.setup(1200,1000)
wn.bgcolor('black')
wn.bgpic('sky.gif')
wn.tracer(30)
#---------------------------------------
sun=turtle.Turtle('circle')         #Sun
sun.penup()
sun.color('yellow')
sun.penup()
Sun_image='Sun.gif'
wn.addshape(Sun_image)
sun.shape(Sun_image)
sun.setposition(0,0)
#------------------------------------------
mercury=turtle.Turtle()             #Mercury
mercury.up()
Mercury_image='mercury.gif'
wn.addshape(Mercury_image)
mercury.shape(Mercury_image)
mercury.setposition(0,-110)
#------------------------------------------
venus=turtle.Turtle()                #Venus
venus.up()
Venus_image='venus.gif'
wn.addshape(Venus_image)
venus.shape(Venus_image)
venus.setposition(0,-135)
#venus.up()
#------------------------------------------
earth=turtle.Turtle()                #Earth
earth.up()
Earth_image='earth.gif'
wn.addshape(Earth_image)
earth.shape(Earth_image)
earth.setposition(0,-190)
#------------------------------------------
moon=turtle.Pen()                   #Moon
moon.up()
moon.setposition(0,60)
moon.shape('circle')
moon.shapesize(0.5)
moon.color('yellow')
moon.speed(0)
#----------------------------------------------
mars=turtle.Turtle()               #Mars  
mars.up()
Mars_image='Mars.gif'
wn.addshape(Mars_image)
mars.shape(Mars_image)
mars.setposition(0,-280)
#----------------------------------------------
jupiter=turtle.Turtle()               #Jupiter
jupiter.up()
Jupiter_image='Jupiter.gif'
wn.addshape(Jupiter_image)
jupiter.shape(Jupiter_image)
jupiter.setposition(0,-350)
#----------------------------------------------
saturn=turtle.Turtle()                #Saturn 
saturn.up()
Suturn_image='Saturn.gif'
wn.addshape(Suturn_image)
saturn.shape(Suturn_image)
saturn.setposition(0,-450)
#------------------------------------------------
uranus=turtle.Turtle()                #Urans     
uranus.up()
Uranus_image='Uranus.gif'
wn.addshape(Uranus_image)
uranus.shape(Uranus_image)
uranus.setposition(0,-540)
#----------------------------------------------------
neptune=turtle.Turtle()               #Neptune
neptune.up()
Neptune_image='Neptune.gif'
wn.addshape(Neptune_image)
neptune.shape(Neptune_image)
neptune.setposition(0,-590)
#----------------------------------------------
while True:
    mercury.circle(110,0.478)       #Planetary motion
    venus.circle(135,0.35)
    earth.circle(190,0.3)
    mars.circle(280,0.24)
    jupiter.circle(350,0.15)
    saturn.circle(450,0.1)
    uranus.circle(540,0.08)
    neptune.circle(590,0.05)
#------------------------------------------------
    moon.hideturtle()              #Moon motion around Earth
    moon.goto(earth.xcor(),earth.ycor())
    moon.fd(45)
    moon.showturtle()
    moon.left(1)
    

