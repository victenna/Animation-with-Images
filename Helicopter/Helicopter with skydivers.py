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
    
image3=['boy.gif','girl.gif','boy1.gif']
for i in range(3):
    wn.addshape(image3[i])
    
   
t1=turtle.Turtle()
t1.shape(image3[0])
t1.up()
t1.hideturtle()
t1.goto(120,400)
t1.setheading(-90)


t2=turtle.Turtle()
t2.shape(image3[1])
t2.up()
t2.hideturtle()
t2.goto(-175,400)
t2.setheading(-90)


t3=turtle.Turtle()
t3.shape(image3[2])
t3.up()
t3.hideturtle()
t3.goto(-295,400)
t3.setheading(-90)


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
#X=t.xcor()
q1=1
q2=0
q3=1




for i in range(450):
    #print(i)
   
    
    if i>=25 and t1.ycor()>-10:
        t1.showturtle()
        t1.fd(q3*2)
        if t1.ycor()<-10:
            t1.fd(0)
            

    if i>=230 and t2.ycor()>-10:
        t2.showturtle()
        t2.fd(q3*2)
        if t2.ycor()<-10:
            t2.fd(0)

    if i>=330 and t3.ycor()>-10:
        t3.showturtle()
        t3.fd(q3*5)
        if t3.ycor()<-10:
            t3.fd(0)
            
        
        
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
    

