import pygame

class Plants:
    def __init__(self, screen: pygame.Surface,x, y, health, damage, cost, image):
        self.screen = screen
        self.x = x
        self.y = y 
        self.health = health 
        self.damage = damage
        self.cost = cost
        

    def hit_by_zombie(self):
        pass

class sunflower(Plants):
    def __init__(self, screen: pygame.Surface, x, y, health, cost, image):
        super().__init__(screen, x, y, health, damage=0, cost=cost, image=image)
        self.sun_generated = 0
        self.sun_timer = 0
        self.sun_generation_interval = 300  # Generate sun every 300 frames (~5 seconds at 60 FPS)
        self.sun_amount = 25  # Sun produced per generation

    def update(self):
        """Update sun generation timer"""
        self.sun_timer += 1
        if self.sun_timer >= self.sun_generation_interval:
            self.sun_generated += self.sun_amount
            self.sun_timer = 0
            return True  # Signal that sun was generated
        return False

    def get_sun(self):
        """Return and reset generated sun"""
        sun = self.sun_generated
        self.sun_generated = 0
        return sun

    def draw(self):
        pass


class peashooter:
    def __init__(self, screen: pygame.Surface, x, y, health, cost, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.health = 6
        self.cost = 100

    def draw():
        pass

class repeater:
    def __init__(self, screen: pygame.Surface, x, y, health, cost, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.health = 6
        self.cost = 200

    def draw():
        pass

class wallnut: 
    def __init__(self, screen: pygame.Surface, x, y, health, cost, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.health = 32
        self.cost = 50

    def draw():
        pass

class cherrybomb:
    def __init__(self, screen: pygame.Surface, x, y, cost, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.cost = 150

    def draw():
        pass