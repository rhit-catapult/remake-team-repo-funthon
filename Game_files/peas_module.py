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
        pygame.draw.circle(self.screen, "dark green", (self.x, self.y), 10)

    def off_screen(self):
        return self.x > self.screen.get_width()