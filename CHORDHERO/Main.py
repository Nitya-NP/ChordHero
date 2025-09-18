"""
This is MainMenu of chordify  which represents lsit of songs, how to play button and quit button

"""

import pygame as pg
import os
from VisualClass import VisualClass
from SongClass import SongClass
from Button import Button
from HowToPlay import HowToPlay
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice").Speak
import threading

# list of songs 
Song1 = SongClass("Happy Birthday",
                      [["_",1],["G",3],["D",3],["D7",3],["G",6],["C",3],
                       ["G",2],["D7",1],["G",2]],100)

Song2 = SongClass("Let It Be",
                 [["_",1],["C",4],["G",4],["AMin",4],["F",4],["C",4],
                  ["G",4],["F",2],["EMin",1],["DMin",1],["C",4],
                  ["C",4],["G",4],["AMin",4],["F",4],["C",4],
                  ["G",4],["F",2],["EMin",1],["DMin",1],["C",4]],146)

Song3 = SongClass("Hotel California", [['_',1],['Amin',4],['E7',4],['G',4],['D',4],['F',4],['C',4],['Dmin',4],['E7',4],
                                                        ['Amin',4],['E7',4],['G',4],['D',4],['F',4],['C',4],['Dmin',4],['E7',4],
                                                        ['Amin',4],['E7',4],['G',4],['D',4],['F',4],['C',4],['Dmin',4],['E7',4],
                                                        ['Amin',4],['E7',4],['G',4],['D',4],['F',4],['C',4],['Dmin',4],['E7',4],
                                                        ['F',4],['C',4],['E7',4],['Amin',4],['F',4],['C',4],['Dmin',4],['E7',4],
                                                        ['Amin',4],['E7',4],['G',4],['D',4],['F',4],['C',4],['Dmin',4],['E7',4],
                                                        ['Amin',4],['E7',4],['G',4],['D',4],['F',4],['C',4],['Dmin',4],['E7',4],
                                                        ['F',4],['C',4],['E7',4],['Amin',4],['F',4],['C',4],['Dmin',4],['E7',4],
                                                        ['Amin',4],['E7',4],['G',4],['D',4],['F',4],['C',4],['Dmin',4],['E7',4],
                                                        ['Amin',4],['E7',4],['G',4],['D',4],['F',4],['C',4],['Dmin',4],['E7',4],
                                                        ['Amin',4],['E7',4],['G',4],['D',4],['F',4],['C',4],['Dmin',4],['E7',4]],148)

Song4 = SongClass("La Bamba",[['_',1],['C',2],['F',2],['G',2],['F',2],['C',2],['F',2],['G',4],
                                       ['C',2],['F',2],['G',2],['F',2],['C',2],['F',2],['G',2],['F',2],
                                       ['C',2],['F',2],['G',2],['F',2],['C',2],['F',2],['G',2],['F',2],
                                       ['C',2],['F',2],['G',2],['F',2],['C',2],['F',2],['G',2],['F',2],['C',2],['F',2],['G',4],
                                       ['C',2],['F',2],['G',2],['F',2],['C',2],['F',2],['G',2],['F',2],['C',2],['F',2],['G',2],['F',2],
                                       ['C',2],['F',2],['G',2],['F',2],['C',2],['F',2],['G',2],['F',2],
                                       ['C',2],['F',2],['G',2],['F',2],['C',2],['F',2],['G',4]],144
                                       )

