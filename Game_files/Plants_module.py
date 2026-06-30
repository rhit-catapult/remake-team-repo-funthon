import pygame
import sys, random, time
import Button_module, peas_module, start_screen_module, Zombie_wave_module, money_module

class Plant:
    def __init__(self, screen: pygame.Surface,row, column, health, damage, cost, image_filename):
        self.screen = screen
        self.column = column
        self.row = row 
        self.health = health 
        self.damage = damage
        self.cost = cost
        self.image:pygame.Surface = pygame.image.load(image_filename)

    def draw(self):
        self.screen.blit(self.image, (self.column*100, self.row*100))

    def get_xy(self):
        return self.column*100, self.row*100


class Sunflower(Plant):
    def __init__(self, screen: pygame.Surface, row, column):
        super().__init__(screen, row, column, 6, 0, 50, "assets/notsunnysunflower.png")
        self.images = [
            pygame.image.load("assets/notsunnysunflower.png"),
            pygame.image.load("assets/sunflower.png"),
        ]
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.last_switch_time = pygame.time.get_ticks()
        self.durations_ms = [5000, 2000]

    def draw(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_switch_time >= self.durations_ms[self.image_index]:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
            self.last_switch_time = current_time
        super().draw()


class Peashooter(Plant):
    def __init__(self, screen: pygame.Surface, row, column):
        super().__init__(screen, row, column, 6, 0, 100, "assets/peashooter.png")
        self.peas = []
        self.pea_y = (row * 100) + 50 
        self.pea_x = (column * 100) + 50
        self.last_shot = 0
        self.delay = 2500

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot >= self.delay:
            self.last_shot = current_time
            peaspawn = peas_module.Pea(self.screen, self.pea_x,self.pea_y)
            self.peas.append(peaspawn)
        
    def remove_peas(self):
        for k in range (len(self.peas)-1, -1, -1):
            if self.peas[k].need_gone:
                self.peas.remove(self.peas[k])

class Gatling(Plant):
    def __init__(self, screen: pygame.Surface, row, column):
        super().__init__(screen, row, column, 6, 0, 200, "assets/gatling_pea.png")
        self.peas2 = []
        self.pea_y2 = (row * 100) + 50 
        self.pea_x2 = (column * 100) + 50
        self.last_shot2 = 0
        self.delay2 = 1250

    def shoot(self):
        current_time2 = pygame.time.get_ticks()
        if current_time2 - self.last_shot2 >= self.delay2:
            self.last_shot2 = current_time2
            peaspawn2 = peas_module.Pea(self.screen, self.pea_x2,self.pea_y2)
            self.peas2.append(peaspawn2)
        
    def remove_peas(self):
        for k in range (len(self.peas2)-1, -1, -1):
            if self.peas2[k].need_gone:
                self.peas2.remove(self.peas2[k])
        

class Wallnut(Plant): 
    def __init__(self, screen: pygame.Surface, row, column):
        super().__init__(screen, row, column, 32, 0, 50, "assets/walnut.png")
        

class Cherrybomb(Plant):
    def __init__(self, screen: pygame.Surface, row, column):
        super().__init__(screen, row, column, None, 0, 150, "assets/cherrybomb.png")

def main():
    poop = True
    fart = bool
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

    sunny_mike = Sunflower(screen, 0, 0)
    spitty_mike = Peashooter(screen, 1, 0)
    super_spitty_mike = Gatling(screen, 2, 0)
    dense_mike = Wallnut(screen, 3,0)
    boom_mike = Cherrybomb(screen, 4, 0)

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
                    fart = False

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

            sun_counter.natural_sun()


    #----------------------------------draw code------------------------------------------------------------#
            sun_button.draw()
            pea_button.draw()
            rep_button.draw()
            wall_button.draw()
            cherry_button.draw()
            sun_button.border_color = "blue"

            sun_counter.draw()
            sunny_mike.draw()
            spitty_mike.shoot()
            for bullet in spitty_mike.peas:
                bullet.move()
                bullet.draw()
                if bullet.off_screen():
                    spitty_mike.peas.remove(bullet)
            spitty_mike.draw()
            super_spitty_mike.shoot()
            for bullet2 in super_spitty_mike.peas2:
                bullet2.move()
                bullet2.draw()
                if bullet2.off_screen():
                    super_spitty_mike.peas2.remove(bullet2)
            super_spitty_mike.draw()
            dense_mike.draw()
            boom_mike.draw()
            
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
            sun_counter.sun_reset()

        pygame.display.update()

if __name__ == "__main__":
    main()