import pygame

class Pea():
    def __init__(self, screen: pygame.surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 10
        self.need_gone = False
    
    def move(self):
        self.x += self.speed

    def draw(self):
        pygame.draw.circle(self.screen,(90, 220, 90), (self.x, self.y), 10)
        pygame.draw.circle(self.screen, (170, 255, 140), (self.x, self.y), 10, width=3)
    def off_screen(self):
        return self.x > self.screen.get_width()