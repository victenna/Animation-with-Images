#mod2_chipo
import turtle
wn=turtle.Screen()

def shapes(im):
    for m in range(10):
        im.append('0'+str(m)+'.gif')

def sprite(turtle,angle,img):
    wn.addshape(img)
    turtle.shape(img)
    turtle.up()
    turtle.setheading(angle)

#storage(im)
#print(im)
