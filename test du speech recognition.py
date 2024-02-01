import moviepy.editor as mp
import speech_recognition as sr
import tempfile
import re
import os 

# Initialiser le reconnaisseur de la parole
recognizer = sr.Recognizer()

# Specify the directory containing audio files
audio_directory = r"C:\\Users\\ASUS\\Desktop\\Dataset\\audio"

# List all audio files in the directory
audio_files = [f for f in os.listdir(audio_directory) if f.endswith(".wav")]

# Initialize variables for accuracy calculation
total_accuracy = 0.0
total_files = 0

# Iterate through each audio file
for audio_file in audio_files:
    audio_path = os.path.join(audio_directory, audio_file)

    # Transcribe the current audio file
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)  # You may need to specify the language code
        except sr.UnknownValueError:
            print(f"Google Speech Recognition n'a pas pu comprendre {audio_file}")
            continue
        except sr.RequestError as e:
            print(f"Erreur lors de la requête à l'API Google Speech Recognition pour {audio_file}: {e}")
            continue
    # Specify the directory containing audio files
    txt_directory = r"C:\\Users\\ASUS\\Desktop\\Dataset\\txt"
    # Read corresponding text file
    txt_file_path = os.path.join(txt_directory, audio_file.replace(".wav", ".txt"))
    with open(txt_file_path, "r") as txt_file:
        target_text = txt_file.read()

    # Compare transcribed text with target text
    accuracy = 0.0
    if target_text.lower() == text.lower():
        accuracy = 100.0

    print(f"Précision pour {audio_file}: {accuracy}%")
    
    # Accumulate accuracy for averaging
    total_accuracy += accuracy
    total_files += 1

# Calculate average accuracy
average_accuracy = total_accuracy / total_files if total_files > 0 else 0.0
print(f"Précision moyenne pour tous les fichiers: {average_accuracy}%")