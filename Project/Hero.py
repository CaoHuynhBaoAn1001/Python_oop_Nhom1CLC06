#RPG_Games 
import random
from random import choices
import time
import Weapon
import Armor
from abc import ABC, abstractmethod

class Character(ABC):
	def __init__ (self, abilityPoints:float, faction:str, healthPoints:float, level:int, name:str, mana:int):
		self.abilityPoints=abilityPoints
		self.faction= faction
		self.__maxhp=healthPoints
		self.healthPoints=self.__maxhp
		self.__level=level
		self.name=name
		self.mana=mana
	@abstractmethod
	def Alive(self):
		pass
	@abstractmethod
	def Attack(self):
		pass
	@abstractmethod
	def Take_damage(self):
		pass
	@abstractmethod
	def print_status(self):
		pass

class Warrior(Character, Weapon.Axe, Armor.ChainLink):
	def Strike(self):
		print("Strike")
	def Execute(self):
		print("Execute")
	def SkinHarden(self):
		print("SkinHarden")	
	def Alive(self):
		return self.healthPoints>0
	def Attack(self,character):
		if not self.Alive():
			return
		print(self.name + " attacks " + character.name)
		character.Take_damage(self.abilityPoints)
	def Take_damage(self,points):
		self.healthPoints -= points
		print(self.name + " take damage "+ str(points))
		if(self.name == "Zombie" and self.healthPoints <= -20):
			print(self.name + "is dead")
		if(self.name != "Zombie" and self.healthPoints <= 0):
			print(self.name + "is dead")
	def print_status(self):
		print(self.name +" has " + str(self.abilityPoints) + " AP  and " + str(self.healthPoints) + "HP")
class Assassin(Character,Weapon.Sword, Armor.LightLeatherVest):
	def Raze(self):
		print("Raze")
	def BleedToDeath(self):
		print("BleedToDeath")
	def Survival(self):
		print("Survival")
	def Alive(self):
		return self.healthPoints>0
	def Attack(self,character):
		if not self.Alive():
			return
		print(self.name + " attacks " + character.name)
		character.Take_damage(self.abilityPoints)
	def Take_damage(self,points):
		self.healthPoints -= points
		print(self.name + " take damage "+ str(points))
		if(self.name == "Zombie" and self.healthPoints <= -20):
			print(self.name + "is dead")
		if(self.name != "Zombie" and self.healthPoints <= 0):
			print(self.name + "is dead")
	def print_status(self):
		print(self.name +" has " + str(self.abilityPoints) + " AP  and " + str(self.healthPoints) + "HP")
class Mage(Character,Weapon.Staff, Armor.ClothRobe):
	def ArcaneWrath(self):
		print("ArcaneWrath")
	def FireBall(self):
		print("FireBall")
	def Meditation(self):
		print("Meditation")
	def Alive(self):
		return self.healthPoints>0
	def Attack(self,character):
		if not self.Alive():
			return
		print(self.name + " attacks " + character.name)
		character.Take_damage(self.abilityPoints)
	def Take_damage(self,points):
		self.healthPoints -= points
		print(self.name + " take damage "+ str(points))
		if(self.name == "Zombie" and self.healthPoints <= -20):
			print(self.name + "is dead")
		if(self.name != "Zombie" and self.healthPoints <= 0):
			print(self.name + "is dead")
	def print_status(self):
		print(self.name +" has " + str(self.abilityPoints) + " AP  and " + str(self.healthPoints) + "HP")
class Druid(Character, Weapon.Staff, Armor.LightLeatherVest):
	def Moonfire(self):
		print("Moonfire")
	def Starburst(self):
		print("Starburst")
	def OneWithTheNature(self):
		print("OneWithTheNature")
	def Alive(self):
		return self.healthPoints>0
	def Attack(self,character):
		if not self.Alive():
			return
		print(self.name + " attacks " + character.name)
		character.Take_damage(self.abilityPoints)
	def Take_damage(self,points):
		self.healthPoints -= points
		print(self.name + " take damage "+ str(points))
		if(self.name == "Zombie" and self.healthPoints <= -20):
			print(self.name + "is dead")
		if(self.name != "Zombie" and self.healthPoints <= 0):
			print(self.name + "is dead")
	def print_status(self):
		print(self.name +" has " + str(self.abilityPoints) + " AP  and " + str(self.healthPoints) + "HP")
