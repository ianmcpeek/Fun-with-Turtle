import turtle
import random
wn = turtle.Screen()
name = "Ian"
wn.bgcolor("lightblue")
wn.title(name + "'s Coding Dojo Python Turtle Course")
snappy = turtle.Turtle()
snappy.speed(20)
x = 1
while x < 400:
  #define a new color with a random number in the range of 0-1 for each color spectrum
	r = random.random() 
	g = random.random()
	b = random.random()
	snappy.color(r, g, b)
	snappy.forward(50 + x)
	snappy.right(90.911)
	x = x+1 
wn.mainloop()
