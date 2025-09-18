
'''
This class takes a list and get elements of the list like - name, chords, bars
'''
class SongClass:
    def __init__(self, name, chords:list, tempo):
        self.name = name
        self.tempo=tempo
            
        self.chords = chords if chords is not None else []
            # Chords 2D list format
            # In each sub list: 
            # first index (self.chords[0]) is the chord, or it is '_' meaning rest
            # second index (self.chords[1]) is how many beats it lasts for
            
        self.total_bars = 0
        #counting total number of bars in the whole song
        for chord in self.chords:
            self.total_bars += chord[1]

    def get_chords(self):
        return self.chords
    
    def get_name(self):
        return self.name
    
    def get_total_bars(self):
        return self.total_bars
    
    def get_tempo(self):
        return self.tempo
    
    def set_tempo(self, tempo):
        self.tempo=tempo
    
    def __str__(self):
        return f'{self.name} - Song Object'
