from collections import defaultdict

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
