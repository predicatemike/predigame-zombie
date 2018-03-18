# A Place for Gamer Customizations


def setup(player, level):
   """ setup is called for every level. this is a place to add new things. """
   background('grass')
   maze(callback=partial(image, 'stone'))

   player.keys(right = 'd', left = 'a', up = 'w', down = 's')

   weapons = import_plugin('weapons.py')
   player.take(weapons.EnergyDrink())
   player.take(weapons.Punch(call='1'))
   player.take(weapons.FlameThrower(call='2'))
   player.take(weapons.Grenade(call='3', distance=6, radius=10))
   player.take(weapons.MustardGas(call='4', distance=10, radius=20))
   player.take(weapons.AirGun(call='space'))
   player.take(weapons.MachineGun(call='5', distance=15, repeat=3))
   player.take(weapons.Landmine(call='6', delay=1))
   player.take(weapons.C4(call='7', detonate='8', distance=8, radius=10))
   player.take(weapons.NuclearBomb(call='n'))
   player.take(weapons.WallBuster())

   #wall = partial(image, 'stone')
   #player.take(WallBuilder(left='left', right='right', front='up', back='down', wall=wall))
   display('f1', 'inventory', player._inventory)

   def drink(soda, player):
      soda.destroy()
      player.energy = 10
   fill(partial(image,'sprite', size=1.0), 0.05, player, drink)

   def claim(coin, player):
      coin.destroy()
      player.wealth = 5
   fill(partial(image,'coin', size=1.0), 0.25, player, claim)

def get_blue():
   """ create a blue (friendly) actor """
   # return name of actor, grazing speed, self defense
   return 'Piggy', 2

def get_red():
   """ create a red (hostile) actor """
   # return name of actor, movement speed
   zombies = ['Zombie-1','Zombie-2','Zombie-3']
   return choice(zombies), randint(1,4)

def get_player():
   # name of player sprite (must exist in actors/ directory)
   # pick a random Soldier
   choices = ['Soldier-1', 'Soldier-2', 'Soldier-3', 'Soldier-4', 'Soldier-5',
              'Soldier-6', 'Soldier-7', 'Soldier-8', 'Soldier-9', 'Soldier-10']
   return choice(choices)
