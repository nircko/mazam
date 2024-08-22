path_of_wav=r"C:\Users\Nir Goldfriend\Downloads\Lynyrd Skynyrd - Sweet Home Alabama.wav"
duration_sample = 6  # in seconds

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal as sg
from sklearn.decomposition import FastICA
import random

# Load the WAV file
sample_rate, y = wavfile.read(path_of_wav)
print('sample_rate:',sample_rate)

# Define the duration to sample (duration_sample seconds) and the max start time
sample_duration = duration_sample * sample_rate #
max_start_time = len(y) - sample_duration

print('max_start_time:',max_start_time)

# Randomly select a start time
start_time = random.randint(0, max_start_time)

# Extract the duration_sample-second segment
sampled_audio = y[start_time:start_time + sample_duration]

y=sampled_audio

# Ensure the signal is in the right shape (2D: samples x channels)
if len(y.shape) == 1:
    y = np.expand_dims(y, axis=1)

# Normalize the audio signal
y = y.astype(np.float32)
y -= y.mean(axis=0)

# Apply FastICA
ica = FastICA(n_components=2, random_state=0)
S_ = ica.fit_transform(y)  # Reconstruct signals

# Normalize the separated signals to be in the 16-bit integer range
def normalize_signal(signal):
    signal = signal / np.max(np.abs(signal))  # Normalize to [-1, 1]
    return np.int16(signal * 32767)  # Convert to 16-bit PCM

S_vocals = normalize_signal(S_[:, 0])
S_accompaniment = normalize_signal(S_[:, 1])

# Function to plot the spectrogram
def plot_spectrogram(signal, sample_rate, title):
    frequencies, times, Sxx = sg.spectrogram(signal, sample_rate)
    plt.figure(figsize=(10, 6))
    plt.pcolormesh(times, frequencies, 10 * np.log10(Sxx), shading='gouraud')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.colorbar(label='Intensity [dB]')
    plt.title(title)
    plt.show()

# Plot the spectrograms
plot_spectrogram(y[:, 0], sample_rate, 'Original Signal (Channel 1)')
plot_spectrogram(S_[:, 0], sample_rate, 'Separated Signal 1 (Likely Vocals)')
plot_spectrogram(S_[:, 1], sample_rate, 'Separated Signal 2 (Likely Accompaniment)')

# Save the separated signals (normalized to 16-bit)
wavfile.write('output_vocals.wav', sample_rate, S_vocals)
wavfile.write('output_accompaniment.wav', sample_rate, S_accompaniment)
