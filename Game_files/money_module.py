import pygame 

class money():
    def __init__(self, screen):
        self.screen = screen
        self.sun = 0
        self.last_sun = 0
        self.delay = 5000
        self.font = pygame.font.SysFont("arialrounded", 42)
        shared_instance = None

    @classmethod
    def get_instance(cls):
        return cls.shared_instance

    def sun_reset(self):
        self.sun = -25
        self.last_sun = 0

    def sun_change(self, sundif):
        self.sun += sundif

    def check_sun(self):
        return self.sun
    
    def natural_sun(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_sun >= self.delay:
            self.last_sun = current_time
            self.sun += 25
            
    def draw(self):
         self.screen.blit(self.font.render(f"sun: {self.sun}", True, (255,255,255), (120,60,40)),
                          (800,580))