import pygame, Button_module

class start_screen:
    def __init__(self, screen: pygame.surface):
        self.screen = screen
        self.font = pygame.font.SysFont("arialrounded", 42)
        self.caption_1 = self.font.render("start game?", True, (255,255,255), (0,0,0))
        self.caption_2 = self.font.render("You died", True, (255,255,255), (0,0,0))


        

    def draw_start(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.caption_1,(500-self.caption_1.get_width()/2, 
                                         325-self.caption_1.get_height() - 0.1*self.screen.get_height()))

    def draw_end(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.caption_2,(500- self.caption_2.get_width()/2,
                                         325 - self.caption_2.get_height() - 0.1*self.screen.get_height()))