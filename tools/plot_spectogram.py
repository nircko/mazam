import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from scipy.signal import spectrogram


def plot_spectrogram(audio_file, output_file):
    # Read the audio file
    sample_rate, audio_data = wav.read(audio_file)

    # Generate the spectrogram
    f, t, Sxx = spectrogram(audio_data, sample_rate)

    # Estimate white noise
    noise_estimation = np.mean(Sxx[:, :10], axis=1)  # Estimate using the first 10 frames

    # Plot the spectrogram
    plt.figure(figsize=(10, 5))
    plt.specgram(audio_data, Fs=sample_rate, NFFT=1024, noverlap=512, cmap='inferno')
    plt.title('Spectrogram')
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (s)')

    # Plot the white noise estimation
    # plt.plot(f, noise_estimation, color='white', linewidth=2)

    # Save the plot
    plt.savefig(output_file)
    plt.close()
