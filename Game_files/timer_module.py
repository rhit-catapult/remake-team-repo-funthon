import pygame
class SurvivalTime:
    def __init__(self, screen):
        self.screen = screen
        self.round_start_time = 0
        self.font = pygame.font.SysFont("Arialrounded", 30)
        self.delta = 0

    def draw(self):
        minutes = self.delta // 60
        seconds = self.delta % 60
        as_image = self.font.render(f"{minutes}:{seconds:02d}", True, (255, 255, 255))
        self.screen.blit(as_image, (self.screen.get_width()-as_image.get_width()-10, 5))

    def start_round(self):
        self.round_start_time = pygame.time.get_ticks()

    def update(self):
        self.delta = (pygame.time.get_ticks() - self.round_start_time)//1000