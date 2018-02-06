from turtle import *
import turtle
import random
import time 
import math
colormode(255)
tracer(0)
hideturtle()
RUNNING = True
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT =  turtle.getcanvas().winfo_height()/2
NUMBER_OF_BALLS = 5 
MINIMUM_BALL_r = 10
MAXIMUM_BALL_r = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5 
Balls = []



TIME_FONT_SIZE = 15
TIME_FONT_TYPE = "bold"
TIME_FONT_NAME = "Helvetica"
TIME_COLOR = "black"

WRITE_FONT_SIZE = 150
WRITE_FONT_TYPE = "bold"
WRITE_FONT_NAME = "Helvetica"
WRITE_COLOR = "blue"

SCORE_COLOR = "blue"


writeToScreeen = turtle.clone()
writeToScreeen.ht()
writeToScreeen.color(WRITE_COLOR)


scoreWrite = turtle.clone()
scoreWrite.color(SCORE_COLOR)
scoreWrite.ht()

timeWrite = turtle.clone()
timeWrite.color(SCORE_COLOR)
timeWrite.ht()
timeScore = 0 









class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.dx = dx 
		self.dy = dy 
		self.shape("circle")
		self.shapesize(r/10)
		self.r = r 
		self.color(color) 
   
	def move(self,width,height):
		current_x = self.xcor()
		new_x = current_x + self.dx 
		current_y = self.ycor()
		new_y = current_y + self.dy
		rightside = new_x + self.r
		leftside = new_x - self.r
		upside = new_y + self.r
		downside = new_y - self.r
		self.goto(new_x,new_y)
		if current_x >= width:
			self.dx = -0.4
		if current_x <= -width:
			self.dx = 0.4
		if current_y >= height:
			self.dy = -0.3
		if current_y <= -height:
			self.dy = 0.3		
			
MY_BALL = Ball(5, 10, 0, 0, 20, "red")
for i in range(NUMBER_OF_BALLS):

	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_r , SCREEN_WIDTH - MAXIMUM_BALL_r)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_r , SCREEN_HEIGHT - MAXIMUM_BALL_r)
	dx = random.randint( MINIMUM_BALL_DX, MAXIMUM_BALL_DX )
	dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	r =random.randint(MINIMUM_BALL_r,MAXIMUM_BALL_r) 	
	color=(random.randint(0,255),random.randint(0,255), random.randint(0,255))
	ball = Ball(x,y,dx,dy,r,color)
	Balls.append(ball)
 	
def collide(ball_a , ball_b):
	if ball_a==ball_b:
		return False
	
	x1 = ball_a.xcor()
	x2 = ball_b.xcor()
	y1 = ball_a.ycor()
	y2 = ball_b.ycor()
	d=math.sqrt(math.pow(x1 - x2,2) + math.pow(y1 - y2,2))	

	if d <= (ball_a.r + ball_b.r):
		return True 
	else:
		return False	





	# r_sum=ball_a.r+ball_b.r
	# center_sum=math.sqrt(math.pow(ball_b.xcor() - ball_a.xcor(),2) + math.pow(ball_b.ycor()) - ball_a.xcor())
	# if center_sum+10 <= r_sum:
	# 	return True 
	# else:
	# 	return False
def check_all_balls_collision():
	for ball_a in Balls:
		for ball_b in Balls:
			if  collide (ball_a,ball_b):

				
				

				x2 = random.randint (-SCREEN_WIDTH + MAXIMUM_BALL_r , SCREEN_WIDTH - MINIMUM_BALL_r)
				y2 = random.randint (-SCREEN_HEIGHT + MAXIMUM_BALL_r , SCREEN_HEIGHT - MINIMUM_BALL_r )
				x_speed = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				y_speed = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
				while x_speed == 0:
					x_speed  = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				while y_speed  == 0:
					y_speed = random.randint(MINIMUM_BALL_DY ,MAXIMUM_BALL_DY )
				r2 = random.randint(MINIMUM_BALL_r,MAXIMUM_BALL_r)
				color2 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))


				if ball_a>ball_b:
					ball_b.r = r2
					ball_b.shapesize(ball_b.r/10)
					ball_b.color = color2
					ball_b.goto(x2,y2)
					ball_b.dx = x_speed
					ball_b.dy = y_speed
					ball_a.r = ball_a.r +1
					ball_a.shapesize(ball_a.r/10)
				else:
					ball_a.r = r2 
					ball_a.shapesize(ball_a.r/10)
					ball_a.color = color2 
					ball_a.goto(x2,y2)
					ball_a.dx = x_speed
					ball_a.dy = y_speed
					ball_b.r = ball_b.r + 1
					ball_b.shapesize(ball_b.r/10)


