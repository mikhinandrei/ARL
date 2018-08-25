from KARL.Utilities.Chord import *
from KARL.Note import Note


class Chord():
    def __init__(self, note, type='major'):
        self.__type = type
        self.__main_note = note
        self.__notes = self.__build_chord()

    def __str__(self):
        if self.type() == 'minor':
            return '{}m'.format(self.main_note())
        else:
            return str(self.main_note())

    def __build_chord(self):
        if self.__type == 'minor':
            return get_minor_chord(self.__main_note)
        else:
            return get_major_chord(self.__main_note)

    def consists_note(self, note):
        return note in self.notes()

    # Accessors
    def main_note(self):
        return self.__main_note

    def type(self):
        return self.__type

    def notes(self):
        return [x.note() for x in self.__notes]