import csv
from collections import defaultdict


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
        liste_bas_prix = lower_price(liste_livres)
        liste_prix_eleves = higher_price(liste_livres)

        # On affiche les prix les moins chers par livres
        print_lower_price(liste_bas_prix)

        # On affiche les prix les moins chers par livres
        print_higher_price(liste_prix_eleves)

        # On analyse la moyenne de prix de chaque livre
        liste_prix_moyens_livres = average_price(liste_livres)

        # On affiche la moyenne des prix par livre
        print_average_price(liste_prix_moyens_livres)

        # On analyse les données globales de chaque sites
        analyse = analysing_website(
            liste_livres,
            liste_bas_prix,
            liste_prix_eleves,
            liste_prix_moyens_livres
        )

        print_analyse(analyse)


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


def initial_values():
    '''
    Cette fonction permet d'initialiser les valeurs
    du dictionnaire de chaque site
    On incrémentera les valeurs en fonction des tests
    pour déterminer le nombre de livre qui sont
    - les moins chers tout concurrent confondu
    - les plus chers tout concurrent confondu
    - moins cher que la moyenne de prix du livre
    - plus cher que la moyenne de prix du livre
    '''
    return {
        'books': 0,
        'cheapest': 0,
        'expensive': 0,
        'less_than_average': 0,
        'more_than_average': 0
    }


def analysing_website(
        sorted_books,
        lower_prices,
        higher_prices,
        average_prices):

    # On intialise notre liste de dictionnaire
    website_analyse = defaultdict(initial_values)

    for group, books in sorted_books.items():
        for book in books:
            site = book["Site"]
            titre = book["Titre"]
            prix = book["Prix"]

            # On ajoute un livre au compteur
            website_analyse[site]["books"] += 1

            # On itère sur chaque livre de notre liste des meilleurs prix
            for livre in lower_prices:
                # Si le titre et le site coincident
                if titre == livre["Titre"] and site == livre["Site"]:
                    # Alors notre site détient un des livres les moins chers
                    website_analyse[site]["cheapest"] += 1

            # On itère sur chaque livre de notre liste de livre les plus chers
            for livre in higher_prices:
                # Si le titre et le site coincident
                if titre == livre["Titre"] and site == livre["Site"]:
                    # Alors notre site détient un des livres les plus chers
                    website_analyse[site]["expensive"] += 1

            # On vérifie maintenant si le prix du livre est
            # soit inférieur à la moyenne de prix pour son titre
            for livre, moyenne_prix in average_prices.items():
                if titre == livre and float(prix) <= float(moyenne_prix):
                    website_analyse[site]["less_than_average"] += 1
                # soit supérieure à la moyenne de prix pour son titre
                elif titre == livre and float(prix) > float(moyenne_prix):
                    website_analyse[site]["more_than_average"] += 1

    return (website_analyse)


def print_analyse(analyse):
    print("\nAnalyse générales par sites :")
    for ligne, caracteristiques in analyse.items():
        print(f"{ligne} : {caracteristiques}.")
