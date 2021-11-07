class Car:
	car_speed=200
	#class Attribute
	def __init__(self,MAX_speed):
		self.max_speed=MAX_speed + "Km/h"
		#instance attribute
	def __init__ (self,para_speed,para_color,para_type):
		self.speed=para_speed + "Km/h"
		self.color=para_color
		self.type=para_type
		#Constructor cơ bản
Lamborghini=Car("300","yellow","sport")
print(Lamborghini.type)
