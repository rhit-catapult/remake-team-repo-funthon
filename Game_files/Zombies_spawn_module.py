import pygame, random

class Zombie_spawn:
    def __init__(self, screen:pygame.surface, row, type, health):
        self.screen = screen
        self.x = 900 + random.randint(50, 150)
        self.y = row * 100
        self.type = type
        self.health = health
        self.damage = 1
        self.speed = 0
        self.add_speed = 0
        self.is_hitting_plant = False
        self.need_kill = False

    def draw(self, add_speed):
        if self.type == 0:
            #regular type zombie
            self.speed = 1.5 + add_speed
            self.screen.blit(pygame.image.load("assets/zombie.png"), (self.x, self.y))
            
        if self.type == 1:
            #cone type zombie
            self.speed = 1 + add_speed
            self.screen.blit(pygame.image.load("assets/cone head zombie.png"), (self.x, self.y))

        if self.type == 2:
            #runner type zombie
            self.speed = 7.5 +add_speed
            self.screen.blit(pygame.image.load("assets/runner.png"), (self.x, self.y))

        if self.type == 3:
            #hulk type zombie
            self.speed = 0.75 + add_speed
            self.damage = 10
            self.screen.blit(pygame.image.load("assets/hulk.png"), (self.x, self.y))

        if self.type == 4:
            #bucket type zombie
            self.speed = 1.25 + add_speed
            self.screen.blit(pygame.image.load("assets/buckethead.png"), (self.x, self.y))

    def move(self):
        self.x -= self.speed/5

    def hit_by(self, pea):
        hit_box = pygame.Rect(self.x, self.y, 25, 100)
        return hit_box.collidepoint(pea.x, pea.y)
    
    def hit_plant(self, plant):
        plant_x, plant_y = plant.get_xy()
        if self.y != plant_y:
            return False
        else:
            return self.x <= plant_x+ 100 and self.x >= plant_x - 25
    
    def exploded(self, plant):
        zombie_hit_box = pygame.Rect(self.x, self.y, 25, 100)
        plant_x, plant_y = plant.get_xy()
        plant_hit_box = pygame.Rect(plant_x - 100, plant_y - 100, 300, 300)
        return zombie_hit_box.colliderect(plant_hit_box)

    def at_end(self):
        if self.x < -80:
            return True