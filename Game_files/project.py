import pygame
import sys, random, time
import Button_module, peas_module, start_screen_module, Zombie_wave_module, money_module, plant_cursor as plant_cursor_module, Plants_module


def main():
    number = 0
    numex = 1
    more_speed = 0
    poop = True
    fart = bool
    total_spawns = 0
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
    money_module.money.shared_instance = money_module.money(screen)

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
    shovel_button= Button_module.Button(screen, 115, 615, "Shovel" )

    start_button = Button_module.Button(screen, 500, 300, "play")
    start_button.border_color = "white"
    end_button = Button_module.Button(screen, 500, 300, "restart?")
    end_button.border_color = "white"

    first_screen = start_screen_module.start_screen(screen)
    end_screen = start_screen_module.start_screen(screen)

    sun_counter = money_module.money.get_instance()

    clock = pygame.time.Clock()
    all_plants = []
    def plant_exists(row, col):
        return any(p.row == row and p.column == col for p in all_plants)
    
    def remove_plant_at(row, col):
        for k in range(len(all_plants) - 1, -1, -1):
            if all_plants[k].row == row and all_plants[k].column == col:
                del all_plants[k]
                return True
        return False
    
    plant_cursor = plant_cursor_module.PlantCursor(screen)

    while True:
        
        clock.tick(60)
        more_speed += 1/3000

        sun_amount = sun_counter.check_sun()

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
#------------------------------button event code-----------------------------------------------------#    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sun_button.is_clicked_by(event.pos) and sun_amount >= 50:
                    plant_cursor.showing_plant = "sunflower"
                    sun_counter.sun_change(-50)
                elif pea_button.is_clicked_by(event.pos) and sun_amount >= 100:
                    plant_cursor.showing_plant = "peashooter"
                    sun_counter.sun_change(-100)
                elif rep_button.is_clicked_by(event.pos) and sun_amount >= 200:
                    plant_cursor.showing_plant = "gatling"
                    sun_counter.sun_change(-200)
                elif wall_button.is_clicked_by(event.pos) and sun_amount >= 50:
                    plant_cursor.showing_plant = "wallnut"
                    sun_counter.sun_change(-50)
                elif cherry_button.is_clicked_by(event.pos) and sun_amount >= 500:
                    plant_cursor.showing_plant = "cherrybomb"
                    sun_counter.sun_change(-500)
                elif shovel_button.is_clicked_by(event.pos):
                    plant_cursor.showing_plant = "shovel"
                elif plant_cursor.showing_plant != "":
                    
                    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
                    row = mouse_pos_y // 100
                    col = mouse_pos_x // 100
                    if plant_cursor.showing_plant == "shovel":
                        if remove_plant_at(row,col):
                            print(f"Removed plant at {row}, {col}")
                        else:
                            print("no plant to smash")
                    else:
                        pass
                    
                    if plant_exists(row, col):
                        print("A plant is already at this location!")
                    elif row>= 5 or col >= 9:
                        print("you cant plant there lil bro")
                    else:
                        if plant_cursor.showing_plant == "sunflower":
                            all_plants.append(Plants_module.Sunflower(screen, row, col))
                        elif plant_cursor.showing_plant == "cherrybomb":
                            all_plants.append(Plants_module.Cherrybomb(screen, row, col))
                        elif plant_cursor.showing_plant == "peashooter":
                            all_plants.append(Plants_module.Peashooter(screen, row, col))
                        elif plant_cursor.showing_plant == "wallnut":
                            all_plants.append(Plants_module.Wallnut(screen, row, col))
                        elif plant_cursor.showing_plant == "gatling":
                            all_plants.append(Plants_module.Gatling(screen, row, col))
                        elif shovel_button.is_clicked_by(event.pos):
                            plant_cursor.showing_plant = "shovel"
                        else:
                            pygame.mouse.set_visible(True)
                        plant_cursor.showing_plant = ""
                else:
                    plant_cursor.showing_plant = ""

                if start_button.is_clicked_by(event.pos):
                    if poop == True:
                        poop = False
                        fart = False

                if end_button.is_clicked_by(event.pos):
                    if fart == True:   
                        fart = False
                        wave.zombies.clear()

                    if music_available and not music_started:
                        try:
                            pygame.mixer.music.set_volume(0.4)
                            pygame.mixer.music.load(music_tracks[music_index])
                            pygame.mixer.music.play()
                            pygame.mixer.music.set_endevent(MUSIC_END)
                        except Exception:
                            pass
                        music_started = True
    #---------------------start screen---------------------------------#        
        if poop == True:
            first_screen.draw_start()
            start_button.draw()
            number = 0
            numex = 1
            more_speed = 0

    #--------------------main bg---------------------------------------#
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
    #------------------------------------------------------------------------------------------------#
            sun_counter.natural_sun()

