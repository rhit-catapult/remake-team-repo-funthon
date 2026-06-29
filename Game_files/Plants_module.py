import pygame
import sys
import random
import Button_module, peas_module

class Plant:
    def __init__(self, screen: pygame.Surface,row, column, health, damage, cost, image_filename):
        self.screen = screen
        self.column = column
        self.row = row 
        self.health = health 
        self.damage = damage
        self.cost = cost
        self.image:pygame.Surface = pygame.image.load(image_filename)

    def draw(self):
        self.screen.blit(self.image, (self.column*100, self.row*100))
    
        

    def hit_by_zombie(self):
        pass

class Sunflower(Plant):
    def __init__(self, screen: pygame.Surface, row, column):
        super().__init__(screen, row, column, 6, 0, 50, "assets/notsunnysunflower.png")
        self.images = [
            pygame.image.load("assets/notsunnysunflower.png"),
            pygame.image.load("assets/sunflower.png"),
        ]
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.last_switch_time = pygame.time.get_ticks()
        self.durations_ms = [5000, 2000]

    def draw(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_switch_time >= self.durations_ms[self.image_index]:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
            self.last_switch_time = current_time
        super().draw()


class Peashooter(Plant):
    def __init__(self, screen: pygame.Surface, row, column):
        super().__init__(screen, row, column, 6, 0, 100, "assets/peashooter.png")
        self.peas = []
        self.pea_x = row * 100 - 50
        self.pea_y = column * 100 - 50

    def shoot(self):
        peaspawn = peas_module.Pea(self.screen, self.pea_x,self.pea_y)
        self.peas.append(peaspawn)
        

class Gatling(Plant):
    def __init__(self, screen: pygame.Surface, row, column):
        super().__init__(screen, row, column, 6, 0, 200, "assets/gatling_pea.png")
        

class Wallnut(Plant): 
    def __init__(self, screen: pygame.Surface, row, column):
        super().__init__(screen, row, column, 32, 0, 50, "assets/walnut.png")
        

class Cherrybomb(Plant):
    def __init__(self, screen: pygame.Surface, row, column):
        super().__init__(screen, row, column, None, 0, 150, "assets/cherrybomb.png")

def main():
    pygame.init()

    pygame.display.set_caption("plants_module")
    screen = pygame.display.set_mode((1000, 650))
    sun_button = Button_module.Button(screen, 115, 550, "sunflower")
    pea_button = Button_module.Button(screen, 315, 550, "peashooter")
    rep_button = Button_module.Button(screen, 500, 550, "repeater")
    wall_button = Button_module.Button(screen, 665, 550, "wallnut")
    cherry_button = Button_module.Button(screen, 850, 550, "cherry bomb")
    
    sunny_mike = Sunflower(screen, 0, 0)
    spitty_mike = Peashooter(screen, 1, 0)
    super_spitty_mike = Gatling(screen, 2, 0)
    dense_mike = Wallnut(screen, 3,0)
    boom_mike = Cherrybomb(screen, 4, 0)
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO: Add you events code
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("TODO: make the cursor look like sunflower.png")
                pygame.mouse.set_visible(False)
                

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
            


        # TODO: Add your project code
        sunny_mike.draw()
        spitty_mike.draw()
        super_spitty_mike.draw()
        dense_mike.draw()
        boom_mike.draw()
        pygame.display.update()

if __name__ == "__main__":
    main()