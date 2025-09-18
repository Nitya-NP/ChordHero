
"""
This class takes song name and chords and displays the chords
* Core functionality
- Visual chord progression display 
- audio feedback, plays both chords and beats
- controls - play, pause
"""
import pygame as pg
from SongClass import SongClass
from Block import Block
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice").Speak

class VisualClass:
    def __init__(self, song_name, chords, tempo):
        """
        Initialize the VisualClass with song details

        Parameters:
            song_name (str): Name of the song.
            chords (list): List of chords and their durations.
        """
        # Initialize song from song class, share class
        self.song = SongClass(song_name, chords,tempo)

        pg.display.set_caption(song_name)
        
        # settings of blocks
        self.width = 1500
        self.height = 800
        self.block_width = 300
        self.fps = 40
        self.tempo = tempo
        self.step = (self.tempo / 70) * self.block_width / self.fps
        self.note_spacing = 300
        self.running = True
        self.paused = False  # Start in paused state

        # Pygame initialization
        pg.init()
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()

        # Create blocks and setup graphics
        self.beats = pg.sprite.Group()
        self.create_blocks()
        self.setup_graphics()

        # Load sound effects
        self.A = pg.mixer.Sound("A.wav")
        self.B = pg.mixer.Sound("B.wav")
        self.C = pg.mixer.Sound("C.wav")
        self.D = pg.mixer.Sound("D.wav")
        self.E = pg.mixer.Sound("E.wav")
        self.F = pg.mixer.Sound("F.wav")
        self.G = pg.mixer.Sound("G.wav")
        self.Min = pg.mixer.Sound("Minor.wav")
        self.Maj = pg.mixer.Sound("Major.wav")
        self.Dim = pg.mixer.Sound("Diminished.wav")
        self.Dom = pg.mixer.Sound("Dominant.wav")
        self.Sev = pg.mixer.Sound("7.wav")
        self.beat_sound = pg.mixer.Sound("beat_Soundeffect.wav")
        self.chord_channel = pg.mixer.Channel(0)
        self.beat_channel = pg.mixer.Channel(1)

        # Load button images
        self.play_image = pg.transform.scale(pg.image.load("play.png"), (70, 70))  # Play button
        self.pause_image = pg.transform.scale(pg.image.load("pause.png"), (70, 70))  # Pause button
        self.home_image = pg.transform.scale(pg.image.load("home.png"), (70, 70))  # Home button
        self.exit_image = pg.transform.scale(pg.image.load("exit.png"), (70, 70))  # Exit button
        self.plus_image = pg.transform.scale(pg.image.load("plus.png"),(70,70)) #plus button
        self.minus_image= pg.transform.scale(pg.image.load("minus.png"),(70,70))#minus button

        # Rectangle block (bar) at the bottom
        self.bar_height = 140

        # Button positions
        self.button_spacing = 80  # Spacing between buttons
        self.buttons = self.create_buttons()

    def create_buttons(self):
        """Create buttons for the bottom bar."""
        button_width = 50
        button_height = 50

        # Calculate button positions
        total_button_width = 3 * button_width + 2 * self.button_spacing
        start_x = (self.width - total_button_width) // 2
        button_y = self.height - self.bar_height + (100 - button_height) // 2  # Center vertically in the bar

        buttons = {
            "home": pg.Rect(start_x, button_y, button_width, button_height),
            "play_pause": pg.Rect(start_x + button_width + self.button_spacing, button_y, button_width, button_height),
            "exit": pg.Rect(start_x + 2 * (button_width + self.button_spacing), button_y, button_width, button_height),
            "tempo_down": pg.Rect(start_x + 4 * (button_width + self.button_spacing), button_y, button_width, button_height),
            "tempo_up": pg.Rect(start_x + 5 * (button_width + self.button_spacing), button_y, button_width, button_height),
        }
        return buttons

    def draw_bottom_bar(self):
        """Draw the rectangle block (bar) at the bottom of the screen."""
        pg.draw.rect(self.screen, "white", (0, self.height - self.bar_height, self.width, self.bar_height))

    def draw_buttons(self):
        """Draw buttons on the bottom bar."""
        # Draw home button
        self.screen.blit(self.home_image, self.buttons["home"].topleft)

        # Draw play/pause button
        if self.paused:
            self.screen.blit(self.pause_image, self.buttons["play_pause"].topleft)
        else:
            self.screen.blit(self.play_image, self.buttons["play_pause"].topleft)

        # Draw exit button
        self.screen.blit(self.exit_image, self.buttons["exit"].topleft)
        
        #draw tempo buttons
        self.screen.blit(self.minus_image, self.buttons["tempo_down"].topleft)
        self.screen.blit(self.plus_image, self.buttons["tempo_up"].topleft)

    def handle_events(self):
        """Handle Pygame events like quitting the application and button clicks."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                self.handle_buttons(mouse_pos)

    def handle_buttons(self, mouse_pos):
        """Handle button clicks."""
        if self.buttons["home"].collidepoint(mouse_pos):
            self.running=False
        elif self.buttons["play_pause"].collidepoint(mouse_pos):
            self.paused = not self.paused  # Toggle pause state
        elif self.buttons["exit"].collidepoint(mouse_pos):
            pg.quit()  # Exit the application
        elif self.buttons["tempo_down"].collidepoint(mouse_pos): #decrease the tempo
            self.tempo -= 10
            self.step = (self.tempo / 70) * self.block_width / self.fps
        elif self.buttons["tempo_up"].collidepoint(mouse_pos): #increase the tempo
            self.tempo += 10
            self.step = (self.tempo / 70) * self.block_width / self.fps

    def create_blocks(self):
        """Create blocks for each chord and rest in the song."""
        for chord_info in self.song.get_chords():
            chord = chord_info[0]  # Chord name (e.g., 'C')
            duration = chord_info[1]  # Duration of the rest time- black blocks
            
            #color 
            red= (255, 0, 0)
            blue= (0, 0, 255)
            green = (57, 255, 20) 
            yellow= (255, 255, 0)
            pink= (255, 0, 255)
            magenta= (255, 0, 128)
            orange=(255, 95, 31)

            if chord == '_':  # Rest (Block black)
                for _ in range(duration):
                    self.beats.add(Block("black", self.width + self.note_spacing, self.block_width, self.height, None))
                    self.note_spacing += 310
            else:
                # Chords (colored blocks)
                color = "black"
                if 'A' in chord:
                    color = red
                elif 'B' in chord:
                    color = pink
                elif 'C' in chord:
                    color = yellow
                elif 'D' in chord:
                    color = blue
                elif 'E' in chord:
                    color = orange
                elif 'F' in chord:
                    color = green
                elif 'G' in chord:
                    color =  magenta

                self.beats.add(Block(color, self.width + self.note_spacing, self.block_width, self.height, chord))
                self.note_spacing += 310
                

                for _ in range(duration-1):
                    self.beats.add(Block("black", self.width + self.note_spacing, self.block_width, self.height, None))
                    self.note_spacing += 310

    def setup_graphics(self):
        """Setup additional graphics like the gray bar and hitbox."""
        # Gray bar
        self.bar = pg.Surface([50, self.height])
        self.bar.fill("gray")
        self.bar_rect = self.bar.get_rect()
        self.bar_rect.x = 50

        # Hitbox
        self.temporary = pg.Surface([5, self.height])
        self.hitbox = pg.Rect(350, 0, 5, self.height)

    def speak_chord(self, chord):
        """Speak the chord in a separate thread."""
        chord = chord.lower()
        base_note = chord[0]
        chord_type = chord[1:]

        # Play the base note sound
        if base_note == 'a':
            self.chord_channel.play(self.A)
        elif base_note == 'b':
            self.chord_channel.play(self.B)
        elif base_note == 'c':
            self.chord_channel.play(self.C)
        elif base_note == 'd':
            self.chord_channel.play(self.D)
        elif base_note == 'e':
            self.chord_channel.play(self.E)
        elif base_note == 'f':
            self.chord_channel.play(self.F)
        elif base_note == 'g':
            self.chord_channel.play(self.G)

        if chord_type != "":
            # Play the chord type sound
        
            if chord_type == 'min' or chord_type == "m":
                self.chord_channel.queue(self.Min)
            if chord_type == 'maj':
                self.chord_channel.queue(self.Maj)
            if chord_type == '7':
                self.chord_channel.queue(self.Sev)
            if chord_type == 'dim':
                self.chord_channel.queue(self.Dim)
                
            

    def play_beat_sound(self):
        """Play the beat sound."""
        self.beat_channel.play(self.beat_sound)

    def speak_beats(self):
        """Update the state of the beats and chord sounds when necessary."""
        for beat in self.beats:
            if beat.rect.colliderect(self.hitbox):
                if beat.chord is not None and not beat.chord_played:
                    self.speak_chord(beat.chord)
                    beat.chord_played = True
            if beat.rect.colliderect(self.bar_rect):
                if not beat.beat_played:
                    self.play_beat_sound()
                    beat.beat_played = True
        

    def draw_graphics(self):
        """Draw all graphics including blocks, chords, bar, and buttons."""
        self.screen.fill("white")
        for beat in self.beats:
            if not self.paused:  # Only move blocks if not paused
                beat.move(self.step)
            self.screen.blit(beat.image, beat.rect)
            self.screen.blit(beat.font.render(beat.chord, True, "black"), (beat.rect.x + 25, self.height - 600))
        self.screen.blit(self.bar, self.bar_rect)

        # Draw the bottom bar and buttons
        self.draw_bottom_bar()
        self.draw_buttons()

        pg.display.update()
        

    def run(self):
        """Main loop to run the application."""
        
        speak(f"Playing {self.song.get_name()}")
        while self.running:
            self.handle_events()
            if not self.paused:   #not paused play the beats 
                self.speak_beats()
            self.draw_graphics() #draw all the graphics 
            self.clock.tick(self.fps)

song_name = 'Happy Birthday'
chords = [['_', 3], ['C', 1], ['G', 4], ['Amin', 4], ['A', 1], ['G', 1]]
visual = VisualClass(song_name, chords, 60)
#visual.run()