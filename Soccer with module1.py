#Soccer with module
import turtle,time,random
from mod_soccer1 import sprite
from mod_soccer1 import shapes
from mod_scr import scr
from mod_scr import tot_number
#from mod_shotts import tot_number
wn=turtle.Screen()
wn.setup(800,800)
wn.bgpic('grass.gif')

im=[]
shapes(im)
print(im)

player=turtle.Turtle()
player.up()
wn.addshape('00.gif')
wn.addshape('03.gif')
player.shape('00.gif')
player.showturtle()
player.goto(-100,-250)
ball=turtle.Turtle()
ball.up()
ball. hideturtle()
ball.goto(170,-400)
wn.addshape('ball.gif')
ball.shape('ball.gif')

golkip=turtle.Turtle()
golkip.up()
golkip.goto(-120,80)
sprite(golkip,0,im[0])

pos=100,100
n=-1
def right():
    global n
    n=n+1
    n1=n%27
    global pos
    sprite(golkip,0,im[n1])
    golkip.fd(15)
    pos=golkip.position()
    
def left():
    global n
    n=n+1
    n1=n%27
    global pos
    sprite(golkip,0,im[n1])
    golkip.fd(-15)
    pos=golkip.position()
    
wn.onkey(left,'Left')
wn.onkey(right,'Right')
wn.listen()

turtle.tracer(1) 
delta=100             
i=-1
while True:
    ball.hideturtle()    
    ball.setheading(random.randint(40,110))
    i=i+1
    i1=i%2
    if i1==0:
        player.shape('00.gif')
        player.showturtle()
        X,Y=player.position()
        ball.setposition(X,Y+100)
        ball.hideturtle()
        time.sleep(0.2)
    if i1==1:
        player.shape('03.gif')
        p=0
        tot_number()
        for q in range(110):
            if p==0:
                ball.showturtle()
            if p==1:
                ball.hideturtle()
            ball.fd(4)
            delta=abs(ball.position()-golkip.position())
            if delta<40:
                scr()
                ball.hideturtle()   
                ball.goto(100,-150)   
                p=1
            if q==109:
                ball.hideturtle()
                ball.goto(-100,-150)
                player.shape('00.gif')
                i=-1
                
    
   
    

       
            
    
    
    
   
       
    
