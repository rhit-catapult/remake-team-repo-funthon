import pygame
import sys
import random
import Zombie_wave_module

class Zombie_spawn:
    def __init__(self, screen, columns, type):
        self.screen = screen
        self.columns = columns
        self.type = type
        self.heath = 0
        self.speed = random.randint(1-3)

    
    def draw(self):
        if self.type == 1:
            #regular type zombie
            self.heath = 2
            self.speed += 1
            pygame.draw.rect(self.screen, (255,255,255), (50,100))
            # TODO regular zombie

        if self.type == 2:
            #bucket type zombie
            s
            # TODO bucket zombie

        if self.type == 3:
            #runner type zombie
            s
            # TODO runner zombie

        if self.type == 4:
            #hulk type zombie
            s
            # TODO hulk zombie

        pass

    def move(self):
        pass

def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("zombie test")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((900, 500))
    test_zombie
    # creates a Character from the my_character.py file

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO: Add you events code

        # TODO: Fill the screen with whatever background color you like!
        screen.fill((90, 135, 72))
        pygame.draw.line(screen, (45, 67, 36), (0, 150), (900, 150), 100)
        

        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

if __name__ == "__main__":
    main()
