import turtle

wn = turtle.Screen()


wn.bgcolor("green")
wn.title("Initials")

kyle = turtle.Turtle()

kyle.color("red")
kyle.pensize(3)

matt = turtle.Turtle()

kyle.forward(100)
kyle.left(90)
kyle.forward(100)
kyle.left(90)
kyle.forward(100)
kyle.left(90)
kyle.forward(100)
kyle.left(180)
kyle.forward(200)
kyle.right(90)
kyle.forward(100)
kyle.right(90)
kyle.forward(100)
kyle.left(90)

kyle.penup()
kyle.forward(50)
kyle.pendown()

kyle.left(90)
kyle.forward(100)
kyle.right(90)
kyle.forward(100)
kyle.right(180)
kyle.forward(100)
kyle.left(90)
kyle.forward(200)
kyle.left(90)
kyle.forward(100)


wn.mainloop()
