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


def plot_clean_spectrogram(audio_file, save_path=None):
    """
    Plots a spectrogram without axes or whitespace.
    """
    # Read the audio file
    sample_rate, audio_data = wav.read(audio_file)

    # Generate the spectrogram
    times, frequencies, Sxx = spectrogram(audio_data, sample_rate)

    # Create a figure and axis with no frame
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the spectrogram
    ax.pcolormesh(times, frequencies, 10 * np.log10(Sxx), shading='gouraud')

    # Remove the axes, ticks, and labels
    ax.axis('off')

    # Remove whitespace around the plot
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    if save_path:
        # Save the figure without any whitespace
        plt.savefig(save_path, bbox_inches='tight', pad_inches=0)
        plt.close(fig)
    else:
        # Display the figure without any whitespace
        plt.show()

# Example usage:
# To display the plot:
# plot_clean_spectrogram(times, frequencies, Sxx)

# To save the plot:
# plot_clean_spectrogram(times, frequencies, Sxx, save_path="spectrogram.png")
