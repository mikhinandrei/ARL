def get_minor_chord(main_note):
    first = main_note
    third = first + 3
    fifth = third + 4
    return [first, third, fifth]


def get_major_chord(main_note):
    first = main_note
    third = first + 4
    fifth = third + 3
    return [first, third, fifth]