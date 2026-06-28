import pygame
import sys
import random
import start_screen_module
# import Zombie_wave_module

class Zombie_spawn:
    def __init__(self, screen:pygame.surface, columns, type):
        self.screen = screen
        self.x = 900 + random.randint(0, 75)
        self.columns = columns * 100
        self.type = type
        self.heath = 0
        self.speed = 0
    
    def draw(self):
        if self.type == 0:
            #regular type zombie
            self.heath = 10
            self.speed = 1
            self.screen.blit(pygame.image.load("assets/zombie.png"), (self.x, self.columns))
            
        if self.type == 1:
            #bucket type zombie
            self.heath = 28
            self.speed = 0.75
            self.screen.blit(pygame.image.load("assets/buckethead.png"), (self.x, self.columns))

        if self.type == 2:
            #runner type zombie
            self.heath = 6
            self.speed = 5
            self.screen.blit(pygame.image.load("assets/runner.png"), (self.x, self.columns))

        if self.type == 3:
            #hulk type zombie
            self.heath = 150
            self.speed = 0.30
            self.screen.blit(pygame.image.load("assets/hulk.png"), (self.x, self.columns))

    def move(self):
        self.x -= self.speed/5

    def hit_by(self, zombie):
        hit_box = pygame.Rect(self.columns, self.x, 25, 100)
        return hit_box.collidepoint(zombie.x, zombie.y)
    
    def at_end(self):
        if self.x < 100:
            return True

# def main():
#     pygame.init()

#     pygame.display.set_caption("pvz")
#     screen = pygame.display.set_mode((1000, 650))

#     clock = pygame.time.Clock()

#     test_zombie = Zombie_spawn(screen, random.randint(0, 4), random.randint(0, 3))
#     while True:
#         clock.tick(60)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()

#             # TODO: Add you events code


# # ------------------------------------- background code ---------------------------------------------------------
#         screen.fill((90,135,72))
#         line_y = -50
#         line_x = -50
#         dark_line = (85, 128, 68)
#         dark_square = (77, 116, 62)
#         square_x = -100
#         square_y = 100

#         for goon1000 in range(2):   #horizontal lines
#             line_y += 200
#             pygame.draw.line(screen, dark_line, (0, line_y), (900, line_y), 100)
               
#         for goon2000 in range(4):   #vertical lines
#             line_x += 200
#             pygame.draw.line(screen, dark_line, (line_x, 0), (line_x, 500), 100)

#         pygame.draw.line(screen, (100,100,100), (950, 0), (950, 650), 100)  #sidewalk
#         pygame.draw.line(screen, (120,60,40), (0, 575), (1000, 575), 150)   #bottom bar

#         for goon3000 in range(8):   #darkest squares
#             square_x += 200
#             pygame.draw.rect(screen, dark_square, ((square_x,square_y),(100,100)))
#             if square_x >= 700:
#                 square_y = 300
#                 square_x = -100





#         for goon4000 in range(4):   #placeholder slots
#             break
#             pygame.draw.rect(screen, (30,30,30), ((15,30), (100,100)))


#         test_zombie.move()
#         test_zombie.draw()
            


#         # TODO: Add your project code

#         pygame.display.update()

# if __name__ == "__main__":
    #main()