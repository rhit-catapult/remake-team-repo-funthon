import random
import Zombies_spawn_module


class Zombie_wave:
    def __init__(self, screen): 
        self.screen = screen
        self.zombies = []
        self.random_chance = 0
        self.spawn_rate = 1
        self.spawn_rate_increase = 2.01

    def spawn_chance(self, juice):
        self.random_chance = random.uniform (0 + juice, 60 + juice)
        if self.random_chance <= 50:
            zombiespawn = Zombies_spawn_module.Zombie_spawn(self.screen, random.randint(0,4), 0, 10)
            self.zombies.append(zombiespawn)
        elif self.random_chance <= 55:
            zombiespawn = Zombies_spawn_module.Zombie_spawn(self.screen, random.randint(0,4), 2, 5)
            self.zombies.append(zombiespawn)
        elif self.random_chance <= 80:
            zombiespawn = Zombies_spawn_module.Zombie_spawn(self.screen, random.randint(0,4), 1, 28)
            self.zombies.append(zombiespawn)
        elif self.random_chance <= 100:
            zombiespawn = Zombies_spawn_module.Zombie_spawn(self.screen, random.randint(0,4), 4, 65)
            self.zombies.append(zombiespawn)
        else:
            zombiespawn = Zombies_spawn_module.Zombie_spawn(self.screen, random.randint(0,4), 3, 300)
            self.zombies.append(zombiespawn)

    def difficulty_increase(self):
        if self.spawn_rate >= 60:
            Zombie_wave.spawn_chance(self)
            self.spawn_rate = 0
        self.spawn_rate += 1**self.spawn_rate_increase

    def check(self):
        print(self.spawn_rate)
        return self.spawn_rate
    
    def remove_zombies(self):
        for k in range (len(self.zombies)-1, -1, -1):
            if self.zombies[k].need_kill:
                self.zombies.remove(self.zombies[k])