class Goblin(Character):
	def Alive(self):
		if (self.healthPoints>0):
			return True
		else:
			return False
	def Attack(self, character):
		if not self.Alive:
				return
		print(self.name + " attacks " + character.name)
		character.Take_damage(self.abilityPoints * (random.randint(110,130)/100))
	def Take_damage(self,points):
		self.healthPoints -= points
		print(self.name + " take damage "+ str(points))
		if(self.name == "Zombie" and self.healthPoints <= -20):
			print(self.name + "is dead")
		if(self.name != "Zombie" and self.healthPoints <= 0):
			print(self.name + "is dead")
	def print_status(self):
		print(self.name +" has " + str(self.abilityPoints) + " AP  and " + str(self.healthPoints) + "HP")
class Zombie(Character):
	def Alive(self):
		if (self.healthPoints>-20):
			return True
		else:
			return False
	def Attack(self, character):
		if not self.Alive:
			return
		print(self.name + " attacks " + character.name)
		character.Take_damage(self.abilityPoints)
	def Take_damage(self,points):
		self.healthPoints -= points
		print(self.name + " take damage "+ str(points))
		if(self.name == "Zombie" and self.healthPoints <= -20):
			print(self.name + "is dead")
		if(self.name != "Zombie" and self.healthPoints <= 0):
			print(self.name + "is dead")
	def print_status(self):
		print(self.name +" has " + str(self.abilityPoints) + " AP  and " + str(self.healthPoints) + "HP")
class Dragon(Character):	
	def Alive(self):
		if (self.healthPoints>0):
			return True
		else:
			return False
	def Attack(self, character):
		if not self.Alive:
			return
		print(self.name + " use FireBall to " + character.name)
		character.Take_damage(self.abilityPoints * (random.randint(140,160)/100))
	def Take_damage(self,points):
		self.healthPoints -= points
		print(self.name + " take damage "+ str(points))
		if(self.name == "Zombie" and self.healthPoints <= -20):
			print(self.name + "is dead")
		if(self.name != "Zombie" and self.healthPoints <= 0):
			print(self.name + "is dead")
	def print_status(self):
		print(self.name +" has " + str(self.abilityPoints) + " AP  and " + str(self.healthPoints) + "HP")
class Battle():
	def do_battle(self, hero, enemy):
		print ("You face "+ enemy.name)
		print(hero.name + " vs " + enemy.name)
		while hero.Alive() and enemy.Alive():
			hero.print_status()
			enemy.print_status()
			print ("What do you want to do?")
			print ("1. fight %s" % enemy.name)
			print ("2. do nothing")
			print ("3. run")
			print ("> "),
			n = int(input())
			if n == 1:
				hero.Attack(enemy)
				enemy.Attack(hero)
			elif n == 2:
				pass
			elif n == 3:
				print ("Goodbye.")
				exit(0)
			else:
				print ("Invalid input %r" % n)
				continue
		if hero.Alive():	
			print ("You defeated the %s" % enemy.name)
			return True
		else:
			print ("YOU LOSE!")
			return False
enemies =[Dragon(15,"Boss",200,10,"Dragon",30),Zombie(5,"Zombie",50,2,"Zom",5), Goblin(7,"Goblin",60,3,"Goblin",7)]
battle_engine=Battle()

while(True):
	print("-------------------")
	print("Welcome to RPG Game")
	print("-------------------")
	time.sleep(1.5)
	print("Choose 1 of 4 Class")
	print("1 : Warrior")
	print("2 : Assassin")
	print("3 : Mage")
	print("4 : Druid")
	time.sleep(1.5)
	n = int(input())
	if(n == 1):
		hero = Warrior(40,"Melee",160,1,"Warrior",10)
	elif n == 2:
		hero = Assassin(50,"Melee",80,1,"Assassin",10)
	elif n == 3:
		hero = Mage(30,"Spellcaster",150,1,"Mage",20)
	elif n == 4:
		hero = Druid(20,"Spellcaster",200,1,"Druid",25)
	for i in random.choices(enemies):
		hero_won = battle_engine.do_battle(hero, i)
		if not hero_won:
			print("YOU LOSE!")
			exit(0)
	exit(0)
print("YOU WIN!!")