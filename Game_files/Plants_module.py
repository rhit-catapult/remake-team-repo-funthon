import pygame, time, peas_module, Zombie_wave_module, money_module

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
            if self.image_index == 1:
                money_module.money.get_instance().sun_change(25)
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
        super().__init__(screen, row, column, 10000000, 0, 150, "assets/cherrybomb.png")
        self.explosion_time = time.time() + 2

class Doomshroom(Plant):
    def __init__(self, screen: pygame.Surface, row, column):
        super().__init__(screen, row, column, 100000000, 0, 150, "assets/doom shrrom.png")

    def is_placed(self):
        zombie = Zombie_wave_module.Zombie_wave(self.screen)
        zombie.zombies.clear()