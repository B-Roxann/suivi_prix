import csv
from collections import defaultdict


def read_file(csv_file):
    '''
    Cette fonction lit le fichier csv afin qu'on l'analyse.
    '''

    # On lit le fichier csv
    with open(csv_file, mode="r", encoding="utf-8") as file:
        reader = list(csv.DictReader(file, delimiter=','))

        return reader


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
    Cette fonction récupère dans une liste
    pour chaque livre son prix le plus bas
    '''
    cheapest_price_by_book = []

    for group, books in file_of_books.items():

        cheapest_price_by_book.append(books[0])

    return cheapest_price_by_book


def print_lower_price(list_of_books):
    '''
    Cette fonction affiche pour chaque livre
    sur quel site il est moins cher,
    et à quel prix.
    '''
    print("\nAnalyse des données : Prix le moins cher par livres")

    for livre in list_of_books:

        titre = livre["Titre"]
        site = livre["Site"]
        prix = livre["Prix"]
        devise = livre["Devise"]

        print(
            f'Le livre "{titre}" '
            f'est moins cher chez {site}, '
            f'au prix de {prix}{devise}.'
        )


def higher_price(file_of_books):
    '''
    Cette fonction récupère dans une liste
    pour chaque livre son prix le plus élevé
    '''
    expensive_price_by_book = []

    for group, books in file_of_books.items():

        expensive_price_by_book.append(books[-1])

    return expensive_price_by_book


def print_higher_price(list_of_books):
    '''
    Cette fonction affiche pour chaque livre
    sur quel site il est plus cher,
    et à quel prix.
    '''
    print("\nAnalyse des données : Prix le plus élevé par livres")

    for livre in list_of_books:

        titre = livre["Titre"]
        site = livre["Site"]
        prix = livre["Prix"]
        devise = livre["Devise"]

        print(
            f'Le livre "{titre}" '
            f'est plus cher chez {site}, '
            f'au prix de {prix}{devise}.'
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

    print("\nAnalyse des données : Prix moyens par livres")
    # On parcour notre liste de livre
    # pour afficher le titre du livre et son prix moyen
    for livre, prix in list_of_average_price.items():
        print(
            f'Le prix moyen du livre "{livre}" '
            f'est de {prix}€.'
        )
