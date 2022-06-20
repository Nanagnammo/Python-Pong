import turtle
import os

# WINDOW SETUP
wn = turtle.Screen()
wn.title('Pong by Jacopo Gentile')
wn.bgcolor('black')
wn.setup(width=800, height=600, startx= 100, starty= 100)
wn.tracer(0)

# SCORE
score_a = 0
score_b = 0

# PADDLE A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-360, 0)

# PADDLE B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 1.5
ball.dy = -1.5

# PEN
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player A  0 - 0  Player B', align='center', font=('Courier', 24, 'normal'))

# MOVING PADDLES
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# KEYBINDINGS
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')

wn.onkeypress(paddle_b_up, 'i')
wn.onkeypress(paddle_b_down, 'k')


# MAIN GAME LOOP
while True:
    wn.update()

    # MOVE BALL
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # BORDER CHECK
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system('afplay pongBounce.wav&')

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
        os.system('afplay pongBounce.wav&')

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write('Player A  {} - {}  Player B'.format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player A  {} - {}  Player B'.format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))

    # PADDLE A / WALL COLLISION
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)
    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)

    # PADDLE B / WALL COLLISION
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)
    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)

    # PADDLE / BALL COLLISION
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(330)
        ball.dx *= -1
        os.system('afplay pongBounce.wav&')

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        os.system('afplay pongBounce.wav&')

    # WIN CHECK
    if score_a == 3:
        pen.clear()
        pen.write('Player A wins!', align='center', font=('Courier', 24, 'normal'))
        ball.dx = 0
        ball.dy = 0
        wn.update()
        wn.ontimer(wn.bye, 3000)

    if score_b == 5:
        pen.clear()
        pen.write('Player B wins!', align='center', font=('Courier', 24, 'normal'))
        ball.dx = 0
        ball.dy = 0
        wn.update()
        wn.ontimer(wn.bye, 3000)
