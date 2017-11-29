from turtle import *
class Hexagon(Turtle):
	def __init__(self,size):
	    Turtle.__init__(self)
	    self.shapesize(size)
	    self.begin_poly()
	    for i in range(6):
	    	self.forward(10)
	    	self.right(60)
	    self.end_poly()
	    j = self.get_poly()
	    register_shape = ("my best shape",j)
Hexagon = Hexagon(10)	    




import random
colormode(255)
class Polygon(Turtle):
	def __init__(self,lines):
		Turtle.__init__(self)
		self.lines = lines
		self.begin_poly()
		for i in range (lines):
			self.forward(10)
			self.right(360/lines)
		self.end_poly()
		n = self.get_poly()
		register_shape = ("my fav shape",n)
	def random_color(self):
		r = random.randint(0,256)
		g = random.randint(0,256)
		b = random.randint(0,256)
		self.color((r,g,b))
Polygon = Polygon(10)
Polygon.random_color()	
mainloop()			






