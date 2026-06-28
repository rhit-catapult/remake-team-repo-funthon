import pygame #,  Button_module
class Pea():
    def __init__(self, screen: pygame.surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 10
    
    def move(self):
        self.x += self.speed

    def draw(self):
        pygame.draw.circle(self.screen, "dark green", (self.x, self.y), 10)

    def off_screen(self):
        if self.x > self.screen.get_width():
            print("IM OFF SCREEN")
            return True
        else:
            return False


# def main():
#     pygame.init()

#     pygame.display.set_caption("pvz")
#     screen = pygame.display.set_mode((1000, 650))

#     sun_button = Button_module.Button(screen, 115, 550, "sunflower")
#     pea_button = Button_module.Button(screen, 315, 550, "peashooter")
#     rep_button = Button_module.Button(screen, 500, 550, "repeater")
#     wall_button = Button_module.Button(screen, 665, 550, "wallnut")
#     cherry_button = Button_module.Button(screen, 850, 550, "cherry bomb")
    
#     test_pea = Pea(screen, 0,300)

#     clock = pygame.time.Clock()
#     while True:
#         clock.tick(60)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()

#             # TODO: Add you events code
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if sun_button.is_clicked_by(event.pos):
#                     print("SUN SUN SUN SUN SUN SUN ")

#                 if pea_button.is_clicked_by(event.pos):
#                     print("PEA PEA PEA PEA PEA PEA PEA APE")

#                 if rep_button.is_clicked_by(event.pos):
#                     print("PEA PEA PEA PEA PEA PEA PEA PEA PEA PEA PEA PAE PEA PEA PEA PEA PEA PEA PEA PEA PEA PEA PEA PEA PEA ")

#                 if wall_button.is_clicked_by(event.pos):
#                     print("WALLNUT")

#                 if cherry_button.is_clicked_by(event.pos):
#                     print("KABOOM")
# # ------------------------------------- background code ------------------------------------------------#
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


#         # TODO: Add your project code
# #----------------------------------draw code------------------------------------------------------------#
#         sun_button.draw()
#         pea_button.draw()
#         rep_button.draw()
#         wall_button.draw()
#         cherry_button.draw()

#         test_pea.move()
#         test_pea.draw()
#         test_pea.off_screen()
#         pygame.display.update()


# main()