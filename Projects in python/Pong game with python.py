
#Pong game with python     (not using oops)
#use w,s and up,down arrows to move
import turtle  # using turtle module to add graphics 

#Creating a screen/window
wn=turtle.Screen()
wn.title("Pong by Anmol Tuteja")
wn.bgcolor("Black")
wn.setup(width=800, height=600) #want to change size of window
wn.tracer(0) #stops the window from updating , so we are manually updating

#score 
score_a=0
score_b=0



    #Add PaddleA, PaddleB , Ball

#Paddle A
paddle_a=turtle.Turtle()   #Turtle object t--module name , T--class name
paddle_a.speed(0)  #Not the speed of paddle to move on screen but speed of animation
paddle_a.shape("square") #Giving our paddle a shape
paddle_a.color("orange")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)  #by default len,wid were 20px now we are stretching width by 5
paddle_a.penup() #pull the pen up -- no drawing while moving
paddle_a.goto(-350,0)  #co ordinates to start



#Paddle B
paddle_b=turtle.Turtle()   #Turtle object t--module name , T--class name
paddle_b.speed(0)  #Not the speed of paddle to move on screen but speed of animation
paddle_b.shape("square") #Giving our paddle a shape
paddle_b.color("orange")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)  #by default len,wid were 20px now we are stretching width by 5
paddle_b.penup() #pull the pen up -- no drawing while moving
paddle_b.goto(350,0)  #co ordinates to start  #+350 as we want it to be on right side of the game


#Ball
ball=turtle.Turtle()   #Turtle object t--module name , T--class name
ball.speed(0)  #Not the speed of paddle to move on screen but speed of animation
ball.shape("circle") #Giving our paddle a shape
ball.color("orange")
ball.penup() #pull the pen up -- no drawing while moving
ball.goto(0,0)  #co ordinates to start
ball.dx=2     #dx is dx (differentitaion)   #every times ball moves it moves by 2px
ball.dy=-2

#pen --- to keep trace of number of wins 
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle      #because we don't want to see it
pen.goto(0,260)
pen.write("Player A:0  player B:0",align="center",font=("Courier",24,"normal"))



#Fuctions
#for up,down

def paddle_a_up():
    #To update / move paddle  I need to know current y coordinates
    y=paddle_a.ycor()
    #y increses if we go up and decreases if we go down
    #so add 20
    y+=20 #add 20px to y
    paddle_a.sety(y) #sety to the new y i.e to the new y coordinate defined

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)


def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)



#Keyboard binding
wn.listen()   #listen for keyboard input 
wn.onkeypress(paddle_a_up,"w") #when user press w call the function paddle_a_up
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")




#Main Game loop
while True:
    wn.update()  #every time the loop runs , it will update the screen

    #Move the ball
    ball.setx(ball.xcor()+ball.dx)    # current x coordinate + 2px (dx)   #speed of ball move depends on computer
    ball.sety(ball.ycor()+ball.dy)


    #Border check -- what if ball hits the border
    if ball.ycor()>290:   #600 is height of window ,, so 300 up , -300 down also ball is 20px height and 20px width
       ball.sety(290)
       ball.dy *=-1 #reverses the direction of the ball



    if ball.ycor()<-290:   
       ball.sety(-290)
       ball.dy *=-1 

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a+=1 #ball is on right side of screen who will get the score
        pen.clear()  #otherwise it will print on itself
        pen.write("Player A:{}  player B:{}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))


    if ball.xcor() <- 390:
        ball.goto(0,0)
        ball.dx *=-1
        score_b+=1
        pen.clear()
        pen.write("Player A:{}  player B:{}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
#Paddle and ball collisions

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *=-1

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *=-1