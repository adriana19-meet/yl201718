from turtle import *
import random
import time 

colormode(255)
#tracer(0)
hideturtle()
screen_width = turtle.getcanvas().winfo_width()/2
screen_height =  turtle.getcanvas().winfo_height()/2

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,radius,color):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.dx = dx 
		self.dy = dy 
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius 
		self.color(color) 
   
	def move(self,width,height):
		current_x = self.xcor()
		new_x = current_x = dx 
		current_y = self.ycor()
		new_y = current_y = dy
		rightside = new_x + self.radius
		leftside = new_x - self.radius
		upside = new_y + self.radius
		downside = new_y - self.radius
		self.goto(new_x,new_y)



ball=Ball(3,6,9,12,22,"blue")
ball2=Ball(6,9,12,15,20,"yellow")
mainloop()