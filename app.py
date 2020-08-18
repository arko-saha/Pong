
# Import modules

import turtle


# Create a screen

window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("steelblue")
window.setup(width=800, height=600)
window.tracer(0)


# Scores

score_a = 0
score_b = 0


# Player 1

player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape("square")
player_a.color("salmon")
player_a.shapesize(stretch_wid=5, stretch_len=1)
player_a.penup()
player_a.goto(-385, 0)


# Player 2

player_b = turtle.Turtle()
player_b.speed(0)
player_b.shape("square")
player_b.color("mediumaquamarine")
player_b.shapesize(stretch_wid=5, stretch_len=1)
player_b.penup()
player_b.goto(378, 0)


# Ping Pong Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("bisque")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.18
ball.dy = 0.18


# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Roboto", 24, "normal"))


# Functions

def player_a_up():
    y = player_a.ycor()
    y += 20
    player_a.sety(y)
    
def player_a_down():
    y = player_a.ycor()
    y -= 20
    player_a.sety(y)

def player_b_up():
    y = player_b.ycor()
    y += 20
    player_b.sety(y)
    
def player_b_down():
    y = player_b.ycor()
    y -= 20
    player_b.sety(y)

    

# Keyboard Binding

window.listen()
window.onkeypress(player_a_up, "w")
window.onkeypress(player_a_down, "s")
window.onkeypress(player_b_up, "Up")
window.onkeypress(player_b_down, "Down")

# Main Loop

while True:
    
    window.update()
    
    # Move the ball
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border Checking
    
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *=-1
        score_a +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Roboto", 24, "normal"))
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *=-1
        score_b +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Roboto", 24, "normal"))
        
    # Collision Case
        
    if ball.xcor() < -365 and ball.ycor() < player_a.ycor() + 50 and ball.ycor() > player_a.ycor() -50:
        ball.dx *= -1
 
    if ball.xcor() > 358 and ball.ycor() < player_b.ycor() + 50 and ball.ycor() > player_b.ycor() -50:
        ball.dx *= -1       
        
    # Computer Player
    
    if player_a.ycor() > ball.ycor() and abs(player_a.ycor() - ball.ycor()) > 15:
        player_a_down()
        
    elif player_a.ycor() < ball.ycor() and abs(player_a.ycor() - ball.ycor()) > 15:
        player_a_up()
        