#mod_soccer
import turtle
wn=turtle.Screen()

def shapes(im):
    for i in range(27):
        im.append(str(i)+'.gif')

def sprite(turtle,angle,img):
    wn.addshape(img)
    turtle.shape(img)
    turtle.up()
    turtle.setheading(angle)

