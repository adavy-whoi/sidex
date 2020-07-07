import matplotlib.pyplot as plt
import numpy as np

hydrophone_data = []

# we'll be using channel 1 data (or 0 because it's 0 indexed)

start_channel = 13
end_channel = 16

for j in range(start_channel, end_channel):
	data = []
	with open('./Sidex_20200127T235718p525826.txt', 'r') as f:
		for i, line in enumerate(f.readlines()):
		#if i >= 2: automatically? skip first two lines
				channel_data = line.split(',')
				data.append(float(channel_data[j]))
		#print(data)
		hydrophone_data.append(data)
		dt = 0.001
		file_length_seconds = 60.0
		t = np.linspace(0.0, 60000.0, len(data))
		x = data
		NFFT = 1024  # the length of the windowing segments
		Fs = int(1.0 / dt)  # the sampling frequency

		fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4)
		ax1.plot(t, x)
		Pxx, freqs, bins, im = ax2.specgram(x, NFFT=NFFT, Fs=Fs, vmin=-150, vmax=-50)
		# The `specgram` method returns 4 objects. They are:
		# - Pxx: the periodogram
		# - freqs: the frequency vector
		# - bins: the centers of the time bins
		# - im: the matplotlib.image.AxesImage instance representing the data in the plot
		ax3.psd(Pxx, NFFT, Fs)
		Pxx, freqs, bins, im = ax4.specgram(x, NFFT=NFFT, Fs=Fs)
		plt.show()
		#choice = input('Type yes or no to save file')
		#if 'y' in choice.lower():
			#plt.savefig('hydrophone_data_{}.png'.format(j))


#print(hydrophone_data[1][0])

