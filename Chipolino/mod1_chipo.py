#mod1_chipo
import turtle
wn=turtle.Screen()
image=[]
#image=[0,0,0,0,0,0,0,0,0,0]
def shapes(image):
    for i in range(10):
        image.append('0'+str(i)+'.gif')
        #image[i]='0'+str(i)+'.gif'





def sprite(turtle,angle,img):
    wn.addshape(img)
    turtle.shape(img)
    turtle.up()
    turtle.setheading(angle)

#shapes(image)        
#print(image)   
    

