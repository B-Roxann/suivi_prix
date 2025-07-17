# Import des fichiers .py
import extract_data as ed
import structuring_data as sd


# Ici le code du programme :
liste_concurrents = []  # Déclaration variable
liste_web = ed.web_site_list()  # On spécifie les variables pour chaque site
liste_concurrents = ed.Extract(liste_web)  # On scrap nos données
sd.write_csv_file(liste_concurrents)  # On écrits nos fichiers csv
