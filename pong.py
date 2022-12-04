# Pong game in Phyton 3
# By AdrianPopescuPx

import turtle

window = turtle.Screen()
window.title("Pong By @AdrianPopescuPx")
window.bgcolor("#145DA0")
window.setup(width=800, height=600)
window.tracer(0) # it stopes the window from updating / it helps speed up my game

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("#2E8BC0")
paddle_a.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("#2E8BC0")
paddle_b.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("#2E8BC0")
ball.penup()
ball.goto(0, 0)

# Main game loop

while True:
    window.update()
