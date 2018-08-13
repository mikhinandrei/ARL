# ToDo: install sklearn
# ToDo: write ML for recognizing chords

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from lib.musicman import *
import matplotlib.pyplot as plt

fname = 'data/test/wonderwall.wav'

chunk = 2500

if fname.split('.')[-1] != 'wav':
    import soundfile as sf

    data, samplerate = sf.read(fname)
    sf.write('data/test/temp.wav', data, samplerate)
    fname = 'data/test/temp.wav'

wf = wave.open(fname, 'r')

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

music_notes = load_data()
harm = get_harmony(music_notes, wf, chunk)
print(harm)

if harm[-1] == 'm':
    harm = NOTES[(NOTES.index(harm[:-1]) + 3) % 12]

chords = [harm,
          NOTES[(NOTES.index(harm) + 2) % 12] + 'm',
          #NOTES[(NOTES.index(harm) + 4) % 12], #NOTES[(NOTES.index(harm) + 4) % 12] + 'm',
          NOTES[(NOTES.index(harm) + 5) % 12], #NOTES[(NOTES.index(harm) + 5) % 12] + 'm',
          NOTES[(NOTES.index(harm) + 7) % 12],
          NOTES[(NOTES.index(harm) + 9) % 12] + 'm'
]

print(chords)
# ================================================================
df = pd.read_csv('data/chords.csv')
df = df.loc[df['chord'].isin(chords)]
print('selected')

lel = df.loc[:,'1':]

X_train, X_test, y_train, y_test = train_test_split(lel, df.chord)

dt = MLPClassifier(alpha=1)
dt.fit(X_train, y_train)
pred = dt.predict(X_test)

print(accuracy_score(pred, y_test))
# =================================================================

wf = wave.open(fname, 'r')
ins = []
for i in range(num_channels):
    data = content[i::num_channels]
    while len(data) == chunk * swidth:
        ll = np.array(wave.struct.unpack("%dh" % (len(data) / swidth), data))
        plt.plot(ll, 'g')
        plt.show()
        ins.append(ll)
        data = wf.readframes(chunk)
        data = data[1:len(data):2]

pred = dt.predict(ins)

chords_per_second = len(pred) / duration
print(chords_per_second)

new_v = []

z = 1
while z + 4 < len(pred):
    buf = pred[z:z+4]
    print(buf)
    z += 4