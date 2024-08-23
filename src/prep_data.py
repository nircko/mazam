from pathlib import Path
import os
from scipy.io import wavfile
from tools.random_sample_mp3 import random_audio_sampler
from tools.plot_spectogram import plot_spectrogram
from src.sep_vocals_ica import sep_ica

input_folder=r"C:\Users\Nir Goldfriend\Documents\mazam_data"
train_sz=100
output_folder=r"C:\Users\Nir Goldfriend\Documents\mazam_train"
for tt in range(train_sz):
    _,output_file = random_audio_sampler(input_folder,output_folder)
    file_path = Path(output_file)
    # Get the parent directory
    parent_folder = file_path.parent
    # Get the filename without extension
    filename = file_path.stem
    # Get the file extension
    extension = file_path.suffix
    S_vocals, _, sample_rate = sep_ica(output_file)
    # Save the separated signals (normalized to 16-bit)
    wav_outfile=os.path.join(parent_folder,filename + '_ica_vocals' + extension)
    wavfile.write(wav_outfile, sample_rate, S_vocals)
    plot_spectrogram(wav_outfile,os.path.join(parent_folder,filename + '_spectrogram' + '.tiff'))




