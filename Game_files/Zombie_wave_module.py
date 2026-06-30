import random
import Zombies_spawn_module


class Zombie_wave:
    def __init__(self, screen): 
        self.screen = screen
        self.zombies = []
        self.likely_hood = 500000 #TODO find a good value for this so that zombie spawning ramps up well
        self.random_chance = 0
        self.spawn_rate = 1
        self.spawn_rate_increase = 2.01

    def spawn_chance(self):
       # elapsed_time = time.perf_counter() - self.start_time
        #if random.randint(0,100) == 1: #random.randint(elapsed_time ** 2, self.likely_hood) == self.likely_hood:
        self.random_chance = random.randint(0, 99)
        if self.random_chance <= 74:
            zombiespawn = Zombies_spawn_module.Zombie_spawn(self.screen, random.randint(0,4), 0, 10)
            self.zombies.append(zombiespawn)
        if 74 < self.random_chance <= 89:
            zombiespawn = Zombies_spawn_module.Zombie_spawn(self.screen, random.randint(0,4), 1, 28)
            self.zombies.append(zombiespawn)
        if 89 < self.random_chance <= 98:
            zombiespawn = Zombies_spawn_module.Zombie_spawn(self.screen, random.randint(0,4), 2, 3)
            self.zombies.append(zombiespawn)
        if self.random_chance == 99:
            zombiespawn = Zombies_spawn_module.Zombie_spawn(self.screen, random.randint(0,4), 3, 150)
            self.zombies.append(zombiespawn)

    def difficulty_increase(self):
        if self.spawn_rate >= 60:
            Zombie_wave.spawn_chance(self)
            self.spawn_rate = 0
        self.spawn_rate += 1**self.spawn_rate_increase
        #print(self.spawn_rate)

    def check(self):
        print(self.spawn_rate)
        return self.spawn_rate
