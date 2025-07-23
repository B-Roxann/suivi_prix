# Import des fichiers .py
import extract_data as ed
import structuring_data as sd
import analysing_data as ad

# Ici le code du programme :
liste_concurrents = []  # Déclaration variable
liste_web = ed.web_site_list()  # On spécifie les variables pour scraper
liste_concurrents = ed.Extract(liste_web)  # On scrap nos données
sd.write_csv_file(liste_concurrents)  # On écrits notre fichier csv
ad.read_file("csv/prix_concurrents.csv")  # On analyse nos données
