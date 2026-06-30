import pygame
import random

class Zombie_spawn:
    def __init__(self, screen:pygame.surface, row, type, health):
        self.screen = screen
        self.x = 900 + random.randint(50, 150)
        self.y = row * 100
        self.type = type
        self.health = health
        self.speed = 0
    
    def draw(self):
        if self.type == 0:
            #regular type zombie
            self.speed = 1
            self.screen.blit(pygame.image.load("assets/zombie.png"), (self.x, self.y))
            
        if self.type == 1:
            #bucket type zombie
            self.speed = 0.75
            self.screen.blit(pygame.image.load("assets/buckethead.png"), (self.x, self.y))

        if self.type == 2:
            #runner type zombie
            self.speed = 5
            self.screen.blit(pygame.image.load("assets/runner.png"), (self.x, self.y))

        if self.type == 3:
            #hulk type zombie
            self.speed = 0.30
            self.screen.blit(pygame.image.load("assets/hulk.png"), (self.x, self.y))

    def move(self):
        self.x -= self.speed/5

    def hit_by(self, pea):
        hit_box = pygame.Rect(self.x, self.y, 25, 100)
        return hit_box.collidepoint(pea.x, pea.y)
    
    def at_end(self):
        if self.x < -80:
            return True