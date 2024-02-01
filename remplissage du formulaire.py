import speech_recognition as sr
import re

# Initialiser le reconnaisseur de la parole
recognizer = sr.Recognizer()
# Transcrire la piste audio en texte
with sr.AudioFile(r"C:\\Users\\ASUS\\Desktop\\Caustaza\Date Issued 21 04 20 (1).wav") as source:
    audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        print("Texte extrait de l'audio :")
        print(text)

      # Exemple d'extraction d'entités
        extracted_data = {
            'Date Issued': re.search(r'date issued (.+?) date due', text),
            'Date Due': re.search(r'date due(.+?) invoice status', text),
            'Invoice Status': re.search(r'invoice status (\S+)', text),
            'Service': re.search(r'service (.+?) balance', text),
            'Balance': re.search(r'balance (\d+)', text),
            'Item Name': re.search(r'item name (.+?) item description', text),
            'Item Description': re.search(r'item description (.+?) cost', text),
            'Cost': re.search(r'cost \$?(\d+)', text),
            'Hours': re.search(r'hours (\d+)', text),
            'Sales person': re.search(r'salesperson (.+?) thanks for your business', text),
            'Thanks for your business': re.search(r'thanks for your business (\S+ .+?) discount', text),
            'Discount': re.search(r'discount (\d+)', text),
            'Tax': re.search(r'tax (\d+)', text),
        }


        # Exemple de remplissage du formulaire
        form_data = {}
        for field, match in extracted_data.items():
            if match is not None:
                form_data[field] = match.group(1) 
            else:
                form_data[field] = None

        # Afficher le formulaire rempli
        print("Formulaire rempli :")
        for field, value in form_data.items():
            print(f"{field}: {value}")

    except sr.UnknownValueError:
        print("Google Speech Recognition n'a pas pu comprendre l'audio")
    except sr.RequestError as e:
        print(f"Erreur lors de la requête à l'API Google Speech Recognition : {e}")
