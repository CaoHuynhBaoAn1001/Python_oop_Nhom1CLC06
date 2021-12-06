from _typeshed import Self
import cmd
import sys
import os
import time 
import random
import Weapon
import Armor

class Character():
  def __init__ (self, abilityPoints:float, healthPoints:float, level:int, name:str,mana : int):
    self.__abilityPoints=abilityPoints
    self.__maxhp = healthPoints
    self.healthPoinst= self.__maxhp
    self.__level=level
    self.name=name
    self.mana = mana
  def Alive(self):
    return self.healthPoints > 0
    
  def Attack(self,character):
    if not self.Alive:
      return
    print(self.name + "attacks" + character.name)
    character.Take_damage(self.__abilityPoints)

  def Take_damage(self,points):
    self.healthPoinst -= points
    print("%s take damage %d",self.name,points)
    if(self.name == "Zombie" and self.healthPoinst <= -20):
      print(self.name + "is dead")
    if(self.name != "Zombie" and self.healthPoinst <= 0):
      print(self.name + "is dead")
    pass

  def print_info(self):
    print("{} dang co {} AP va {} HP ",format(self.name,self.__abilityPoints,self.__healthPoints))
    pass
class Warrior(Character, Weapon.Axe, Armor.ChainLink):
  def Strike(self):
    print("Strike")
  def Execute(self):
    print("Execute")
  def SkinHarden(self):
    print("SkinHarden")
class Assassin(Character,Weapon.Sword, Armor.LightLeatherVest):
  def Raze(self):
    print("Raze")
  def BleedToDeath(self):
    print("BleedToDeath")
  def Survival(self):
    print("Survival")
class Mage(Character,Weapon.Staff, Armor.ClothRobe):
  def ArcaneWrath(self):
    print("ArcaneWrath")
  def FireBall(self):
    print("FireBall")
  def Meditation(self):
    print("Meditation")
class Druid(Character, Weapon.Staff, Armor.LightLeatherVest):
  def Moonfire(self):
    print("Moonfire")
  def Starburst(self):
    print("Starburst")
  def OneWithTheNature(self):
    print("OneWithTheNature")
class Zombie(Character):
  def Alive(self):
    return self.Alive > -20
  pass
class Goblin(Character):
  def Attack(self, character):
    if(self.Alive != True):
      return
    print(self.name + "attacks" + character.name)
    Goblin_damage = random.random() > 0.5
    if(Goblin_damage == True):
      character.Take_damage(self.__abilityPoints * 3)
    else:
      character.Take_damage(self.__abilityPoints)
  pass 
class Dragon(Character):
  def __init__(self, abilityPoints: float, healthPoints: float, level: int, name: str, mana: int):
    self.abilityPoints = abilityPoints
    super().__init__(abilityPoints,healthPoints,level,name,mana)
  def Attack(self, character):
    if not self.Alive:
      return
    print(self.name + "attack" + character.name)
    Dragon_damage = random.random() > 0.5
    if(Dragon_damage == True):
      character.Take_damage(self.abilityPoints * 3)
    else:
      character.Take_damage(self.abilityPoints)

class Battle():
  def do_battle(self,hero,monster):
    print(hero.name + " vs " + monster.name)
    while hero.Alive() and monster.Alive():
      #hero.print_info()
      #monster.print_info()
      print("------------")
      print("Select ")
      print("1: Fight")
      print("2: Do nothing")
      print("3: Flee")
      #input = int(input())
      #if(input == 1):
hero.Attack(monster)
      #elif(input == 2):
        #pass
      #elif(input == 3):
        #print("Goodbye")
        #exit(0)
      monster.Attack(hero)
    if(hero.Alive):
      print("You win")
      return True
    else:
      print("You lost")
      return False
warrior = Warrior(10,50,3,"warror",30)
dragon = Dragon(2,15,1,"rong",20)
battle_vs = Battle()
hero_won = battle_vs.do_battle(warrior,dragon)
if not hero_won:
  print("You lost")
else:
  print("You win")