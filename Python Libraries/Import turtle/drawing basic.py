import turtle

# Create a turtle graphics window
window = turtle.Screen()
my_turtle = turtle.Turtle()

# Draw a simple shape
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

# Close the graphics window on click
window.exitonclick()
