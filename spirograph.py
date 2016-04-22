
import turtle
import random
wn = turtle.Screen()
wn.bgcolor("darkgray")
wn.title("Gravity Well")
snappy = turtle.Turtle()
snappy.speed(20)
x = 0


snappy.pendown()
l = 200
for i in range(3): 
	while x < 360: 
	    snappy.forward(l)     
	    snappy.right(120)
	    snappy.forward(l)
	    snappy.right(120)
	    snappy.forward(l)
	    snappy.right(120)

	    snappy.right(1) 
	    x = x+1 # adds 1 to the value of x,
	l *= 1.5
	x = 0
wn.mainloop()
