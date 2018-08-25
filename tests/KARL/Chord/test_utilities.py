from KARL.Utilities.Chord import *
from KARL.Note import Note
import unittest


class TestUtilities(unittest.TestCase):
    def test_get_minor_chord(self):
        chord = get_minor_chord(Note('A', 1))
        self.assertEqual(chord, ['A1', 'C2', 'E2'])

    def test_get_major_chord(self):
        chord = get_major_chord(Note('C', 1))
        self.assertEqual(chord, ['C1', 'E1', 'G1'])

    def test_get_minor_chord_without_octave(self):
        chord = get_minor_chord(Note('A'))
        self.assertEqual(chord, ['A', 'C', 'E'])

    def test_get_major_chord_without_octave(self):
        chord = get_major_chord(Note('C'))
        self.assertEqual(chord, ['C', 'E', 'G'])

if __name__ == '__main__':
    unittest.main()