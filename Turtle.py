import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
logo_turtle = turtle.Turtle()
logo_turtle.speed(2)

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        logo_turtle.forward(size)
        logo_turtle.right(90)

# Function to draw a circle
def draw_circle(radius):
    logo_turtle.circle(radius)

# Drawing the company logo
# Example: a simple logo with a square and a circle

# Move to the starting position
logo_turtle.penup()
logo_turtle.goto(-50, -50)
logo_turtle.pendown()

# Draw a square
logo_turtle.color("blue")
draw_square(100)

# Move to the next position
logo_turtle.penup()
logo_turtle.goto(0, 0)
logo_turtle.pendown()

# Draw a circle
logo_turtle.color("red")
draw_circle(50)

# Hide the turtle and display the window
logo_turtle.hideturtle()
screen.mainloop()
