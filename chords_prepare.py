import wave
from lib.musicman import *
import json
import pandas as pd

types = {
    1: np.int8,
    2: np.int16,
    4: np.int32
}

music_notes = load_data()

chunk = 2500

lines = []

chords = ['C', 'Cm',
          'C#', 'C#m',
          'D', 'Dm',
          'D#', 'D#m',
          'E', 'Em',
          'F', 'Fm',
          'F#', 'F#m',
          'G', 'Gm',
          'G#', 'G#m',
          'A', 'Am',
          'A#', 'A#m',
          'B', 'Bm']

for chord in chords:
    wf = wave.open(('data/chords/%s.wav' % format(chord)), 'r')

    swidth = wf.getsampwidth()
    num_channels = wf.getnchannels()
    framerate = wf.getframerate()

    print(framerate)
    nframes = wf.getnframes()
    print(swidth)

    duration = nframes / framerate
    print(duration)

    window = np.blackman(chunk)
    content = wf.readframes(chunk)
    #samples = np.fromstring(content, dtype=types[swidth])

    k = 0
    for i in range(num_channels):
        data = content[i::num_channels]
        while len(data) == chunk * swidth:
            indata = np.array(wave.struct.unpack("%dh" % (len(data) / swidth), data))
            data = wf.readframes(chunk)
            data = data[1:len(data):2]
            if k == 0:
                k += 1
                continue
            line = [chord]
            line += [x for x in indata]
            lines.append(line)
            k += 1

cols = ['chord']
cols += range(1, chunk + 1)
df = pd.DataFrame(lines, columns=cols)
df.to_csv('data/chords.csv')
