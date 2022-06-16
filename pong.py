import time
import turtle
import winsound

wn = turtle.Screen()
wn.title("BNHP Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


def initial_dx():
    return 0.1 if round(time.time() * 1000) % 2 == 0 else -0.1


def initial_dy():
    return -0.1 if round(time.time() * 1000) % 3 == 0 else 0.1



# paddle
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.goto(-350, 0)

# paddle_b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = initial_dx()
ball.dy = initial_dy()

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0      Player B: 0", align="center", font=("Courier", 24, "normal"))

# score
score_a = 0
score_b = 0


# Function
def paddle_a_up():
    if paddle_a.ycor() > 245:
        return
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)


def paddle_a_down():
    if paddle_a.ycor() < -245:
        return
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)


def paddle_b_up():
    if paddle_b.ycor() > 245:
        return
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)


def paddle_b_down():
    if paddle_b.ycor() < -245:
        return
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)


# Keyboard
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_a_up, "W")
wn.onkeypress(paddle_a_down, "S")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(wn.bye, "Escape")

# main loop
while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.Beep(250, 150)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

        winsound.Beep(250, 150)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = initial_dx() * -1
        score_a += 1
        for i in range(800, 40, -250):
            winsound.Beep(i, 60)
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = initial_dx() * -1
        score_b += 1
        for i in range(300, 801, 250):
            winsound.Beep(i, 60)
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    # paddle bounce
    if 350 > ball.xcor() > 340 and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        winsound.Beep(450, 150)
        ball.dx *= -1

    if -350 < ball.xcor() < -340 and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        winsound.Beep(450, 150)
        ball.dx *= -1
