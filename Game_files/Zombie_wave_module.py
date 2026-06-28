import pygame
import sys
import random
import time
import Zombies_spawn_module


class Zombie_wave:
    def __init__(self, screen): 
        self.screen = screen
        #self.start_time = project.start_time #TODO start time has to be a time.pef_counter() when the start button is clicked
        self.zombies = []
        self.likely_hood = 500000 #TODO find a good value for this so that zombie spawning ramps up well
        self.random_chance = 0

    def spawn_chance(self):
       # elapsed_time = time.perf_counter() - self.start_time
        if random.randint(-100,100) == 1: #random.randint(elapsed_time ** 2, self.likely_hood) == self.likely_hood:
            print("working")
            self.random_chance = random.randint(0, 99)
            if self.random_chance <= 74:
                zombiespawn = Zombies_spawn_module.Zombie_spawn(self.screen, random.randint(0,4), 0)
                self.zombies.append(zombiespawn)
                print("normal")
            if 74 < self.random_chance <= 89:
                zombiespawn = Zombies_spawn_module.Zombie_spawn(self.screen, random.randint(0,4), 1)
                self.zombies.append(zombiespawn)
                print("bucket")
            if 89 < self.random_chance <= 98:
                zombiespawn = Zombies_spawn_module.Zombie_spawn(self.screen, random.randint(0,4), 2)
                self.zombies.append(zombiespawn)
                print("runner")
            if self.random_chance == 99:
                zombiespawn = Zombies_spawn_module.Zombie_spawn(self.screen, random.randint(0,4), 3)
                self.zombies.append(zombiespawn)
                print("hulk")

def main():
    pygame.init()

    pygame.display.set_caption("zombie test")
    screen = pygame.display.set_mode((1000, 650))

    clock = pygame.time.Clock()

    test_zombie = Zombie_wave(screen)
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


        test_zombie.spawn_chance()

        for zombie in test_zombie.zombies:
            zombie.move()
            zombie.draw()


        # TODO: Add your project code

        pygame.display.update()

if __name__ == "__main__":
    main()



