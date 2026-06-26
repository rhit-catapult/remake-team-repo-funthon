import pygame
import sys
import random
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
        super().__init__(screen, row, column, 6, 0, 50, "sunflower.png") 
       

   


class Peashooter(Plant):
    def __init__(self, screen: pygame.Surface, x, y, health, cost, image):
        self.health = 6
        self.cost = 100

    def draw():
        pass

class Repeater(Plant):
    def __init__(self, screen: pygame.Surface, x, y, health, cost, image):
        self.health = 6
        self.cost = 200

    def draw():
        pass

class Wallnut(Plant): 
    def __init__(self, screen: pygame.Surface, x, y, health, cost, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.health = 32
        self.cost = 50

    def draw():
        pass

class Cherrybomb(Plant):
    def __init__(self, screen: pygame.Surface, x, y, cost, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.cost = 150

    def draw():
        pass
def main():
    pygame.init()

    pygame.display.set_caption("plants_module")
    screen = pygame.display.set_mode((1000, 650))
    sunny_mike = Sunflower(screen, 1, 6)
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO: Add you events code


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
        pygame.display.update()

if __name__ == "__main__":
    main()