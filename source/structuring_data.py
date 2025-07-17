import csv


'''2nde partie du projet :
   Structurer les données dans un fichier CSV

Dans un premier temps:
    On va créer un fichier avec le nom du site

Dans un second temps:
    On va créer les en-tetes du fichier csv : titre, prix

Enfin:
    On va écrire grâce à une boucle dans le fichier csv
'''


# Organisation des informations
def organise_book_price(liste_livres):
    titre_livre = []
    prix_livre = []
    # On itère sur chaque site pour en extraire
    for livre, prix in liste_livres.items():

        # Les titres des livres
        titre_livre.append(livre)

        # Les prix des livres
        prix_livre.append(prix["prix :"])
    return titre_livre, prix_livre


# Ecriture d'un fichier csv par site web
def write_csv_file(liste_concurrents):
    en_tete = ["Titre", "Prix"]

    # Pour chaque site, on va créer un fichier .csv
    for site_concurrent, livres in liste_concurrents.items():
        with open(
            f"csv/{site_concurrent}.csv",
            mode="w+",
            encoding="utf-8",
            newline=""
        ) as csv_file:

            # on prépare notre csv.writer
            writer_csv = csv.writer(csv_file, delimiter=',')

            # On ajoute les en-têtes
            writer_csv.writerow(en_tete)

            # On organise les données "titre" et "prix"
            titre_livre, prix_livre = organise_book_price(livres)

            # On itère pour ajouter ces données à notre csv
            for titre, prix in zip(titre_livre, prix_livre):
                writer_csv.writerow([titre, prix])
