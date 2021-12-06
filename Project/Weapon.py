class Weapon:
	def __init__(self,damage:float):
		self.__damage=damage
	pass

class Axe(Weapon):
	def HackNSlash():
		pass
	def Axeweapon(self):
		print("Axe")
class Hammer(Weapon):
	def Stun():
		pass
	def Hammerweapon(self):
		print("Hammer")
class Staff(Weapon):
	def Empower():
		pass
	def Staffweapon(self):
		print("Staff")
class Sword(Weapon):
	def Bloodthrist():
		pass
	def Swordweapon(self):
		print("Sword")