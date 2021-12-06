class Person:
	def __init__ (self,para_name):
		self.name=para_name
	def showInfo(self):
		print(self.name)
	def Run(self):
		print("Running...")
	pass

class Student(Person):
	def __init__ (self,para_name,para_age,para_height:float):
		#Goi den Constructor cua lop cha de gan gia tri vao thuoc tinh "name"
		super().__init__ (para_name)
		self.age=para_age
		self.height=para_height
	#Override phuong thuc cung ten cua lop cha
	def showInfo(self):
		print("Im {}".format(self.name))
		print("Im {}".format(self.age))
		print("Height {}".format(self.height))
	def Run(self): #cach goi method Run cua lop cha
		Person.Run(self)
	pass
A=Student("Bao","18","1.7")
A.showInfo()
A.Run()







