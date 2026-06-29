import pygame
import sys, random, time
import Button_module, start_screen_module, Zombie_wave_module, money_module
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
        return self.x > self.screen.get_width()

def main():
    poop = True
    fart = False
    pygame.init()
    
    try:
        pygame.mixer.init()
    except Exception:
        pass

    music_available = pygame.mixer.get_init() is not None
    music_tracks = ["assets/5-loonboon.mp3", "assets/hype_zombie_music.mp3"]
    music_index = 0
    MUSIC_END = pygame.USEREVENT + 1
    music_started = False


    pygame.display.set_caption("pvz")
    screen = pygame.display.set_mode((1000, 650))

    # load plant preview images
    try:
        sunflower_preview = pygame.image.load("assets/sunflower.png").convert_alpha()
    except Exception:
        sunflower_preview = None
    selected_plant_image = None

    wave = Zombie_wave_module.Zombie_wave(screen)
    pea = Pea(screen, 350, 50)
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
            # handle end of music track to play next sequentially
            if event.type == pygame.USEREVENT + 1:
                try:
                    music_index = (music_index + 1) % len(music_tracks)
                    pygame.mixer.music.load(music_tracks[music_index])
                    pygame.mixer.music.play()
                except Exception:
                    pass
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sun_button.is_clicked_by(event.pos):
                    # toggle sunflower placement preview
                    if selected_plant_image is None and sunflower_preview is not None:
                        selected_plant_image = sunflower_preview
                        pygame.mouse.set_visible(False)
                    else:
                        selected_plant_image = None
                        pygame.mouse.set_visible(True)

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
                    if music_available and not music_started:
                        try:
                            pygame.mixer.music.set_volume(0.4)
                            pygame.mixer.music.load(music_tracks[music_index])
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_endevent(MUSIC_END)
                        except Exception:
                            pass
                        music_started = True
                
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
            pea.move()
            pea.draw()
            pea.off_screen()

            
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

if __name__ == "__main__":
    main()