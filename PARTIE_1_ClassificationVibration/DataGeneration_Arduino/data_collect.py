import serial
import csv
import time

# Ouverture du port série
ser = serial.Serial('COM3', 115200)
time.sleep(2)  # Attendre que la connexion série soit établie

# Création du fichier CSV et écriture de l'en-tête
with open("vibrations.csv", mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["X", "Y", "Z", "Label"])  # En-tête du fichier CSV

    print("Collecte des données en cours... Appuyez sur Ctrl+C pour arrêter. :)")
    
    try:
        # Lecture continue des données depuis le port série
        while True:
            # Lire la ligne de données, la décoder et la nettoyer
            li