def check_myball_collision():
	for i in Balls:
		if collide (MY_BALL,i) == True:
			x2 = random.randint (-SCREEN_WIDTH + MAXIMUM_BALL_r , SCREEN_WIDTH - MINIMUM_BALL_r)
			y2 = random.randint (-SCREEN_HEIGHT + MAXIMUM_BALL_r , SCREEN_HEIGHT - MINIMUM_BALL_r )
			x_speed = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
			y_speed = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
			r2 = random.randint(MINIMUM_BALL_r,MAXIMUM_BALL_r)
			color2 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

			x_speed2 = 1
			while x_speed2 == 0:
				x_speed2 = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
			y_speed2 = 1
			while y_speed2 == 0:
				y_speed2 = random.randint(MINIMUM_BALL_DY ,MAXIMUM_BALL_DY )
 

			if MY_BALL.r > i.r:
				i.r = r2
				i.shapesize(i.r/10)
				i.color = color2
				i.goto(x2,y2)
				i.dx = x_speed2
				i.dy = y_speed2
				MY_BALL.r = ball_a.r +1
				MY_BALL.shapesize(MY_BALL.r/10)
			
			else:
				return False

	return True 


def move_around(event):
	Xcoor =  event.x - SCREEN_WIDTH
	Ycoor =  SCREEN_HEIGHT - event.y
	MY_BALL.goto(Xcoor ,Ycoor)

getcanvas().bind("<Motion>", move_around)
getscreen().listen()


# ball = Ball(3,6,0.3,0.4,20,"blue")
# ball2 = Ball(6,9,0.4,0.5,10,"yellow")
# My_Ball = Ball(9,12,0.5,0.6,15,"black")
# while True:
	# ball.move(SCREEN_WIDTH , SCREEN_HEIGHT)
	# ball2.move(SCREEN_WIDTH , SCREEN_HEIGHT)
	# My_Ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
	# getscreen().update()
	#if ball.pos() <= SCREEN_HEIGHT
	#circle.move(-3 , )	



def move_all_balls():
	for i in Balls:
		i.move(SCREEN_WIDTH, SCREEN_HEIGHT)
	

def creaetefood():
	iscreateFood = random.random()

	if iscreateFood < 0.2 and len (FOOD) < MAX_FOOD_NUM:
		x = random.randint(-SCREEN_WIDTH + MAX_FOOD_radius ,SCREEN_WIDTH  - MAX_FOOD_radius)
		y = random.randint(-SCREEN_HEIGHT + MAX_FOOD_radius , SCREEN_HEIGHT - MAX_FOOD_radius)
		radius = random.randint(MIN_FOOD_RADIUS , MAX_FOOD_radius)
		color = (random.randint(0,225), random.randint(0,225), random.randint(0,225))

		food = Ball(x,y,0,0,radius,color) 
		FOOD.append(food)


def timerDisplay():
	global timeScore
	timeScore = int(time.clock() * 1.5)
	timeWrite.goto(-SCREEN_WIDTH +10, SCREEN_HEIGHT - 30)
	timeWrite.clear()
	timeWrite.write("Time: " + str(timeScore), False, "left", (TIME_FONT_NAME, TIME_FONT_SIZE, TIME_FONT_TYPE)





while RUNNING:
	if SCREEN_WIDTH != getcanvas().winfo_width()/2:
		SCREEN_WIDTH = getcanvas().winfo_width()/2

	elif SCREEN_HEIGHT != getcanvas().winfo_height()/2:
		SCREEN_HEIGHT = getcanvas().winfo_height()/2


	move_all_balls()
	check_all_balls_collision()
	MY_BALL.move(SCREEN_WIDTH , SCREEN_HEIGHT)
	if check_myball_collision() == False:
		RUNNING = False
		
	else:
	 	RUNNING = True



	getscreen().update()
	time.sleep(0.01)










	