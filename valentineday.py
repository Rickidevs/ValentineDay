import turtle


pencere = turtle.Screen()
pencere.setup(width=600, height=600)
pencere.bgcolor("black")

pencere.title("tik-tok: Rickidev")

kaplumbaga = turtle.Turtle()
kaplumbaga.pensize(5)
kaplumbaga.hideturtle()
kaplumbaga.speed(0) 
kaplumbaga.pencolor("red") 


kaplumbaga.penup()
kaplumbaga.goto(0, -200)
kaplumbaga.pendown()
kaplumbaga.begin_fill()
kaplumbaga.left(140)
kaplumbaga.forward(224)

for i in range(200):
    kaplumbaga.right(1)
    kaplumbaga.forward(2)
kaplumbaga.left(120)

for i in range(200):
    kaplumbaga.right(1)
    kaplumbaga.forward(2)
kaplumbaga.forward(224)
kaplumbaga.end_fill()

kaplumbaga.penup()
kaplumbaga.goto(-2, -50) 
kaplumbaga.color("white")
kaplumbaga.pendown()
kaplumbaga.write("SEN", align="center", font=("Courier", 60, "normal"))


turtle.done()