Song5 = SongClass("Take it Easy", [['_',4],['G',4],['C',2],['Amin',2],['G',4],['C',2],['Amin',2],
                                   ['G',4],['G',5],['D',1],['C',2],
                                   ['G',2],['D',2],['C',2],["G",2],
                                   ["Emin",4],['C',2],["G",2],['Amin',2],['C',2],["Emin",4],
                                   ['C',2],["G",2],['C',2],["G",2],['Amin',2],['C',2],["G",4],["G",4],
                                   ['G',5],['D',1],['C',2],['G',2],['D',2],['C',2],["G",2],
                                   ["Emin",2],['D',2],['C',2],["G",2],['Amin',2],['C',2],["Emin",4],
                                   ['C',2],["G",2],['C',2],["G",2],['Amin',2],['C',2],["G",4],
                                   ['G',5],['D',1],['C',2],
                                   ['G',2],['D',2],['C',2],["G",2],
                                   ['Emin',2],['D',2],['C',2],["G",2],
                                   ['Amin',2],['C',2],['Emin',2],["D",2],
                                   ['G',5],['D',1],['Amin7',2],['G',2],['D',2],['C',2],["G",2],
                                   ['Emin',4],['C',2],["G",2],
                                   ['Amin',2],['C',2],['Emin',4],
                                   ['C',2],["G",2],['C',2],["G",2],['Amin',2],['C',2],["G",4],
                                   ['C',2],["C",2],['G',2],["G",2],['C',2],["C",2],['G',2],["G",2],
                                   ['C',2],["C",2],['G',2],["Dmin7",2],['C',4],['G',2],["Dmin7",2],['C',4],['Emin',1]],139)




Song6 = SongClass("All of Me", [['Emin',2],['C',2],['G',2],['D',2],['Emin',2],['C',2],['G',2],['D',2],
                               ['Emin',2],['C',2],['G',2],['D',2],['Emin',2],['C',2],['G',2],['D',2],['Emin',2],['C',2],['G',2],['D',2],['Emin',2],['C',2],['G',2],['D',2],
                               ['Amin',4],['G',2],['D',2],['Amin',4],['G',2],['D',2],
                               ['G',4],['Emin',4],['Amin',4],['C',2],['D',2],['G',4],['Emin',4],['Amin',4],['C',2],['D',2],
                               ['Emin',2],['C',2],['G',2],['D',2],['Emin',2],['C',2],['G',2],['D',2],
                               ['Amin',4],['G',2],['D',2],['Amin',4],['G',2],['D',2],
                               ['G',4],['Emin',4],['Amin',4],['C',2],['D',2],['G',4],['Emin',4],['Amin',4],['C',2],['D',2],
                               ['Emin',2],['C',2],['G',2],['D',2],['Emin',2],['C',2],['G',2],['D',2],['Emin',2],['C',2],['G',2],['D',2],['Emin',2],['C',2],['G',2],['D',2]],120)

Song7 = SongClass("Brown Eyed Girl", [['G',2],['C',2],['G',2],['D',2],['G',2],['C',2],['G',2],['D',2],
                                      ['G',2],['C',2],['G',2],['D',2],['G',2],['C',2],['G',2],['D',2],
                                      ['G',2],['C',2],['G',2],['D',2],['G',2],['C',2],['G',2],['D',2],
                                      ['D',4],['G',2],['Emin',2],['C',2],['D',2],['G',2],['D7',2],
                                      ['G',2],['C',2],['G',2],['D',2],['G',2],['C',2],['G',2],['D',2],
                                      ['G',2],['C',2],['G',2],['D',2],['G',2],['C',2],['G',2],['D',2],
                                      ['D',4],['G',2],['Emin',2],['C',2],['D',2],['G',4],
                                      ['D7',4],
                                      ['G',2],['C',2],['G',2],['D',2],['G',2],['C',2],['G',2],['D',2],['G',4]],141)

Song8 = SongClass("I'm Yours", [['G',4],['D',4],['Emin',4],['C',4],
                                ['G',4],['D',4],['Emin',4],['C',4],['G',4],['D',4],['Emin',4],['C',4],
                                ['G',4],['D',4],['Emin',4],['C',4],['G',4],['D',4],['Emin',4],['C',4],
                                ['G',4],['D',4],['Emin',4],['C',4],['G',4],['D',4],['Emin',4],['C',4],['A7',4],
                                ['G',4],['D',4],['Emin',4],['C',4],['G',4],['D',4],['Emin',4],['C',4],
                                ['G',2],['D',2],['Emin',2],['D',2],['C',4],['A7',4],
                                ['G',2],['Bmin',2],['Emin',2],['D',2],['C',4],['A7',4],
                                ['G',4],['D',4],['Emin',4],['C',4],['G',4],['D',4],['Emin',4],['C',4],
                                ['G',4],['D',4],['Emin',4],['C',4],['G',4],['D',4],['Emin',4],['C',4],
                                ['G',4],['D',4],['Emin',4],['C',4],['A7',4],['G',4]],151)

