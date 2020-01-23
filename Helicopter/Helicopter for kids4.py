import turtle,time
wn=turtle.Screen()
wn.bgpic('road.gif')
t=turtle.Turtle()
t.up()
turtle.tracer(2)
turtle.bgcolor('brown')
Y=0
dy=2

imag1=['helicopter11.gif','helicopter12.gif'] 
imag2=['helicopter21.gif','helicopter22.gif']

def helic(img):
    wn.addshape(img)
    t.shape(img)
i=0
for i in range (100):
    i1=i%2
    helic(imag1[i1])
    t.goto(0,Y)
    Y=Y+dy
    time.sleep(0.015)
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
    
  
        

