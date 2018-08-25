codes = {
    'C': 0,
    'C#': 1,
    'D': 2,
    'D#': 3,
    'E': 4,
    'F': 5,
    'F#': 6,
    'G': 7,
    'G#': 8,
    'A': 9,
    'A#': 10,
    'B': 11,
}

notes = {
    0: 'C',
    1: 'C#',
    2: 'D',
    3: 'D#',
    4: 'E',
    5: 'F',
    6: 'F#',
    7: 'G',
    8: 'G#',
    9: 'A',
    10: 'A#',
    11: 'B',
}

class Note():
    def __init__(self, note, octave):
        self.note = note
        if octave:
            self.octave = octave
        else:
            self.octave = 0

    def __add__(self, offset):
        if not isinstance(offset, int):
            raise Exception('Note offset must be an integer value!!!')
        new_val = codes[self.note] + offset
        octave = self.octave + new_val // 12
        note = notes[new_val % 12]
        return Note(note, octave)

    def __str__(self):
        return self.note + str(self.octave)

    def __eq__(self, other):
        return str(self) == other

