from turtle import *
import turtle
import random
import time 

colormode(255)
tracer(0)
hideturtle()
screen_width = turtle.getcanvas().winfo_width()/2
screen_height =  turtle.getcanvas().winfo_height()/2
NUMBER_OF_BALLS = 5 
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MIMIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5 
BALL = []

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
		new_x = current_x + self.dx 
		current_y = self.ycor()
		new_y = current_y + self.dy
		rightside = new_x + self.radius
		leftside = new_x - self.radius
		upside = new_y + self.radius
		downside = new_y - self.radius
		self.goto(new_x,new_y)
		if current_x >= width:
			self.dx = -0.4
		if current_x <= -width:
			self.dx = 0.4
		if current_y >= height:
			self.dy = -0.3
		if current_y <= -height:
			self.dy = 0.3		
			

#for i in range(0,5):
	#Create variabes like x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS. )
	#ball=Ball(all variables)
	#list_name.append(ball)


ball = Ball(3,6,0.3,0.4,20,"blue")
ball2 = Ball(6,9,0.4,0.5,10,"yellow")
My_Ball = Ball(9,12,0.5,0.6,15,"black")
while True:
	ball.move(screen_width , screen_height)
	ball2.move(screen_width , screen_height)
	My_Ball.move(screen_width,screen_height)
	getscreen().update()

	
mainloop()