Song9 = SongClass('Have You Ever Seen The Rain', [['Amin',2],['F',2],['C',2],['G',2],['C',4],
                                                  ['C',4],['C',4],['G',4],['C',4],['C',4],['C',4],['G',4],['C',4],
                                                  ['F',2],['G',2],['C',2],['Amin7',2],['F',2],['G',2],['C',2],['Amin7',2],
                                                  ['F',2],['G',2],['C',4],
                                                  ['C',4],['C',4],['G',4],['C',4],['C',4],['C',4],['G',4],['C',4],
                                                  ['F',2],['G',2],['C',2],['Amin7',2],['F',2],['G',2],['C',2],['Amin7',2],
                                                  ['F',2],['G',2],['C',4],
                                                  ['F',2],['G',2],['C',2],['Amin7',2],['F',2],['G',2],['C',2],['Amin7',2],
                                                  ['F',2],['G',2],['C',4],['G',4],['C',4]],116)

Song10 = SongClass("Zombie",[["_",4],["Em",4],["C",4],["G",4],["D",4],["Em",4],["C",4],["G",4],["D",4],
                            ["Em",4],["C",4],["G",4],["D",4],["Em",4],["C",4],["G",4],["D",4],["Em",4],
                            ["C",4],["G",4],["D",4],["Em",4],["C",4],["G",4],["D",4],["Em",4],["C",4],
                            ["G",4],["D",4],["Em",4],["C",4],["G",4],["D",4],["Em",4],["C",4],["G",4],
                            ["D",4],["Em",4],["C",4],["G",4],["D",4],["Em",4],["C",4],["G",4],["D",4],
                            ["Em",4],["C",4],["G",4],["D",4],["Em",4],["C",4],["G",4],["D",4],["Em",4],
                            ["C",4],["G",4],["D",4],["Em",4],["C",4],["G",4],["D",4],["Em",4],["C",4],
                            ["G",4],["D",4],["Em",4],["C",4],["G",4],["D",4],["Em",4],["C",4],["G",4],
                            ["D",4],["Em",4],["C",4],["G",4],["D",4],["Em",4],["C",4],["G",4],["D",4],
                            ["Em",4],["C",4],["Em",4],["C",4],["Em",4],["C",4],["Em",4],["C",4],["Em",4],
                            ["C",4],["G",4],["D",4],["Em",4],["C",4],["G",4],["D",4],["Em",4],["C",4],
                            ["G",4],["D",4],["Em",4],["C",4],["Em",4],["C",4],["Em",4],["C",4],["Em",4]],167)

Song11 = SongClass("Losing My Religion",[["_",4],["F",4],["Dm",2],["G",2],["Am",8],["F",4],["Dm",2],                                        
                                        ["G",2],["Am",4],["G",4],["Am",8],["Em",8],["Am",8],["Em",8],["Am",8],["Em",8],
                                        ["Dm",8],["G",8],["Am",8],["Em",8],["Am",8],["Em",8],["Am",8],["Em",8],
                                        ["Dm",8],["G",8],["F",4],["Dm",2],["G",2],["Am",8],["F",4],["Dm",2],["G",2],
                                        ["Am",8],["Am",8],["Em",8],["Am",8],["Em",8],["Am",8],["Em",8],["Dm",8],["G",8],
                                        ["Am",8],["Em",8],["Am",8],["Em",8],["Am",8],["Em",8],["Dm",8],["G",8],["F",4],
                                        ["Dm",2],["G",2],["Am",8],["F",4],["Dm",2],["G",2],["Am",4],["G",4],["Am",4],
                                        ["G",4],["F",4],["G",4],["C",4],["Dm",4],["C",4],["Dm",4],["Am",8],["Em",8],
                                        ["Am",8],["Em",8],["Am",8],["Em",8],["Dm",8],["G",8],["F",4],["Dm",2],["G",2],
                                        ["Am",8],["F",4],["Dm",2],["G",2],["Am",8],["F",4],["Dm",2],["G",2],["Am",8],
                                        ["F",4],["Dm",2],["G",2],["Am",4],["G",4],["Am",8],["Am",8],["Am",8],["Am",8]],122)

