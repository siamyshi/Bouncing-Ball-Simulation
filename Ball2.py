import turtle

window = turtle.Screen()
window.bgcolor("white")
window.title("Bouncing Ball Simulation")

ball = turtle.Turtle()
ball.shape("square")
ball.color("black")
ball.penup()
ball.speed(0)
ball.goto(0, 200)
ball.dy = 0

gravity = 0.09

while True:
    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)
    
    if ball.ycor() < -300:
        ball.dy *= -1