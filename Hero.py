#RPG_Games 
import random
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
		print(self.name +" dang co " + str(self.abilityPoints) + " AP  va " + str(self.healthPoints) + "HP")
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
		print(self.name +" dang co " + str(self.abilityPoints) + " AP  va " + str(self.healthPoints) + "HP")
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
		print(self.name +" dang co " + str(self.abilityPoints) + " AP  va " + str(self.healthPoints) + "HP")
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
		print(self.name +" dang co " + str(self.abilityPoints) + " AP  va " + str(self.healthPoints) + "HP")
class Goblin(Character):
	def Alive(self):
		if (self.healthPoints>0):
			return True
		else:
			return False
	def Attack(self, character):
		if (self.Alive != True):
			return
		print(self.name + " attacks " + character.name)
		Goblin_damage = random.random() > 0.5
		if(Goblin_damage == True):
			character.Take_damage(self.abilityPoints * 3)
		else:
			character.Take_damage(self.abilityPoints)
	def Take_damage(self,points):
		self.healthPoints -= points
		print(self.name + " take damage "+ str(points))
		if(self.name == "Zombie" and self.healthPoints <= -20):
			print(self.name + "is dead")
		if(self.name != "Zombie" and self.healthPoints <= 0):
			print(self.name + "is dead")
	def print_status(self):
		print(self.name +" dang co " + str(self.abilityPoints) + " AP  va " + str(self.healthPoints) + "HP")
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
		print(self.name +" dang co " + str(self.abilityPoints) + " AP  va " + str(self.healthPoints) + "HP")
class Dragon(Character):	
	def Alive(self):
		if (self.healthPoints>0):
			return True
		else:
			return False
	def Attack(self, character):
		if (self.Alive != True):
			return
		print(self.name + " attacks " + character.name)
		Dragon_damage = random.random() > 0.4
		if(Dragon_damage == True):
			character.Take_damage(self.abilityPoints * 5)
		else:
			character.Take_damage(self.abilityPoints)
	def Take_damage(self,points):
		self.healthPoints -= points
		print(self.name + " take damage "+ str(points))
		if(self.name == "Zombie" and self.healthPoints <= -20):
			print(self.name + "is dead")
		if(self.name != "Zombie" and self.healthPoints <= 0):
			print(self.name + "is dead")
	def print_status(self):
		print(self.name +" dang co " + str(self.abilityPoints) + " AP  va " + str(self.healthPoints) + "HP")
class Battle():
	#def Alive(self):
		#return self.healthPoints>0
	def do_battle(self, hero, enemy):
		#print ("Hero faces the %s" % enemy.name)
		print(hero.name + " vs " + enemy.name)
		while hero.Alive() and enemy.Alive():
			hero.print_status()
			enemy.print_status()
			print ("What do you want to do?")
			print ("1. fight %s" % enemy.name)
			print ("2. do nothing")
			print ("3. flee")
			print ("> "),
			n = int(input())
			if n == 1:
				hero.Attack(enemy)
			elif n == 2:
				pass
			elif n == 3:
				print ("Goodbye.")
				exit(0)
			else:
				print ("Invalid input %r" % n)
				continue
			enemy.Attack(hero)
		if hero.Alive():	
			print ("You defeated the %s" % enemy.name)
			return True
		else:
			print ("YOU LOSE!")
			return False

#hero = ['Warrior(10,"Melee",100,1,"Wa",10)','Assassin(15,"Melee",80,1,"Assa",10)','Mage(20,"Spellcaster",70,1,"Magee",20)','Druid(20,"Spellcaster",70,1,"Dru",25)']
hero = Warrior(50,"Melee",100,1,"Wa",10)
enemies = [Dragon(15,"Boss",200,10,"Dra",30),Zombie(5,"Zombie",50,2,"Zom",5), Goblin(7,"Goblin",60,3,"Goblin",7)]
battle_engine=Battle()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print("YOU LOSE!")
        exit(0)
print ("YOU WIN!")