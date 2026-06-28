import pygame
import random

class Zombie_spawn:
    def __init__(self, screen:pygame.surface, columns, type):
        self.screen = screen
        self.x = 900 + random.randint(0, 75)
        self.columns = columns * 100
        self.type = type
        self.heath = 0
        self.speed = 0
    
    def draw(self):
        if self.type == 0:
            #regular type zombie
            self.heath = 10
            self.speed = 1
            self.screen.blit(pygame.image.load("assets/zombie.png"), (self.x, self.columns))
            
        if self.type == 1:
            #bucket type zombie
            self.heath = 28
            self.speed = 0.75
            self.screen.blit(pygame.image.load("assets/buckethead.png"), (self.x, self.columns))

        if self.type == 2:
            #runner type zombie
            self.heath = 3
            self.speed = 5
            self.screen.blit(pygame.image.load("assets/runner.png"), (self.x, self.columns))

        if self.type == 3:
            #hulk type zombie
            self.heath = 150
            self.speed = 0.30
            self.screen.blit(pygame.image.load("assets/hulk.png"), (self.x, self.columns))

    def move(self):
        self.x -= self.speed/5

    def hit_by(self, zombie):
        hit_box = pygame.Rect(self.columns, self.x, 25, 100)
        return hit_box.collidepoint(zombie.x, zombie.y)
    
    def at_end(self):
        if self.x < -80:
            return True