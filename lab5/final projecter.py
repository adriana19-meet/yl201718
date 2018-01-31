from turtle import *
import turtle
import random
import time 

colormode(255)
tracer(0)
hideturtle()
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT =  turtle.getcanvas().winfo_height()/2
NUMBER_OF_BALLS = 5 
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MIMIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5 
BALLS = []

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
			

for i in range(NUMBER_OF_BALLS):

	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint( MINIMUM_BALL_DX, MAXIMUM_BALL_DX )
	dy = random.randint(MIMIMUM_BALL_DY , MAXIMUM_BALL_DY)
	radius =random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS) 	
	color=(random.randint(0,255),random.randint(0,255), random.randint(0,255))
	ball = Ball(x,y,dx,dy,radius,color)
	BALLS.append(ball)
 	
def collide(ball_a , ball_b):
	if ball_a==ball_b:
		return False
	r_sum=ball_a.r+ball_b.r
	center_sum=math.sqrt(math.pow(ball_b.xcor() - ball_a.xcor(),2) + math.pow(ball_b.ycor()) - ball_a.xcor())
	if center_sum+10 <= r_sum:
		return True 
	else:
		return False
def check_all_balls_collision():
	for ball_a in Balls :
		for ball_b in Balls:
			if  collide (ball_a,ball_b )==True:

				ball_ar==ball_a.r
				ball+br==ball_b.r
				

				x2 = random.randint (-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MINIMUM_BALL_RADIUS)
				y2 = random.randint (-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MINIMUM_BALL_RADIUS )
				x_speed = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				y_speed = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
				while x_speed2 == 0:
					x_speed2 = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				while y_speed2 == 0:
					y_speed2 = random.randint(MINIMUM_BALL_DY ,MAXIMUM_BALL_DY )
				radius2 = random.randit(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				color2 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))


				if r_a>r_b:
					ball_b.r = radius2
					ball_b.shapesize(ball_b.r/10)
					ball_b.color = color2
					ball_b.goto(x2,y2)
					ball_b.dx = x_speed2
					ball_b.dy = y_speed2
					ball_a.r = ball_a.r +1
					ball_a.shapesize(ball_a.r/10)
				else:
					ball_a.r = radius2 
					ball_a.shapesize(ball_a.r/10)
					ball_a.color = color2 
					ball_a.goto(x2,y2)
					ball_a.dx = x_speed2
					ball_a.dy = y_speed2
					ball_b.r = ball_b
					ball_b.shapesize(ball_b.r/10)


def 							
	# Create variabes like x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS. )
	# ball=Ball(all variables)
	# list_name.append(ball)
 

ball = Ball(3,6,0.3,0.4,20,"blue")
ball2 = Ball(6,9,0.4,0.5,10,"yellow")
My_Ball = Ball(9,12,0.5,0.6,15,"black")
while True:
	# ball.move(SCREEN_WIDTH , SCREEN_HEIGHT)
	# ball2.move(SCREEN_WIDTH , SCREEN_HEIGHT)
	# My_Ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
	getscreen().update()
	#if ball.pos() <= SCREEN_HEIGHT
	#circle.move(-3 , )	

def move_all_balls():
	for i in BALLS:
		move()
	

mainloop()