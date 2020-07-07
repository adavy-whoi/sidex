import matplotlib.pyplot as plt
import numpy as np

PPS_data = []

# we'll be using channel 13 data (index 12)

selected_channel = 12
with open('./Sidex_20200127T235718p525826.txt', 'r') as f:
	for i, line in enumerate(f.readlines()):
	#if i >= 2: automatically? skip first two lines
		channel_data = line.split(',')
		PPS_data.append(float(channel_data[selected_channel]))

#print(PPS_data[2])

dt = 0.001
file_length_seconds = 60.0
t = np.linspace(0.0, 60000.0, len(PPS_data))
x = PPS_data
NFFT = 1024  # the length of the windowing segments
Fs = int(1.0 / dt)  # the sampling frequency

fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.plot(t, x)
Pxx, freqs, bins, im = ax2.specgram(x, NFFT=NFFT, Fs=Fs)
# The `specgram` method returns 4 objects. They are:
# - Pxx: the periodogram
# - freqs: the frequency vector
# - bins: the centers of the time bins
# - im: the matplotlib.image.AxesImage instance representing the data in the plot
plt.show()

