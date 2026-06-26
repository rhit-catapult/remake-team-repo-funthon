import pygame

class Plants:
    def __init__(self, screen,x, y, health, damage, cost, image):
        self.screen = screen
        self.x = x
        self.y = y 
        self.health = health 
        self.damage = damage
        self.cost = cost
        
    def draw(self):
        pass


    

    def hit_by_zombie(self, health):
        pass