#----------------------------------draw code------------------------------------------------------------#
    #------------------------change color if you can afford----------------------#    
            if  sun_amount >= 50:
                sun_button.border_color = "blue"
                wall_button.border_color = "blue"
            else:
                sun_button.border_color = "red"
                wall_button.border_color = "red"

            if sun_amount >= 100:
                pea_button.border_color = "blue"
            else:
                pea_button.border_color = "red"

            if sun_amount >= 500:
                cherry_button.border_color = "blue"
            else:
                cherry_button.border_color = "red"
                
            if sun_amount >= 200:
                rep_button.border_color = "blue"
            else:
                rep_button.border_color = "red"

    #------------------------------main draw-------------------------------------------#
            for plants in all_plants:
                plants.draw()
            plant_cursor.draw()
            sun_button.draw()
            pea_button.draw()
            rep_button.draw()
            wall_button.draw()
            cherry_button.draw()
            shovel_button.draw()
            sun_counter.draw()
            for plant in all_plants:
                if isinstance(plant, Plants_module.Peashooter):
                    plant.shoot()
                    for bullet in list(plant.peas):
                        bullet.move()
                        bullet.draw()
                        for zombie in wave.zombies:
                            if zombie.hit_by(bullet):
                                zombie.health -= 1
                                if zombie.health == 0:
                                    zombie.need_kill = True
                                bullet.need_gone = True
                        if bullet.off_screen() and bullet in plant.peas:
                            bullet.need_gone = True
                    plant.remove_peas()
                elif isinstance(plant, Plants_module.Gatling):
                    plant.shoot()
                    for bullet2 in list(plant.peas2):
                        bullet2.move()
                        bullet2.draw()
                        for zombie in wave.zombies:
                            if zombie.hit_by(bullet2):
                                zombie.health -= 1
                                if zombie.health == 0:
                                    zombie.need_kill = True
                                bullet2.need_gone = True
                        if bullet2.off_screen() and bullet2 in plant.peas2:
                            bullet2.need_gone = True
                    plant.remove_peas()


            if number >= 500:
                number = 0
                wave.spawn_chance()

            for zombie in wave.zombies:
                for plant in all_plants:
                    if zombie.hit_plant(plant):
                        zombie.is_hitting_plant = True
                        plant.health -= zombie.damage/60
                        if plant.health <= 0:
                            all_plants.remove(plant)

                                
                if not zombie.is_hitting_plant:
                    zombie.move()
                zombie.draw(more_speed)
                zombie.is_hitting_plant = False
                if zombie.at_end():
                    if zombie.at_end() == True:
                        fart = True
                    zombie.need_kill = True

        
            for plant in all_plants:
                if isinstance(plant, Plants_module.Cherrybomb):
                    if time.time() >= plant.explosion_time:
                        for zombie in wave.zombies:
                            if zombie.exploded(plant):
                                zombie.health -= 50
                                if zombie.health <= 0:
                                    zombie.need_kill = True
                        all_plants.remove(plant)
            
            wave.remove_zombies()

            
        #---------------------------------end screen-----------------------------------#
        if fart == True:
            end_screen.draw_end()
            end_button.draw()
            sun_counter.sun_reset()
            all_plants.clear()
            number = 0
            numex = 1
            more_speed = 0

        #------------------------------------------------------------------------------#
        numex += 0.01
        pp = 1.05**numex
        number += pp
        #print(pp, numex)
        pygame.display.update()

main()