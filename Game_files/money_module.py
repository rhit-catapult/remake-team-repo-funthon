import pygame 
import sys, random, time
import Zombies_spawn_module, Zombie_wave_module, Button_module

class money():
    def __init__(self, screen):
        self.screen = screen
        self.sun = 0
        self.last_sun = 0
        self.delay = 5000
        self.font = pygame.font.SysFont("arialrounded", 42)

    def sun_reset(self):
        self.sun = -25
        self.last_sun = 0

    def sun_change(self, sundif):
        self.sun += sundif

    def check_sun(self):
        return self.sun
    
    def natural_sun(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_sun >= self.delay:
            self.last_sun = current_time
            self.sun += 25
            

    def draw(self):
         self.screen.blit(self.font.render(f"sun: {self.sun}", True, (255,255,255), (120,60,40)),
                          (800,580))
            

# def main():
#     pygame.init()

#     pygame.display.set_caption("pvz")
#     screen = pygame.display.set_mode((1000, 650))

#     clock = pygame.time.Clock()

#     sun = money(screen)
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


#         sun.natural_sun()    
#         sun.sun_change(3)
#         sun.draw()


#         # TODO: Add your project code

#         pygame.display.update()

# if __name__ == "__main__":
#     main()