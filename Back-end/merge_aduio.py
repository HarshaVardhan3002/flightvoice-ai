import os
from pydub import AudioSegment

# 📂 Folder containing .wav files
INPUT_FOLDER = r"C:/Users/Von3002/Desktop/Final_year_project/Datasets/ATCO2-LIDdataset-v1_beta/LID_EVAL_EN-AU"  # Change this to your dataset folder

# 📂 Output path (Project's Main Directory)
OUTPUT_FILE = r"C:/Users/Von3002/Desktop/Final_year_project/Datasets/stitched_audio.wav"

wav_files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".wav")]
wav_files.sort()  # Sort files if needed

# Check if we have audio files
if not wav_files:
    print("No .wav files found in the dataset folder.")
    exit()

# Load and merge all audio files
stitched_audio = AudioSegment.empty()

for file in wav_files:
    file_path = os.path.join(INPUT_FOLDER, file)
    print(f"Processing: {file_path}")
    audio = AudioSegment.from_wav(file_path)
    stitched_audio += audio  # Append audio

# Save the final stitched audio
stitched_audio.export(OUTPUT_FILE, format="wav")

print(f"✅ Merged audio saved at: {OUTPUT_FILE}")