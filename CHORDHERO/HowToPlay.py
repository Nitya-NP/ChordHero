# -*- coding: utf-8 -*-
"""
This class pops How to Play screen.
displays the text and plays the audio 

"""
import pygame as pg
from win32com.client import Dispatch
import threading

pg.display.set_caption("How To Play")
icon = pg.image.load("icon.png")
pg.display.set_icon(icon)

class HowToPlay:
    def __init__(self):
        
        self.screen = pg.display.set_mode((800, 650)) #creats 800x650 screen
        self.clock = pg.time.Clock()
        self.speak= Dispatch("SAPI.SpVoice").speak #intialize speak import
        self.keep_playing_audio = True
        
        # Instructions with text
        self.instructions = [
            "1. Select a song from the menu",
            "2. The chords will appear on screen and chords will be played a", 
            "half a beat before it has to be played.",
            "3. After chord is being played, you follow along with the beats.",
            "4. Each chord representated by colors Red for A, Pink for B, Yellow for C", 
             "Blue for D, Orange for E, Green for F and Magenta for G ",
            "5. You can pause and play by navigating to the buttons.",
            "6. Press the home button to open the menu bar and Exit to", 
            "exit the program.",
        ]
        
        # close button at bottom center
        self.close_btn = pg.Rect(330, 560, 180, 60)
        
        # fonts
        self.fonts = {
            'title': pg.font.SysFont('tahoma', 50, bold=True),
            'text': pg.font.SysFont('tahoma', 25),
            'button': pg.font.SysFont('tahoma', 40)
        }

    def draw(self):
        self.screen.fill((240, 240, 245))  
        
        # Draws the title
        title = self.fonts['title'].render("How To Play", True, (0, 0, 0))
        self.screen.blit(title, (100+title.get_width()//2, 50))
        
        # Draws the instructions
        y= 150
        for line in self.instructions:
            text = self.fonts['text'].render(line, True, (0, 0, 0))
            self.screen.blit(text, (40, y))
            y += 50
        
        # Close button
        pg.draw.rect(self.screen, (200, 50, 50), self.close_btn)
        btn_text = self.fonts['button'].render("CLOSE", True, (255, 255, 255))
        self.screen.blit(btn_text, (360,560))

    def play_audio(self):
        #plays the instructions audio
        for line in self.instructions:
            if not self.keep_playing_audio:  # Check if we should stop
                return
            self.speak(line)
            for _ in range(25):
                if not self.keep_playing_audio:
                    return
                pg.time.delay(10)

    def run(self):
        # Start audio in separate thread
        audio_thread = threading.Thread(target=self.play_audio)
        audio_thread.start()
        
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.MOUSEBUTTONDOWN: #if close buttion clicked or not
                    if self.close_btn.collidepoint(event.pos):
                        running = False
            
            self.draw()
            pg.display.flip()
            self.clock.tick(60)
        
        # Clean up before closing
        self.keep_playing_audio = False  # Signal audio thread to stop

