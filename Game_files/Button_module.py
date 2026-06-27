import pygame
import sys


class Button:
    def __init__(self, screen, center_x, center_y, text, text_color=(255, 255, 255), background_color=(0, 0, 0),
                 border_color=(255, 255, 255), padding=10, font_name="arialrounded", font_size=24):
        self.screen = screen
        font = pygame.font.SysFont(font_name, font_size)
        self.caption = font.render(text.upper(), True, text_color, background_color)
        self.caption_x = center_x - self.caption.get_width() / 2
        self.caption_y = center_y - self.caption.get_height() / 2
        self.padding = padding
        self.bound_left_x = self.caption_x - self.padding
        self.bound_right_x = self.caption_x + self.caption.get_width() + self.padding
        self.bound_top_y = self.caption_y - self.padding
        self.bound_bottom_y = self.caption_y + self.caption.get_height() + self.padding
        self.background_color = background_color
        self.border_color = border_color
        self.text_color = text_color

    def draw(self):
        width = self.bound_right_x - self.bound_left_x
        height = self.bound_bottom_y - self.bound_top_y
        pygame.draw.rect(self.screen, self.background_color, (self.bound_left_x, self.bound_top_y, width, height))
        pygame.draw.rect(self.screen, self.border_color, (self.bound_left_x, self.bound_top_y, width, height), 4)

        self.screen.blit(self.caption, (self.caption_x, self.caption_y))

    def is_clicked_by(self, pos):
        pos_x = pos[0]
        pos_y = pos[1]
        return (self.bound_left_x < pos_x < self.bound_right_x and
                self.bound_top_y < pos_y < self.bound_bottom_y)  # Chained comparisons are only a Python thing.






# def main():
#     pygame.init()

#     pygame.display.set_caption("pvz")
#     screen = pygame.display.set_mode((1000, 650))

#     test_button = Button(screen, 200, 100, "ojsfiuawhf")

#     clock = pygame.time.Clock()
#     while True:
#         clock.tick(60)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()

#             # TODO: Add you events code
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if test_button.is_clicked_by(event.pos):
#                     print("i got clicked")

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
            

#         # TODO: Add your project code
#         test_button.draw()
#         pygame.display.update()


# main()