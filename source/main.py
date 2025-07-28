# Import des fichiers .py
import extract_data as ed
import structuring_data as sd
import analysing_data as ad
import analysing_rivalry as ar

# Ici le code du programme :

# Première partie du programme : scraping des données
liste_concurrents = []  # Déclaration variable
liste_web = ed.web_site_list()  # On spécifie les variables pour scraper
liste_concurrents = ed.Extract(liste_web)  # On scrap nos données

# Seconde partie du programme : Structuration des données en .csv
sd.write_csv_file(liste_concurrents)  # On écrits notre fichier csv

# Troisième partie du programme : Analyse des prix
reader = ad.read_file("csv/prix_concurrents.csv")  # On lit le .csv
liste_livres = ad.sort_by_price(ad.sort_by_name(reader))  # Liste triée
liste_bas_prix = ad.lower_price(liste_livres)  # Prix les plus bas
liste_prix_eleves = ad.higher_price(liste_livres)  # Prix les plus hauts
liste_prix_moyens_livres = ad.average_price(liste_livres)  # Moyenne prix

# Quatrième partie du programme : détecter un concurrent + ou - cher
analyse = ar.analysing_website(
    liste_livres,
    liste_bas_prix,
    liste_prix_eleves,
    liste_prix_moyens_livres
)  # Analyse globale pour chaque site

# Cinquième partie du programme : 
#  Affichage de toutes les informations récoltées
ad.print_lower_price(liste_bas_prix)
ad.print_higher_price(liste_prix_eleves)
ad.print_average_price(liste_prix_moyens_livres)
ar.print_analyse(analyse)