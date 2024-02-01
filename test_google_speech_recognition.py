import moviepy.editor as mp
import speech_recognition as sr
import tempfile
import re
import os 
import matplotlib.pyplot as plt
import Levenshtein

# Initialiser le reconnaisseur de la parole
recognizer = sr.Recognizer()

# Specify the directory containing audio files
audio_directory = r"C:\\Users\\ASUS\\Desktop\\Dataset\\audio"

# List all audio files in the directory
audio_files = [f for f in os.listdir(audio_directory) if f.endswith(".wav")]

# Initialize variables for accuracy calculation
total_accuracy = 0.0
total_loss = 0.0
total_files = 0
accuracy_list=[]


# Iterate through each audio file
for audio_file in audio_files:
    audio_path = os.path.join(audio_directory, audio_file)

    # Transcribe the current audio file
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        try:
            detected_words = recognizer.recognize_google(audio, language="en").lower().split()
        except sr.UnknownValueError:
            print(f"Google Speech Recognition n'a pas pu comprendre {audio_file}")
            accuracy = 0.0
            continue
        except sr.RequestError as e:
            print(f"Erreur lors de la requête à l'API Google Speech Recognition pour {audio_file}: {e}")
            accuracy = 0.0
            continue

 

    # Read corresponding text file
    txt_file_path = os.path.join(audio_directory, audio_file.replace(".wav", ".txt"))
    with open(txt_file_path, "r") as txt_file:
        target_words = txt_file.read().lower().split()

    # Compare transcribed text with target text
    accuracy = 0.0
    # Calculate accuracy based on detected words
    correct_words = [word for word in detected_words if word in target_words]
    accuracy = (len(correct_words) / len(target_words)) * 100 if len(target_words) > 0 else 0.0
    print(f"Précision pour {audio_file}: {accuracy:.2f}%")
    print(detected_words)
    accuracy_list.append(accuracy)
    # Calculate loss using Levenshtein distance
    loss = Levenshtein.distance(" ".join(detected_words), " ".join(target_words))


    # Accumulate accuracy for averaging
    total_accuracy += accuracy
    total_loss += loss
    total_files += 1

# Calculate average accuracy
average_accuracy = total_accuracy / total_files if total_files > 0 else 0.0
print(f"Précision moyenne pour tous les fichiers: {average_accuracy}%")
average_loss = total_loss / total_files if total_files > 0 else 0.0
print(f"Loss moyenne pour tous les fichiers: {average_loss}")
"""
# Plot the accuracies
plt.figure(figsize=(10, 6))
plt.plot(range(1, total_files + 1), accuracy_list, marker='o', linestyle='-', color='b')
plt.xlabel('Fichier audio')
plt.ylabel('Précision (%)')
plt.title('Précision de la reconnaissance vocale par fichier')
plt.xticks(range(1, total_files + 1))
plt.grid(True)
plt.tight_layout()
plt.show()
"""