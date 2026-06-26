import pygame

class Plants:
    def __init__(self, screen: pygame.Surface,x, y, health, damage, cost, image):
        self.screen = screen
        self.x = x
        self.y = y 
        self.health = health 
        self.damage = damage
        self.cost = cost
        
    def draw(self):
        pass


    

    def hit_by_zombie(self):
        pass

class sunflower:
    def __init__(self, screen: pygame.Surface, x, y, health, cost, image):
        self.screen = screen
        self.x = x 
        self.y = y 
        self.health = 6
        self.cost = 50

class peashooter:
    def __init__(self, screen: pygame.Surface, x, y, health, cost, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.health = 6
        self.cost = 100

class wallnut: 
    def __init__(self, screen: pygame.Surface, x, y, health, cost, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.health = 32
        self.cost = 50
class cherrybomb:
    def __init__(self, screen: pygame.Surface, x, y, cost, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.cost = 150