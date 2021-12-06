

class Goblin(Character):
	def Alive(self):
		if (self.ehealthPoints>-20):
			return True
		else:
			return False
	def Attack(self, character):
		if (self.Alive != True):
			return
		print(self.name + "attacks" + character.name)
		Goblin_damage = random.random() > 0.5
		if(Goblin_damage == True):
			character.Take_damage(self.__abilityPoints * 3)
		else:
			character.Take_damage(self.__abilityPoints)
		pass 
class Zombie(Enemy):
	pass
class Dragon(Enemy):
	pass
enemy=[Goblin(),Zombie(),Dragon()]

