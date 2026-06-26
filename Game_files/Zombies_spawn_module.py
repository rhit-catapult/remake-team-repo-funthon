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
        self.speed = random.randint(1, 3)

    
    def draw(self):
        if self.type == 1:
            #regular type zombie
            self.heath = 10
            self.speed += 6
            pygame.draw.rect(self.screen, ("grey"), (850, 300, 25,50) )
            # TODO regular zombie

        if self.type == 2:
            #bucket type zombie
            self.heath = 28
            self.speed += 3
            pygame.draw.rect(self.screen, ("orange"), (850, 200, 25,50) )
            # TODO bucket zombie

        if self.type == 3:
            #runner type zombie
            self.heath = 6
            self.speed += 10
            pygame.draw.rect(self.screen, ("red"), (850, 400, 25,50) )
            # TODO runner zombie

        if self.type == 4:
            #hulk type zombie
            self.heath = 150
            self.speed += 0
            pygame.draw.rect(self.screen, ("black"), (850, 100, 25,50) )
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
    test_zombie = Zombie_spawn(screen, 3, random.randint(1, 4))
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
        test_zombie.draw()

        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

if __name__ == "__main__":
    main()
