import turtle as t

def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1, 3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()
    t.speed('very-slow')
    t.bgcolor('Dodger Blue')

def arm(color):
    t.pendown()
    t.begin_fill()
    t.color(color)
    t.forward(60)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(10)
    t.end_fill()
    t.penup()
    t.setheading(0)

# Feet
t.goto(-100, -150)    
rectangle(50, 20, 'blue')
t.goto(-30, -150)
rectangle(50, 20, 'blue')

# Legs
t.goto(-25, -50)
rectangle(15, 100, 'grey')
t.goto(-55, -50)
rectangle(-15, 100, 'grey')

# Body
t.goto(-90, 100)
rectangle(100, 150, 'red')

# Arms
t.goto(-90, 85)
#t.goto(-150, 70)
t.setheading(180)
arm('light blue')
# rectangle(60, 15, 'grey')
t.goto(-90, 20)
#t.goto(-150, 110)
t.setheading(180)
arm('purple')
#rectangle(15, 40, 'grey')

t.goto(10, 70)
rectangle(60, 15, 'grey')
t.goto(55, 110)
rectangle(15, 40, 'grey')

# Neck
#t.goto(-50, 120)
#rectangle(15, 20, 'grey')
t.goto(10, 85)
t.setheading(0)
arm('goldenrod')

# Head
t.goto(-85, 170)
rectangle(80, 50, 'red')

# Eyes
t.goto(-60, 160)
rectangle(30, 10, 'white')
#t.goto(-55, 155)
t.goto(-60, 160)
rectangle(5, 5, 'black')
#t.goto(-40, 155)
t.goto(-45, 155)
rectangle(5, 5, 'black')

# Mouth
t.goto(-65, 135)
t.right(5)
rectangle(40, 5, 'black')

t.hideturtle()