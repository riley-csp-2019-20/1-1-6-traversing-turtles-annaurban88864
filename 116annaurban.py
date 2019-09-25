#   a116_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    new_color = turtle_colors.pop()
    t.color(new_color)
    my_turtles.append(t)

# pen starting point
t.penup()
startx = 0
starty = 0
t.pendown()

# makes the different lines branching off
count = 0
for t in my_turtles:
    t.penup()
    t.goto(startx, starty)
    t.pendown()
    t.right(45*count)  
    t.forward(50)
    count += 1

    # makes main line keep moving forward
    startx = startx + 50
    starty = starty + 50
    startx = t.xcor()
    starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()