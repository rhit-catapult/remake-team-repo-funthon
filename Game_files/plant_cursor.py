import pygame
import time
import Button_module
import sys
import Plants_module


class PlantCursor:

    def __init__(self, screen: pygame.surface):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        self.screen = screen
       
        self.image_notsunnysunflower = pygame.image.load("assets/notsunnysunflower.png")
        self.image_cherrybomb = pygame.image.load("assets/cherrybomb.png")   
        self.image_peashooter = pygame.image.load("assets/peashooter.png")
        self.image_walnut = pygame.image.load("assets/walnut.png")
        self.image_gatling_pea = pygame.image.load("assets/gatling_pea.png")
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
        else:
            pygame.mouse.set_visible(True)
        # if time.time() > self.last_hit_time + 1:
        #     self.screen.blit(self.image_no_umbrella, (self.x, self.y))
        # else:
        #     self.screen.blit(self.image_umbrella, (self.x, self.y))



def main():
    pygame.init()

    pygame.display.set_caption("plants_module")
    screen = pygame.display.set_mode((1000, 650))
    
    sun_button = Button_module.Button(screen, 115, 550, "sunflower")
    pea_button = Button_module.Button(screen, 315, 550, "peashooter")
    rep_button = Button_module.Button(screen, 500, 550, "repeater")
    wall_button = Button_module.Button(screen, 665, 550, "wallnut")
    cherry_button = Button_module.Button(screen, 850, 550, "cherry bomb")

    all_plants = []
    def plant_exists(row, col):
        return any(p.row == row and p.column == col for p in all_plants)
    
    plant_cursor = PlantCursor(screen)
    
    # sunny_mike = Sunflower(screen, 0, 0)
    # spitty_mike = Peashooter(screen, 1, 0)
    # super_spitty_mike = Gatling(screen, 2, 0)
    # dense_mike = Wallnut(screen, 3,0)
    # boom_mike = Cherrybomb(screen, 4, 0)
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if sun_button.is_clicked_by(event.pos):
                    plant_cursor.showing_plant = "sunflower"
                elif pea_button.is_clicked_by(event.pos):
                    plant_cursor.showing_plant = "peashooter"
                elif rep_button.is_clicked_by(event.pos):
                    plant_cursor.showing_plant = "gatling"
                elif wall_button.is_clicked_by(event.pos):
                    plant_cursor.showing_plant = "wallnut"
                elif cherry_button.is_clicked_by(event.pos):
                    plant_cursor.showing_plant = "cherrybomb"
                elif plant_cursor.showing_plant != "":
                    print(f"Placing {plant_cursor.showing_plant} at {event.pos}")
                    
                    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
                    row = mouse_pos_y // 100
                    col = mouse_pos_x // 100
                    # TODO: before appending, check whether a plant already exists at (row, col)
                    if plant_exists(row, col):
                        print("A plant is already at this location!")
                    else:
                        if plant_cursor.showing_plant == "sunflower":
                            all_plants.append(Plants_module.Sunflower(screen, row, col))
                        elif plant_cursor.showing_plant == "cherrybomb":
                            all_plants.append(Plants_module.Cherrybomb(screen, row, col))
                        elif plant_cursor.showing_plant == "peashooter":
                            all_plants.append(Plants_module.Peashooter(screen, row, col))
                        elif plant_cursor.showing_plant == "wallnut":
                            all_plants.append(Plants_module.Wallnut(screen, row, col))
                        elif plant_cursor.showing_plant == "gatling":
                            all_plants.append(Plants_module.Gatling(screen, row, col))
                        else:
                            pygame.mouse.set_visible(True)
                        plant_cursor.showing_plant = ""
                    # TODO: if it does, skip placement and maybe print a warning or keep selection active
                else:
                    plant_cursor.showing_plant = ""



# ------------------------------------- background code ---------------------------------------------------------
        screen.fill((90,135,72))
        line_y = -50
        line_x = -50
        dark_line = (85, 128, 68)
        dark_square = (77, 116, 62)
        square_x = -100
        square_y = 100

        for goon1000 in range(2):   #horizontal lines
            line_y += 200
            pygame.draw.line(screen, dark_line, (0, line_y), (900, line_y), 100)
            
        for goon2000 in range(4):   #vertical lines
            line_x += 200
            pygame.draw.line(screen, dark_line, (line_x, 0), (line_x, 500), 100)

        pygame.draw.line(screen, (100,100,100), (950, 0), (950, 650), 100)  #sidewalk
        pygame.draw.line(screen, (120,60,40), (0, 575), (1000, 575), 150)   #bottom bar

        for goon3000 in range(8):   #darkest squares
            square_x += 200
            pygame.draw.rect(screen, dark_square, ((square_x,square_y),(100,100)))
            if square_x >= 700:
                square_y = 300
                square_x = -100





        for goon4000 in range(4):   #placeholder slots
            break
            pygame.draw.rect(screen, (30,30,30), ((15,30), (100,100)))
            

        for plants in all_plants:
            plants.draw()
        # TODO: Add your project code
        # sunny_mike.draw()
        # spitty_mike.draw()
        # super_spitty_mike.draw()
        # dense_mike.draw()
        # boom_mike.draw()
        plant_cursor.draw()
        sun_button.draw()
        pea_button.draw()
        rep_button.draw()
        wall_button.draw()
        cherry_button.draw()
        pygame.display.update()

if __name__ == "__main__":
    main()