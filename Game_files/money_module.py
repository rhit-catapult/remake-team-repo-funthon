import pygame 
import sys, random, time

class money():
    def __init__(self):
        self.sun = 0
    
    def sun_change(self, sundif):
        self.sun += sundif