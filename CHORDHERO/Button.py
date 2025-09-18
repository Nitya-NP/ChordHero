
"""
This class creates multiple button with name of the music
also check if mousse is hovering over the buttons
"""

import pygame as pg
from SongClass import SongClass

pg.init()
global running 

screen_width =  1500
screen_height = 800


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
BUTTON_COLOR = (0, 0, 0)
BUTTON_HOVER_COLOR = (57, 255, 20)

button_font = pg.font.SysFont('tahoma', 35, bold=True)


class Button:

    def __init__(self,x, y, width, height, text, action=None, name=None, chordes=None,tempo=None):
    
        self.rect = pg.Rect(x, y, width, height) #x, y posion coordinaties & width and height button dimentions
        self.text = text #music name
        self.action = action #if clicked or not
        self.color = BUTTON_COLOR
        self.hover_color = BUTTON_HOVER_COLOR #if hovered than color changes
        
        self.name=name
        self.chordes=chordes
        self.screen = pg.display.set_mode((screen_width, screen_height))
        self.tempo=tempo
        
        self.SongClass = SongClass(self.name,self.chordes,self.tempo)

    def draw(self):
        # Draw button
        pg.draw.rect(self.screen, self.color, self.rect)
        pg.draw.rect(self.screen, BLACK, self.rect, 2)  # Border
        # Draw text
        t1=""
        t2=""
        # text is longer than splits into 2 lines
        if len(self.text)>16:
            t1=self.text[0:14]
            t2=self.text[14:]
            
            text_surface1 = button_font.render(t1, True, WHITE)
            text_surface2 = button_font.render(t2, True, WHITE)
            
            self.screen.blit(text_surface1, (self.rect.x + (self.rect.width - text_surface1.get_width()) // 2,
                                  self.rect.y-20 + (self.rect.height - text_surface1.get_height()) // 2))
            self.screen.blit(text_surface2, (self.rect.x + (self.rect.width - text_surface2.get_width()) // 2,
                                  self.rect.y+20 + (self.rect.height - text_surface2.get_height()) // 2))
        else:
            text_surface = button_font.render(self.text, True, WHITE)
            self.screen.blit(text_surface, (self.rect.x + (self.rect.width - text_surface.get_width()) // 2,
                                  self.rect.y + (self.rect.height - text_surface.get_height()) // 2))

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos) #check if mouse is hovering over the buttons
    

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if self.action:
                self.action()  # Perform the associated action