Song12 = SongClass("How To Dissapear Completely", [["_",12],["C",12],["C",12],["Em",12],["Em",12],["C",12],
                                                  ["C",12],["Em",12],["Em",12],["C",12],["C",12],["Em",12],["Em",12],["C",12],
                                                  ["C",12],["Em",12],["Em",12],["C",12],["C",12],["Em",12],["Em",12],["G",12],
                                                  ["G",12],["Em",12],["Em",12],["G",12],["G",12],["Em",12],["Em",12],["C",12],
                                                  ["Em",12],["Em",12],["C",12],["C",12],["Em",12],["Em",12],["G",12],["G",12],
                                                  ["Em",12],["Em",12],["G",12],["G",12],["Em",12],["Em",12],["C",12],["Em",12],
                                                  ["Em",12],["C",12],["C",12],["Em",12],["Em",12],["G",12],["G",12],["Em",12],
                                                  ["Em",12],["G",12],["G",12],["Em",12],["Em",12],["Em",12],["Em",12],["D",12],
                                                  ["D",12],["Em",12],["Em",12],["Em",12],["Em",12],["D",12],["D",12],["Em",12],
                                                  ["Em",12],["Em",12],["Em",1]],102)


pg.init()

running = True 

screen_width =  1500
screen_height = 800

pg.display.set_caption("CHORDHERO") #caption 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
BUTTON_COLOR = (0, 0, 0)
BUTTON_HOVER_COLOR = (57, 255, 20)

icon = pg.image.load("icon.png") #icon intilization
pg.display.set_icon(icon)

logo_img = pg.image.load("icon.png")
logo_img = pg.transform.scale(logo_img, (150, 150)) #resize
    
