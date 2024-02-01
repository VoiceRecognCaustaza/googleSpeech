import moviepy.editor as mp
import speech_recognition as sr
import tempfile
import re

# Initialiser le reconnaisseur de la parole
recognizer = sr.Recognizer()
mot_a_chercher = input("donnee  mot qui recherche ")
# Transcrire la piste audio en texte
with sr.AudioFile(r"C:\\Users\\ASUS\\Desktop\\Dataset\\audio\\0f119ce2-c824-4bbe-8da1-253b8a79c4bb.wav") as source:
    audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        print("Texte extrait de l'audio :")
        print(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition n'a pas pu comprendre l'audio")
    except sr.RequestError as e:
        print("Erreur lors de la requête à l'API Google Speech Recognition : {0}".format(e))
"""
# Supprimer le fichier audio temporaire
import os
os.remove(temp_audio_filename)
"""