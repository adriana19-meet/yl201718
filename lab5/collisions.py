from turtle import*
import random 
class Ball(Turtle):
	def __init__(self,radius,color,speed):
		turtle.__init__(self)
		self.shape("circle")
		self.shapesize(raduis/10)
		self.raduis = raduis
		self.color = color
		self.speed = speed 

Ball1 = Ball(10,"blue", 10)
Ball2 = Ball(20,"yellow",20)

def check_collision(ball1,ball2):
	r1 = ball1.radius
	r2 = ball2.radius
	x1 = ball1.xcor() 
	x2 = ball2.xcor() 
	y1 = ball1.ycor()
	y2 = ball2.ycor()
	d =math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
	if d < (r1,+,r2)