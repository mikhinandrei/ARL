import numpy as np
import wave
from KARL.Note import Note
from KARL.Chord import Chord


NOTES = ['C',
        'C#',
        'D',
        'D#',
        'E',
        'F',
        'F#',
        'G',
        'G#',
        'A',
        'A#',
        'B'
]


def get_sound_note(music_freqs, freq):
    if freq <= 0:
        return
    freq = np.log(freq)
    log_fr = np.log(list(music_freqs.keys()))
    list_freqs = list(music_freqs.keys())
    try:
        return music_freqs[list_freqs[int(round((log_fr[0] - freq)/0.0577))]]
    except IndexError:
        return


def get_harmony(music_notes, wf, chunk):
    result = dict(zip(NOTES, [1 for x in range(12)]))
    flag = 0
    prev_note = ''

    swidth = wf.getsampwidth()
    num_channels = wf.getnchannels()
    framerate = wf.getframerate()
    window = np.blackman(chunk)
    content = wf.readframes(chunk)

    for i in range(num_channels):
        data = content[i::num_channels]
        while len(data) == chunk * swidth:
            indata = np.array(wave.struct.unpack("%dh" % (len(data) / swidth), data)) * window
            fftData = abs(np.fft.rfft(indata)) ** 2
            fftData = np.array(list(filter(lambda x: x > 0, fftData)))
            if len(fftData) == 0:
                data = wf.readframes(chunk)
                data = data[1:len(data):2]
                continue
            which = fftData[1:].argmax() + 1
            if which != len(fftData) - 1:
                y0y, y1y, y2y = np.log(fftData[which - 1:which + 2])
                x1y = (y2y - y0y) * .5 / (2 * y1y - y2y - y0y)
                y = (which + x1y) * framerate / chunk
                try:
                    note = get_sound_note(music_notes, y)[:-1]
                except TypeError:
                    data = wf.readframes(chunk)
                    data = data[1:len(data):2]
                    continue
                if note != prev_note:
                    if flag == 1:
                        result[prev_note] -= 1
                    else:
                        flag = 1
                elif flag == 1:
                    flag = 0
                try:
                    result[note] += 1
                except KeyError:
                    result[note] = 1
            else:
                print("AAAAAARGGGGHHHHHH")
                print(y, get_sound_note(music_notes, y))
            prev_note = note
            data = wf.readframes(chunk)
            data = data[1:len(data):2]
    popular = list(dict(reversed(sorted(result.items(), key=lambda x: x[1]))).keys())
    print(popular)
    # ToDo: work for case Sound of Silence
    stated = 0
    tone = Note(popular[0])
    if result[NOTES[(NOTES.index(tone) + 3) % 12]] > result[NOTES[(NOTES.index(tone) + 4) % 12]]:
        return Chord(tone, 'minor')
    else:
        return Chord(tone)
