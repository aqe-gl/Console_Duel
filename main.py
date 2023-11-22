import random


class Enemy:
    def __init__(self, name, health, attack):
        self.health = health
        self.attack = attack
        self.name = name

    def be_attacked(self, damage):
        self.health = self.health - damage
        print(f'{self.name} received {damage}')


class User(Enemy):
    def __init__(self, name, health, attack, armour = 10):
        super().__init__(name, health, attack)
        self.max_health = health
        self.armour = armour

    def heal(self):
        if not self.health >= self.max_health:
            health = self.health // 10
            self.health += health
            print(f'you have installed {health} health. Your health now is {self.health}')
        else:
            print('impossible to add extra health')

    def be_attacked(self, damage):
        self.health = self.health - (damage - self.armour)
        print(f'{self.name} received {damage}')

enemy = Enemy(name='thief', health=random.randint(50, 300), attack=random.randint(15, 70))
enemy_2 = Enemy(name='wizard', attack=random.randint(15, 70), health=random.randint(50, 300))
enemy_3 = Enemy(name='kidnapper', attack=random.randint(75, 450), health=random.randint(5, 50))
enemies = [enemy, enemy_2, enemy_3]
random_enemy = random.choice(enemies)

print(f'your enemy is {random_enemy.name}')

user = User(name='nick', attack=random.randint(15, 70), health=random.randint(50, 300))

hit = 0

while True:
    print(f'your health is {user.health}, your attack is {user.attack}, your armour is {user.armour}')
    print(f'enemy\'s health is {random_enemy.health}, enemy\'s attack is {random_enemy.attack}')

    user_input = input('\n Choose action:\n 1 - increase health\n 2 - attack\n 3 - increase armour\n')
    if user_input == "1":
        user.heal()
    elif user_input == "2":
        random_enemy.be_attacked(user.attack)
    elif user_input == "3":
        user.armour += 10


    user.be_attacked(random_enemy.attack)


    if user.health <= 0 and random_enemy.health <= 0:
        print('draw')
        break
    elif user.health <= 0:
        print('You lose!')
        break
    elif random_enemy.health <= 0:
        print('You won!')
        break


'''print(f'fighter one has {enemy.health} health and {enemy.attack} attack')
print(f'fighter two has {enemy_2.health} health and {enemy_2.attack} attack')

while True:
    if enemy.health <= 0 and enemy_2.health <= 0:
        print('draw')
        break

    elif enemy.health <= 0:
        print(f'the second one won.\nhe had health {enemy_2.health}')
        break
    elif enemy_2.health <= 0:
        print(f'the first one won.\nhe had health {enemy.health}')
        break
    enemy.be_attacked(enemy_2.attack)
    enemy_2.be_attacked(enemy.attack)
    hit += 1
    print(hit, enemy.health, enemy_2.health)'''



