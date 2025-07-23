import csv

'''3ème partie du projet :
    Analyser les prix
- Déterminer les livres les moins chers
- Afficher les prix moyens par livre

Dans un premier temps :
    définir :
        - moins cher : < 27€
        - abordable : 27€ > prix < 33€
        - plus cher : > 33€

Dans un second temps :
    Parcourrir chaque livre de chaque site
    Les classer dans des listes "prix_bas", "prix_mediant", "plus_haut"

Enfin :
    afficher les prix moyens par livre

'''


def read_file(csv_file):
    # On lit le fichier csv
    with open(csv_file, mode="r", encoding="utf-8") as file:
        reader = list(csv.DictReader(file, delimiter=','))

        # On catégorise les prix 
        categories_prix = group_by_price(reader)
        # Puis affiche la liste de ceux au plus bas prix
        print(
            f"Les livres les moins chers sont {categories_prix['prix_bas']}"
        )

        # On analyse la moyenne de prix de chaque livre
        prix_moyens_livres = average_price(reader)
        # On itère pour l'afficher
        for livre, prix in prix_moyens_livres.items():
            print(
                f"Le prix moyen du livre {livre} "
                f"est de {prix:.2f}."
            )


def group_by_price(csv_reader):

    '''
    Cette fonction regroupe les livres par tranche de prix.

    Parameters:
        prix_bas (list) : liste qui accueil les < 27€
        prix_mediant (list) : liste qui accueil l'entre 2
        prix_haut (list) : liste qui accueil les > 33€

        montant (float) : le prix du livre parcouru

    Returns :
        comparaison_prix (dictionnaire) :
            les livres triés par prix

    '''

    comparaison_prix = dict()
    prix_bas = []
    prix_mediant = []
    prix_haut = []

    # On itère sur chaque livre dans le fichier csv
    for livre in csv_reader:
        montant = float(livre["Prix"])

        # On catégorise chaque montant
        if montant < 27:
            prix_bas.append(livre)
        elif montant > 33:
            prix_mediant.append(livre)
        else:
            prix_haut.append(livre)
    # On ajoute au dictionnaire chaque catégorie de prix
    comparaison_prix["prix_bas"] = prix_bas
    comparaison_prix["prix_mediant"] = prix_mediant
    comparaison_prix["prix_haut"] = prix_haut

    # On retourne le dictionnaire
    return comparaison_prix


def average_price(file_of_books):

    '''
    Cette fonction calcule le prix moyen de chaque livre
    et le retourne dans un dictionnaire.

    Parameters :
        livre_titre (str) : titre du livre parcouru

        prix_du_livre (float) : son prix

        nombre_d_exemplaires (int) : son nombre d'exemplaires

        moyenne_prix_livre (float) : la moyenne de prix

        prix_moyens_livres (dictionnaire) :
            Récupère les (clés) livre_titre : (valeurs) moyenne_prix_livre

    Returns : 
        prix_moyens_livres (dictionnaire)
    '''

    prix_moyens_livres = dict()

    # On itère sur chaque livre du fichier csv
    for le_livre in file_of_books:
        livre_titre = le_livre["Titre"]

        # Si le livre a déjà été analysé
        if livre_titre in prix_moyens_livres:
            continue  # On passe au prochain livre

        somme_prix_livre = 0
        nombre_d_exemplaires = 0
        moyenne_prix_livre = 0

        # On itère à nouveau pour calculer la moyenne de prix
        for livres in file_of_books:

            livres_titres = livres["Titre"]

            # Si on trouve un occurence du livre
            if livre_titre == livres_titres:
                # On ajoute le montant à la somme
                somme_prix_livre += float(livres["Prix"])
                # et on incrémente le compteur d'exemplaires
                nombre_d_exemplaires += 1
        # On se prémuni d'une erreur ZeroDivisionError
        if nombre_d_exemplaires > 0:
            # On en calcule la moyenne du prix
            moyenne_prix_livre = somme_prix_livre / nombre_d_exemplaires
        else:
            # Sinon moyenne = 0
            moyenne_prix_livre = 0
        # On ajoute le titre du livre avec son prix moyen au dictionnaire
        prix_moyens_livres[livre_titre] = moyenne_prix_livre

    # On retourne le dictionnaire
    return prix_moyens_livres
