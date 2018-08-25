from KARL.Chord import Chord
from KARL.Note import Note
import unittest


class TestChord(unittest.TestCase):
    def test_init_minor_chord(self):
        chord = Chord(Note('A'), 'minor')
        self.assertEqual(chord.notes(), ['A', 'C', 'E'])
        self.assertEqual(str(chord), 'Am')

    def test_init_major_chord(self):
        chord = Chord(Note('C'))
        self.assertEqual(chord.notes(), ['C', 'E', 'G'])
        self.assertEqual(str(chord), 'C')

    def test_consist_major(self):
        chord = Chord(Note('C'))
        self.assertTrue(chord.consists_note('C'))
        self.assertTrue(chord.consists_note('E'))
        self.assertTrue(chord.consists_note('G'))

    def test_consist_minor(self):
        chord = Chord(Note('C'), 'minor')
        self.assertTrue(chord.consists_note('C'))
        self.assertTrue(chord.consists_note('D#'))
        self.assertTrue(chord.consists_note('G'))


if __name__ == '__main__':
    unittest.main()