import csv
from collections import defaultdict

'''3ème partie du projet :
    Analyser les prix
- Déterminer les livres les moins chers
- Afficher les prix moyens par livre
'''


def read_file(csv_file):
    '''
    Cette fonction va analyser le fichier csv pour en extraire :
        - La liste de livre
        - Le prix le plus bas de chaque livre
        - Le prix moyen de chaque titre commun

    Parameters:
        liste_livres (list): liste de dictionnaires
        prix_moyens_livres (list): liste de dictionnaires
    '''

    # On lit le fichier csv
    with open(csv_file, mode="r", encoding="utf-8") as file:
        reader = list(csv.DictReader(file, delimiter=','))

        # On créé notre liste de livres triée
        liste_livres = sort_by_price(sort_by_name(reader))

        # On analyse les prix des livres
        # et on affiche les prix les moins chers par livres
        lower_price(liste_livres)

        # On analyse la moyenne de prix de chaque livre
        prix_moyens_livres = average_price(liste_livres)

        # On affiche la moyenne des prix par livre
        print_average_price(prix_moyens_livres)


def sort_by_name(reader):
    '''
    Cette fonction construit l'objet defaultDict
    soit le dictionnaire des livres triés par leur noms

    Parameters:
    reader : objet DictReader sous forme de liste
    liste_livres (list): liste de dictionnaires

    returns : liste_livres
    '''
    # On initialise notre defaultDict
    liste_livres = defaultdict(list)

    # On construit liste_livres en regroupant les livres par titres
    for livre in reader:
        titre = livre["Titre"]
        liste_livres[titre].append(livre)

    return liste_livres


def sort_by_price(list_of_books):

    '''
    Cette fonction tri les livres par prix
    dans chaque groupe de livre.

    Parameters:
        file_of_books (object DictReader) : dictionnaires de livres

    Returns :
        new_sorted_list
    '''
    new_sorted_list = defaultdict(list)
    for group, books in list_of_books.items():
        sorted_books = sorted(books, key=lambda book: book["Prix"])
        for book in range(len(books)):
            books[book] = sorted_books[book]
        # Aurait pu être remplacé par books[:] = sorted_books
        # pour une modification "in-place"
        new_sorted_list[group] = books

    # On retourne la nouvelle liste de dictionnaires
    return new_sorted_list


def lower_price(file_of_books):
    '''
    Cette fonction affiche pour chaque livre
    sur quel site il est moins cher,
    et à quel prix.
    '''
    for group, books in file_of_books.items():
        print(
            f'Le livre "{books[0]["Titre"]}" '
            f'est moins cher chez {books[0]["Site"]}, '
            f'au prix de {books[0]["Prix"]}{books[0]["Devise"]}.'
        )


def average_price(file_of_books):

    '''
    Cette fonction calcule le prix moyen de chaque livre
    et le retourne dans un dictionnaire.

    Parameters :
        somme_totale (int)
        moyenne_prix (int)
        nombre_exemplaires (int)
        prix_moyens_livres (dictionnaire)

    Returns :
        le dictionnaire de chaque livre avec son prix
        moyen : prix_moyens_livres
    '''
    prix_moyens_livres = dict()

    for group, books in file_of_books.items():
        # On intialise les variables
        somme_totale = 0
        moyenne_prix = 0
        nombre_exemplaires = 0
        # On itère sur chaque livre pour calculer notre moyenne
        for book in books:
            # On récupère le prix du livre parcouru
            prix = float(book["Prix"])

            # On ajoute le prix du livre au total
            somme_totale += prix

            # On incrémente notre compteur d'exemplaires
            nombre_exemplaires += 1

        # On se prémuni de l'erreur ZeroDivisionError
        if nombre_exemplaires == 0:
            moyenne_prix = 0
        else:
            moyenne_prix = somme_totale / nombre_exemplaires

        # On ajoute le tout à notre liste
        # en s'assurant que la moyenne reste à 2 décimales
        # après la virgule
        prix_moyens_livres[group] = f"{moyenne_prix:.2f}"

    # On retourne notre liste de prix moyens par livres
    return prix_moyens_livres


def print_average_price(list_of_average_price):

    '''
    Cette fonction affiche le prix moyen de chaque livre
    qui ont le même titre
    '''
    # On parcour notre liste de livre
    # pour afficher le titre du livre et son prix moyen
    for livre, prix in list_of_average_price.items():
        print(
            f"Le prix moyen du livre {livre} "
            f"est de {prix}€."
        )
