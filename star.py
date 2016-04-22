import turtle
import random
wn = turtle.Screen()
name = "Ian"
wn.bgcolor("lightblue")
wn.title(name + "'s Coding Dojo Python Turtle Course")
snappy = turtle.Turtle()
snappy.speed(20)
snappy.color("red")
snappy.pensize(5)
#star pattern
degree = 144
length = 200
snappy.speed(1)
snappy.forward(length)
snappy.right(degree)
snappy.forward(length)
snappy.right(degree)
snappy.forward(length)
snappy.right(degree)
snappy.forward(length)
snappy.right(degree)
snappy.forward(length)
wn.mainloop()
