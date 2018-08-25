import unittest
from KARL.Note import Note


class TestNoteMethods(unittest.TestCase):
    def test___init__(self):
        note = Note('C', 1)
        self.assertEqual(str(note), 'C1')

    def test____add__(self):
        note = Note('C', 1)
        note_2 = note + 1
        self.assertEqual(str(note_2), 'C#1')

    def test_increment(self):
        note = Note('C', 1)
        note += 4
        self.assertEqual(note, 'E1')

    def test_next_octave(self):
        note = Note('A', 1)
        note += 5
        self.assertEqual(str(note), 'D2')


if __name__ == '__main__':
    unittest.main()