import turtle
import random
wn = turtle.Screen()
wn.bgcolor("darkgray")
snappy = turtle.Turtle()
snappy.speed(20)
x = 0


snappy.pendown()
l = 50
for i in range(3): 
	while x < 360/3: 
	    snappy.forward(l)     
	    snappy.right(120)
	    snappy.forward(l)
	    snappy.right(120)
	    snappy.forward(l)
	    snappy.right(120)

	    snappy.right(10) 
	    x = x+3 # adds 1 to the value of x,
	l *= 1.5
	x = 0
wn.mainloop()
