import turtle

# Start filling Tai Chi with half black
turtle.begin_fill()
turtle.color("black")

# Draw a half circle
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.circle(200, 180)

# Draw the middle dividing curve of Tai Chi
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()
turtle.circle(100, 180)
turtle.right(180)  # Turn 180°, and draw the other half
turtle.circle(100, -180)

turtle.end_fill()  # finishing filling Tai Chi with half black

# the other half of circle
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.circle(200, -180)

# draw the black tai chi fish eye
turtle.begin_fill()
turtle.color("white")

turtle.penup()
turtle.goto(0, 150)
turtle.pendown()
turtle.circle(50)

turtle.end_fill()  # finishing filling

# draw the black tai chi fish eye
turtle.begin_fill()
turtle.color("black")

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.circle(50)

turtle.end_fill()  # finishing filling
turtle.hideturtle()

turtle.mainloop()