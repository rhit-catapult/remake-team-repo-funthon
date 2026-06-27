import pygame
import sys
import random
import time
import Zombies_spawn_module
import project

class Zombie_wave:
    def __init__(self): 
        self.start_time = project.start_time #TODO start time has to be a time.pef_counter() when the start button is clicked
        self.zombies = []
        self.likely_hood = 500000 #TODO find a good value for this so that zombie spawning ramps up well
    
    def spawn_chance(self):
        elapsed_time = time.perf_counter() - self.start_time
        if random.randint(elapsed_time ** 1/2, self.likely_hood):
            #TODO summon zombie type based on spawn code
