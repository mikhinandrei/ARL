from KARL.Chord.Utilities import *
from KARL.Note import Note


class Chord():
    def __init__(self, string):
        if string[-1] == 'm':
            self.type = 'minor'
            string = string[:-1]
        else:
            self.type = 'major'
        self.main_note = Note(string, 1)
        self.notes = self.__build_chord()

    def __build_chord(self):
        if self.type == 'minor':
            return get_minor_chord(self.main_note)
        else:
            return get_major_chord(self.main_note)
