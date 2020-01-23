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
def condition(r,images,length):
    if q==r:
        helic(images)
        t.fd(length)
    for i in range (100):
    i1=i%2
    helic(imag1[i1])
    t.goto(0,Y)
    Y=Y+dy
    time.sleep(0.015)
n=0
i=0
q=1
while True:
    X=t.xcor()
    i1=i%2
    condition(1,imag1[i1],5)
    i=i+1
    time.sleep(0.02)
    if X>=480:
        n=n+1
        q=-1
    condition(-1,imag2[i1],-5)
    if X<-480:
        q=1
        condition(1,imag1[i1],5)
        if n>=5 and X==0:
            j=0
        for i in range (100):
            j1=j%2
            helic(imag2[j1])
            j=j+1
            t.goto(0,Y)
                        Y=Y-dy
            time.sleep(0.015)
        break
