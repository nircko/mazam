import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal as sg
from sklearn.decomposition import FastICA

import random

def sep_ica(path_of_wav):
    """
    :param path_of_wav: full path to wav files
    :return:
    """
    # Load the WAV file
    sample_rate, y = wavfile.read(path_of_wav)
    # Ensure the signal is in the right shape (2D: samples x channels)
    if len(y.shape) == 1:
        y = np.expand_dims(y, axis=1)

    # Normalize the audio signal
    y = y.astype(np.float32)
    y -= y.mean(axis=0)

    # Apply FastICA
    ica = FastICA(n_components=2, random_state=0)
    S_ = ica.fit_transform(y)  # Reconstruct signals
    S_vocals = normalize_signal(S_[:, 0])
    S_accompaniment = normalize_signal(S_[:, 1])

    return S_vocals,S_accompaniment,sample_rate


# Normalize the separated signals to be in the 16-bit integer range
def normalize_signal(signal):
    signal = signal / np.max(np.abs(signal))  # Normalize to [-1, 1]
    return np.int16(signal * 32767)  # Convert to 16-bit PCM

# Function to plot the spectrogram
def plot_spectrogram(signal, sample_rate,title="Spectrogram", save_path=None):
    frequencies, times, Sxx = sg.spectrogram(signal, sample_rate)
    plt.figure(figsize=(10, 6))
    plt.pcolormesh(times, frequencies, 10 * np.log10(Sxx), shading='gouraud')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.colorbar(label='Intensity [dB]')
    plt.title(title)
    plt.show()

def export_ica(path_of_wav):
    S_vocals, S_accompaniment, sample_rate = sep_ica(path_of_wav)
    # Save the separated signals (normalized to 16-bit)
    wavfile.write('output_vocals'+path_of_wav, sample_rate, S_vocals)
    # wavfile.write('output_accompaniment.wav', sample_rate, S_accompaniment)


if __name__ == '__main__':
    path_of_wav = r"C:\Users\Nir Goldfriend\Downloads\Lynyrd Skynyrd - Sweet Home Alabama.wav"
    duration_sample = 6  # in seconds
    sample_rate, y = wavfile.read(path_of_wav)
    S_vocals, sample_rate = sep_ica(path_of_wav=path_of_wav)
    # Plot the spectrograms
    plot_spectrogram(y[:, 0], sample_rate, 'Original Signal (Channel 1)')
    plot_spectrogram(S_vocals, sample_rate, 'Separated Signal 1 (Likely Vocals)')
