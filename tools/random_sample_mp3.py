import os
import random
import sys
from pydub import AudioSegment


def random_audio_sampler(input_folder, output_folder=None):
    # Get all mp3 files in the input folder
    mp3_files = [f for f in os.listdir(input_folder) if f.endswith('.mp3')]

    if not mp3_files:
        print("No MP3 files found in the specified folder.")
        return
    else:
        print(len(mp3_files))

    # Randomly select one MP3 file
    selected_file = random.choice(mp3_files)
    selected_file_path = os.path.join(input_folder, selected_file)

    # Load the selected MP3 file
    audio = AudioSegment.from_mp3(selected_file_path)

    # Define the duration to sample (29 seconds) and the max start time
    sample_duration = 29 * 1000  # in milliseconds
    max_start_time = len(audio) - sample_duration

    if max_start_time <= 0:
        print("The audio file is shorter than 29 seconds.")
        return

    # Randomly select a start time
    start_time = random.randint(0, max_start_time)

    # Extract the 29-second segment
    sampled_audio = audio[start_time:start_time + sample_duration]
    if output_folder is not None:
        output_file=os.path.join(output_folder,selected_file + f'{start_time}_{sample_duration}sec.wav')
        # Save the sampled segment as a new MP3 file
        sampled_audio.export(output_file, format="wav")
        print(f"Sampled audio saved to {output_file}")
        return sampled_audio,output_file
    else:
        return sampled_audio


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python random_audio_sampler.py <input_folder> <output_file>")
    else:
        input_folder = sys.argv[1]
        output_file = sys.argv[2]
        random_audio_sampler(input_folder, output_file)