import pygame
import sys
import random
import Zombie_wave_module

class Zombie_spawn:
    def __init__(self, screen, columns, type):
        self.screen = screen
        self.y = 875
        self.columns = columns * 100
        self.type = type
        self.heath = 0
        self.speed = 0

    
    def draw(self):
        if self.type == 0:
            #regular type zombie
            self.heath = 10
            self.speed = 1
            pygame.draw.rect(self.screen, ("grey"), (self.y, self.columns, 25,100) )
            # TODO regular zombie

        if self.type == 1:
            #bucket type zombie
            self.heath = 28
            self.speed = 0.75
            pygame.draw.rect(self.screen, ("orange"), (self.y, self.columns, 25, 100) )
            # TODO bucket zombie

        if self.type == 2:
            #runner type zombie
            self.heath = 6
            self.speed = 2
            pygame.draw.rect(self.screen, ("red"), (self.y, self.columns, 25, 100) )
            # TODO runner zombie

        if self.type == 3:
            #hulk type zombie
            self.heath = 150
            self.speed = 0.30
            pygame.draw.rect(self.screen, ("black"), (self.y, self.columns, 25, 100) )
            # TODO hulk zombie

    def move(self):
        self.y -= self.speed/5
        pass

def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("zombie test")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((900, 500))
    test_zombie = Zombie_spawn(screen, random.randint(0, 3), random.randint(0, 3))
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
        test_zombie.move()
        test_zombie.draw()

        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

if __name__ == "__main__":
    main()
