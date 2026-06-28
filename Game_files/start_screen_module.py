import pygame, sys, time, random, Button_module

class start_screen:
    def __init__(self, screen: pygame.surface):
        self.screen = screen
        self.font = pygame.font.SysFont("arialrounded", 42)
        self.caption_1 = self.font.render("start game?", True, (0,0,0), (255,255,255))
        self.start_button = Button_module.Button(self.screen, 100, 100, "Start")
        

    def draw(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.caption_1,(300,200))


# def main():
#     pygame.init()

#     pygame.display.set_caption("pvz")
#     screen = pygame.display.set_mode((1000, 650))

#     clock = pygame.time.Clock()

#     test_zombie = start_screen(screen)
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



#         test_zombie.draw()
            


#         # TODO: Add your project code

#         pygame.display.update()

# if __name__ == "__main__":
#     main()
