
import turtle
import random
wn = turtle.Screen()
snappy = turtle.Turtle()
snappy.speed(20)

snappy.pendown()
length = 200
degree = 144
while x < 10: 
	for i in range(5): 
		snappy.forward(length)
		snappy.right(degree)
	snappy.right(360/10) 
wn.mainloop()
