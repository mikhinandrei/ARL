# ToDo: ML для определения размерности
# ToDo: multitrack
# ToDo: убрать шлаковые ноты

import wave
from KARL.Utilities.Supplier import *
from KARL.musicman import *

types = {
    1: np.int8,
    2: np.int16,
    4: np.int32
}

music_notes = load_data('data/data.csv')

chunk = 2500
# open up a wave
wf = wave.open('data/test/reco/gravity.wav', 'r')

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

print(get_harmony(music_notes, wf, chunk))

for i in range(num_channels):
    data = content[i::num_channels]
    while len(data) == chunk * swidth:
        indata = np.array(wave.struct.unpack("%dh" % (len(data) / swidth), data)) * window
        #plt.plot(indata, 'g')
        #plt.show()
        fftData = abs(np.fft.rfft(indata)) ** 2
        fftData = np.array(list(filter(lambda x: x > 0, fftData)))
        if len(fftData) == 0:
            data = wf.readframes(chunk)
            data = data[1:len(data):2]
            continue
        # find the maximum
        which = fftData[1:].argmax() + 1
        # use quadratic interpolation around the max
        if which != len(fftData) - 1:
            y0y, y1y, y2y = np.log(fftData[which - 1:which + 2])
            x1y = (y2y - y0y) * .5 / (2 * y1y - y2y - y0y)
            # find the frequency and output it
            y = (which + x1y) * framerate / chunk
            print(y, get_sound_note(music_notes, y))
        else:
            x = which * framerate / chunk
            print(y, get_sound_note(music_notes, y))
        # read some more data
        data = wf.readframes(chunk)
        data = data[1:len(data):2]
    print('=' * 50)
