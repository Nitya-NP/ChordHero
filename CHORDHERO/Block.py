
"""
This class creates a block which represents chords in Chord visulization.
Each block has a chord and moves across the screem 
"""
import pygame as pg

class Block(pg.sprite.Sprite):
    def __init__(self, color, x, width, height, chord):
        pg.sprite.Sprite.__init__(self)# create the block

        self.image = pg.Surface([width,height]) #get position 
        self.image.fill(color) #fills with specific color 
        
        self.rect = self.image.get_rect()
        self.rect.x = x #position x
        self.rect.y = 0 #position y (0 as it moving across)
        
        self.chord = chord #text
        self.font = pg.font.SysFont('tahoma', 130,bold=True) #font for displaying the font
        
        self.chord_played = False
        self.beat_played = False
        
    def move(self,step):
        self.rect.x -= step #Move the block horizontlly by specific x steps
        