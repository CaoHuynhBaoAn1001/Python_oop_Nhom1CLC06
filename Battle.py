import Hero

class Battle:
	def do_battle(self,hero,enemy):
		print("Hero face the {}".format(enemy.name))
		while hero.Alive() and enemy.Alive():
			hero.print_status()
			enemy.print_status()
