import turtle,time
wn=turtle.Screen()
wn.bgpic('cross1.gif')
image=['01.gif','02.gif','03.gif',\
        '04.gif','05.gif','06.gif',\
        '07.gif','08.gif','09.gif',\
        '010.gif']


chipo=turtle.Turtle()
chipo.goto(-40,-275)
chipo.up()

def addshapes():
    
    for i in range(10):
        wn.addshape(image[i])
    
addshapes()
for m in range(100):
    m1=m%10
    chipo.shape(image[m1])
    chipo.fd(10)
    time.sleep(0.1)
    
    
    
