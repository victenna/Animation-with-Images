import turtle,time
wn=turtle.Screen()
wn.bgpic('road.gif')
t=turtle.Turtle()
t.up()
t1=turtle.Turtle()
t1.up()
turtle.tracer(2)
turtle.bgcolor('brown')

image1=['helicopter11.gif','helicopter12.gif'] 
image2=['helicopter21.gif','helicopter22.gif']
image3='boy.gif'
wn.addshape(image3)
t1.shape(image3)
t1.goto(0,400)
for i in range(2):
    wn.addshape(image1[i])
    wn.addshape(image2[i])


X=0
t.setheading(90)
def up_down(direction):
    for i in range (100):
        i1=i%2
        t.shape(image2[i1])
        t.fd(direction)
        time.sleep(0.015)
up_down(4.5)
t.setheading(0)
X=t.xcor()
q1=1
q2=0
for i in range(950):
    i1=i%2
    X=t.xcor()
    t.shape(q1*image1[i1]+abs(q2)*image2[i1])
    t.fd(q1*5+q2*5)
    time.sleep(0.02)
    if X>=480: 
        q1=0
        q2=-1
    if X<=-480: 
        q1=1
        q2=0
t.setheading(-90)        
up_down(4.5)        
    

