import pygame

class PlantCursor:

    def __init__(self, screen: pygame.surface):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        self.screen = screen
       
        self.image_notsunnysunflower = pygame.image.load("assets/notsunnysunflower.png")
        self.image_cherrybomb = pygame.image.load("assets/cherrybomb.png")   
        self.image_peashooter = pygame.image.load("assets/peashooter.png")
        self.image_walnut = pygame.image.load("assets/walnut.png")
        self.image_gatling_pea = pygame.image.load("assets/gatling_pea.png")
        self.image_shovel = pygame.image.load("assets/shovel.png")
        self.showing_plant = ""

        
    def draw(self):
        """ Draws this sprite onto the screen. """
        
        if self.showing_plant == "sunflower":
            mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)
            self.screen.blit(self.image_notsunnysunflower, (mouse_pos_x-50, mouse_pos_y-50))
        elif self.showing_plant == "cherrybomb":
            mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)
            self.screen.blit(self.image_cherrybomb, (mouse_pos_x-50, mouse_pos_y-50))
        elif self.showing_plant == "peashooter":
            mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)
            self.screen.blit(self.image_peashooter, (mouse_pos_x-50, mouse_pos_y-50))
        elif self.showing_plant == "wallnut":
            mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)
            self.screen.blit(self.image_walnut, (mouse_pos_x-50, mouse_pos_y-50))
        elif self.showing_plant == "gatling":
            mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)
            self.screen.blit(self.image_gatling_pea, (mouse_pos_x-50, mouse_pos_y-50))
        elif self.showing_plant == "shovel":
             mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
             pygame.mouse.set_visible(False)
             self.screen.blit(self.image_shovel, (mouse_pos_x-50, mouse_pos_y-50))
            
        else:
            pygame.mouse.set_visible(True)