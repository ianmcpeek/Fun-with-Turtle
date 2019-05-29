import turtle
import random
wn = turtle.Screen()
name = "Ian"
wn.bgcolor("#f7f4f2")
snappy = turtle.Turtle()
snappy.speed(20)
snappy.color("#2d1b47")
x = 3
while x < 300:
  #define a new color with a random number in the range of 0-1 for each color spectrum
	snappy.forward(25 + x)
	snappy.right(125)
	x += 3
wn.mainloop()