class MainMenu:
    def __init__(self):
        """Intialize the following variables """
        self.running = True  
        x = 170
        #intializing buttons of each song, quit button adn houw to pllay button
        self.buttons = [
            Button(30, 20 + x, 300, 100, Song1.get_name(), lambda: self.open_popup(Song1), Song1.get_name(), Song1.get_chords(),Song1.get_tempo()),
            Button(410, 20 + x, 300, 100, Song2.get_name(), lambda: self.open_popup(Song2), Song2.get_name(), Song2.get_chords(),Song2.get_tempo()),
            Button(800, 20 + x, 300, 100, Song3.get_name(), lambda: self.open_popup(Song3), Song3.get_name(), Song3.get_chords(),Song3.get_tempo()),
            Button(1170, 20 + x, 300, 100, Song4.get_name(), lambda: self.open_popup(Song4), Song4.get_name(), Song4.get_chords(),Song4.get_tempo()),
            Button(30, 180 + x, 300, 100, Song5.get_name(), lambda: self.open_popup(Song5), Song5.get_name(), Song5.get_chords(),Song5.get_tempo()),
            Button(410, 180  + x, 300, 100, Song6.get_name(), lambda: self.open_popup(Song6), Song6.get_name(), Song6.get_chords(),Song6.get_tempo()),
            Button(800, 180  + x, 300, 100, Song7.get_name(), lambda: self.open_popup(Song7), Song7.get_name(), Song7.get_chords(),Song7.get_tempo()),
            Button(1170, 180  + x, 300, 100, Song8.get_name(), lambda: self.open_popup(Song8), Song8.get_name(), Song8.get_chords(),Song8.get_tempo()),
            Button(30, 330 + x, 300, 100, Song9.get_name(), lambda: self.open_popup(Song9), Song9.get_name(), Song9.get_chords(),Song9.get_tempo()),
            Button(410, 330 + x, 300, 100, Song10.get_name(), lambda: self.open_popup(Song10), Song10.get_name(), Song10.get_chords(),Song10.get_tempo()),
            Button(800, 330 + x, 300, 100, Song11.get_name(), lambda: self.open_popup(Song11), Song11.get_name(), Song11.get_chords(),Song11.get_tempo()),
            Button(1170, 330 + x, 300, 100, Song12.get_name(), lambda: self.open_popup(Song12), Song12.get_name(), Song12.get_chords(),Song12.get_tempo()),
            Button(410, 640, 300, 100, "QUIT", self.quit_game),
            Button(800, 640, 300, 100, "HOW TO PLAY", self.HowToPlay)
        ]
        self.previously_hovered = None  # Track the previously hovered button

        # Title text
        self.title_font = pg.font.SysFont('couriernew', 120, bold=True)  # Customize font and size for title
        self.title_text = self.title_font.render("CHORDHERO", True, BLACK)  # display title
        self.logo_img = logo_img  
        self.title_group_width = self.logo_img.get_width() + 20 + self.title_text.get_width()
        self.screen = pg.display.set_mode((screen_width, screen_height))

    def draw(self):
        """ Dras the title text, logo and button """
        self.screen.fill((255,255,255)), [pg.draw.line(self.screen, (255, max(150, 255-int(105*y/screen_height)), min(255, int(50+205*y/screen_height))), (0,y), (screen_width,y)) for y in range(screen_height)]

        # Draw the title at the top center
        title_x = (screen_width - self.title_text.get_width()) // 2  # Center horizontally
        title_y = 10  # Position at the top with some padding
        
        title_group_x = (screen_width - self.title_group_width) // 2  # Center the group
        title_y = 10
        
        # Draw logo 
        self.screen.blit(self.logo_img, (title_group_x-10, title_y -20+ (self.title_text.get_height() - self.logo_img.get_height()) // 2))
        self.screen.blit(self.title_text, (title_x+50, title_y))
        
        # Draw buttons
        for button in self.buttons:
            button.draw()
            
    def HowToPlay(self):
        """open the howtoplay button and runs it"""
        self.running =False
        
        self.HowToPlay= HowToPlay()
        self.HowToPlay.run()
        self.screen = pg.display.set_mode((screen_width, screen_height)) #resize the screen after howtoplay is played 
    
    def open_popup(self, Song):
        """open visualclass and chord visulization"""
        self.running=False
        Song = VisualClass(Song.get_name(), Song.get_chords(),Song.get_tempo())
        Song.run()
        #self.running =True

    def quit_game(self):
        """when clicked quit, it stops running closes the screeen"""
        global running
        running = False   
    
    def speak_async(self,text):
        """speak the song name """
        threading.Thread(target=speak, args=(text,)).start()

    def handle_events(self, event):
        """handles mouse events"""
        mouse_pos = pg.mouse.get_pos()
        currently_hovered = None
    
        #First pass to find which button is hovered
        for button in self.buttons:
            if button.is_hovered(mouse_pos):
                currently_hovered = button
                break
            
        # Second pass to update button states
        for button in self.buttons:
            if button == currently_hovered:
                if button != self.previously_hovered:
                    button.color = BUTTON_HOVER_COLOR #changes color 
                    self.speak_async(button.text)#plays the text sound
            else:
                button.color = BUTTON_COLOR
                
            button.handle_event(event)
            
        # Update the previously hovered button
        self.previously_hovered = currently_hovered

           
def main():
    """plays the mainmenu"""
    menu = MainMenu() 
    global running
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            menu.handle_events(event)
        menu.draw()
        pg.display.flip()
    pg.quit()
    os._exit(0)

if __name__ == "__main__":
    main()
    