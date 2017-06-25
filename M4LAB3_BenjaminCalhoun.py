import turtle

wn = turtle.Screen()


wn.bgcolor("lightblue")
wn.title("Snowflakes")

kyle = turtle.Turtle()

kyle.color("darkblue")
kyle.pensize(1)

matt = turtle.Turtle()

kyle.penup()
kyle.forward(90)
kyle.left(90)
kyle.pendown()

def branch():
    for i in range(3):
        for i in range(3):
          kyle.forward(30)
          kyle.backward(30)
          kyle.right(45)
    kyle.left(90)
    kyle.backward(30)
    kyle.left(45)
kyle.right(90)
kyle.forward(90)


for i in range(8):
  branch()
  kyle.left(45)

wn.mainloop()
