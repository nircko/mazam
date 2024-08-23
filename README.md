# maZam - Singer Recognition Using Transfer Learning with Spectrograms post ICA

---

## Project Overview

This project showcases the application of transfer learning to retrain an existing neural network for singer recognition. The model is trained on spectrograms—visual representations of audio signals—to learn how to identify different artists based on their voice characteristics.

---

## Prerequisites

Before running the scripts, make sure you have the following installed:

- **Python 3.9**: Download and install Python 3.9 from [python.org](https://www.python.org/downloads/release/python-390/).
- **FFmpeg**: Required for audio processing tasks. Install FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html) and ensure it is added to your system's PATH.
- **Python Packages**: Install the required Python packages by running the setup script.
---

## Setup Instructions

**Setup Mac**:
   ```bash
   setup.sh
```
**Setup windows**:
   ```bash
   setup.bat
```


## Organize you dataset
```bash
dataset/
  ├── artist_1/
  │   ├── song1_spectrogram.png
  │   ├── song2_spectrogram.png
  ├── artist_2/
  │   ├── song1_spectrogram.png
  │   ├── song2_spectrogram.png
  
```bash
