import pygame
import sys, random, time
import Button_module, peas_module, start_screen_module, Zombie_wave_module, money_module

def main():
    poop = True
    fart = False
    pygame.init()

    pygame.display.set_caption("pvz")
    screen = pygame.display.set_mode((1000, 650))

    wave = Zombie_wave_module.Zombie_wave(screen)

    sun_button = Button_module.Button(screen, 115, 550, "sunflower")
    pea_button = Button_module.Button(screen, 315, 550, "peashooter")
    rep_button = Button_module.Button(screen, 500, 550, "repeater")
    wall_button = Button_module.Button(screen, 665, 550, "wallnut")
    cherry_button = Button_module.Button(screen, 850, 550, "cherry bomb")

    start_button = Button_module.Button(screen, 500, 300, "play")
    end_button = Button_module.Button(screen, 500, 300, "restart?")
    first_screen = start_screen_module.start_screen(screen)
    end_screen = start_screen_module.start_screen(screen)

    sun_counter = money_module.money(screen)

    clock = pygame.time.Clock()

    while True:
        
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sun_button.is_clicked_by(event.pos):
                    print("SUN SUN SUN SUN SUN SUN ")

                if pea_button.is_clicked_by(event.pos):
                    print("PEA PEA PEA PEA PEA PEA PEA APE")

                if rep_button.is_clicked_by(event.pos):
                    print("PEA PEA PEA PEA PEA PEA PEA PEA PEA PEA PEA PAE PEA PEA PEA PEA PEA PEA PEA PEA PEA PEA PEA PEA PEA ")

                if wall_button.is_clicked_by(event.pos):
                    print("WALLNUT")

                if cherry_button.is_clicked_by(event.pos):
                    print("KABOOM")

                if start_button.is_clicked_by(event.pos):
                    poop = False
                
                if end_button.is_clicked_by(event.pos):
                    fart = False
                    wave.zombies.clear()
# ------------------------------------- background code ------------------------------------------------#
        
        if poop == True:
            first_screen.draw_start()
            start_button.draw()

        else:
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

    #----------------------------------draw code------------------------------------------------------------#
            sun_button.draw()
            pea_button.draw()
            rep_button.draw()
            wall_button.draw()
            cherry_button.draw()
            sun_button.border_color = "blue"

            sun_counter.natural_sun()
            sun_counter.draw()
            
            wave.spawn_chance()
            for zombie in wave.zombies:
                zombie.move()
                zombie.draw()
                if zombie.at_end():
                    if zombie.at_end() == True:
                        fart = True
                    wave.zombies.remove(zombie)
        if fart == True:
            end_screen.draw_end()
            end_button.draw()

        pygame.display.update()

main()