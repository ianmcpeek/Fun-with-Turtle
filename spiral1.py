
import turtle
import random
wn = turtle.Screen()
name = "Ian"
wn.bgcolor("lightblue")
wn.title(name + "'s Coding Dojo Python Turtle Course")
snappy = turtle.Turtle()
#spiral pattern
snappy.speed(22)
for i in range(1000):
	snappy.forward(i)
	snappy.right(98)
wn.mainloop()
