    
import turtle
import random
wn = turtle.Screen()
wn.bgcolor("#070707")
snappy = turtle.Turtle()
snappy.speed(20)
x = 0


snappy.pendown()
# should be determines by screen size
strokeSize = 175
strokeColors = [ '#e51b1b', '#ffffff', '#ff6600']
angle = 120
spoke = 10
decrement =  0.8
for i in range(3): 
	snappy.penup()
	snappy.color(strokeColors[i])
	snappy.pendown()
	while x < 360/3: 
	    snappy.forward(strokeSize)     
	    snappy.right(angle)
	    snappy.forward(strokeSize)
	    snappy.right(angle)
	    snappy.forward(strokeSize)
	    snappy.right(angle)

	    snappy.right(spoke)
	    x = x+3 # adds 1 to the value of x,
	strokeSize *= decrement
	x = 0
wn.mainloop()
