import turtle,time
wn=turtle.Screen()
wn.bgpic('road.gif')
t=turtle.Turtle()
t.up()
turtle.tracer(2)
turtle.bgcolor('brown')
image1=['helicopter11.gif','helicopter12.gif'] 
image2=['helicopter21.gif','helicopter22.gif']
for i in range(2):
    wn.addshape(image1[i])
    wn.addshape(image2[i])
diver=[]    
image3=['boy.gif','boy1.gif','boy2.gif', 'boy3.gif','girl.gif']

def condition(turtle):
    turtle.setheading(-90)
    if turtle.ycor()>-10:
        turtle.fd(5)
    if turtle.ycor()<-10:
            turtle.fd(0)
    
for i in range(5):
    wn.addshape(image3[i])
    diver.append(turtle.Turtle())
    diver[i].shape(image3[i])
    diver[i].up()
    diver[i].hideturtle()
    diver[i].setheading(-90)
t.setheading(90)
def up_down(step):
    global Y
    for i in range (100):
        i1=i%2
        t.shape(image1[i1])
        t.fd(step)
        Y=t.ycor()
        time.sleep(0.015)
up_down(4.5)
t.setheading(0)
s=0
q=0
q1=1
q2=0
i=0
while True:
    if q>=5 and X>=450:
        s=s+1
    if s==1:
        t.setheading(-90)
        up_down(4.5)
        Y=t.ycor()
    if s>1:
        t.goto(X,0)
        t.shape(image1[0])
    if s==0:    
        i=i+1
        i1=i%2
        X=t.xcor()
        Y=t.ycor()
        t.shape(q1*image1[i1]+abs(q2)*image2[i1])
        t.fd(q1*5+q2*5)
        time.sleep(0.02)
        if X>=480: 
            q1=0
            q2=-1
        if X<=-480: 
            q1=1
            q2=0
        for m in range(5):
            condition(diver[m])
        def h(x,y):
            global q
            global X,Y
            q=q+1
            for n in range (1,6):
                if q==n:
                    diver[n-1].goto(X,400)
                    diver[n-1].showturtle()
        wn.onclick(h)
