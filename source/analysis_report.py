
def create_report(
            list_of_lower_prices,
            list_of_higher_prices,
            list_of_average_prices,
            analyse
        ):
    with open("rapport.txt", mode="w+", encoding="utf-8") as file:
        file.write(print_lower_price(list_of_lower_prices))
        file.write(print_higher_price(list_of_higher_prices))
        file.write(print_average_price(list_of_average_prices))
        file.write(print_analyse_by_website(analyse))
        file.write(marketing_takeaways(list_of_average_prices))


def print_lower_price(list_of_books):
    '''
    Cette fonction concatène les lignes à insérer au rapport
    pour chaque livre sur quel site il est moins cher,
    et à quel prix.
    '''
    # On créé la variable qui va contenir tout le texte
    # a insérer au rapport
    lower_price = "Analyse des données : Prix le moins cher par livres"

    # On itère pour chaque livre et concatène le texte
    for livre in list_of_books:

        titre = livre["Titre"]
        site = livre["Site"]
        prix = livre["Prix"]
        devise = livre["Devise"]

        lower_price += (
            f'\nLe livre "{titre}" '
            f'est moins cher chez {site}, '
            f'au prix de {prix}{devise}.'
        )
    # On retourne nos lignes à insérer au rapport
    return lower_price


def print_higher_price(list_of_books):
    '''
    Cette fonction concatène les lignes à insérer au rapport
    pour chaque livre sur quel site il est plus cher,
    et à quel prix.
    '''
    # On créé la variable qui va contenir tout le texte
    # a insérer au rapport
    higher_price = "\n\nAnalyse des données : Prix le plus élevé par livres"

    # On itère pour chaque livre et concatène le texte
    for livre in list_of_books:

        titre = livre["Titre"]
        site = livre["Site"]
        prix = livre["Prix"]
        devise = livre["Devise"]

        higher_price += (
            f'\nLe livre "{titre}" '
            f'est plus cher chez {site}, '
            f'au prix de {prix}{devise}.'
        )
    # On retourne nos lignes à insérer au rapport
    return higher_price


def print_average_price(list_of_average_price):

    '''
    Cette fonction concatène les lignes à insérer au rapport
    sur le prix moyen de chaque livre qui ont un titre commun
    '''
    # On créé la variable qui va contenir tout le texte
    # a insérer au rapport
    average_price = "\n\nAnalyse des données : Prix moyens par livres"

    # On parcour notre liste de livre
    # pour concaténer le titre du livre et son prix moyen
    for livre, prix in list_of_average_price.items():
        average_price += (
            f'\nLe prix moyen du livre "{livre}" '
            f'est de {prix}€.'
        )
    # On retourne nos lignes à insérer au rapport
    return average_price


def print_analyse_by_website(analyse):

    '''
    Cette fonction concatène les lignes à insérer au rapport
    sur l'analyse effectuée par concurrent
    '''
    # On créé la variable qui va contenir tout le texte
    # a insérer au rapport
    analysis = ("\n\nAnalyse générales par sites :")

    for ligne, caracteristiques in analyse.items():

        # On initialise nos variables
        books = caracteristiques["books"]
        cheapest = caracteristiques["cheapest"]
        expensive = caracteristiques["expensive"]
        less_average = caracteristiques["less_than_average"]
        more_average = caracteristiques["more_than_average"]

        # On commence à initialiser notre variable
        analysis += (f"\nLe site {ligne} est ")

        # Puis on y rajoute s'il a des prix les plus chers
        # ou les moins chers
        if cheapest > books / 2:
            analysis += (
                f"moins cher pour {cheapest} "
                f"sur {books} livres étudiés,\n"
            )
        elif expensive > books / 2:
            analysis += (
                f"plus cher pour {expensive} "
                f"sur {books} livres étudiés,\n"
            )
        else:
            analysis += (
                f"situé dans la moyenne du marché "
                f"sur {books} livres étudiés,\n"
            )

        # Et enfin s'il est généralement plus cher
        # ou moins cher
        if less_average > books / 2:
            analysis += (
                "et pratique des tarifs généralement "
                "inférieurs à la tendance observée."
            )
        elif more_average > books / 2:
            analysis += (
                "et pratique des prix plus élevés que "
                "la tendance générale."
            )
    # On retourne nos lignes à insérer au rapport
    return analysis


def marketing_takeaways(list_of_average_prices):
    '''
    Cette fonction ajoute à notre rapport
    nos conseils marketing en se positionnant 0.10€ moins cher
    que le prix moyen du marché, en arrondissant au supérieur.
    exemple 25.47 => 25.37 => 25.40
    afin de rester compétitif sans rogner notre marge.
    '''

    # On commence par initialiser notre variable
    takeaways = "\n\nConclusions marketing :"

    # On itère sur chaque livre afin d'en donner notre recommandation
    for livre, prix in list_of_average_prices.items():
        # On définit notre prix conseillé
        prix_conseille = round((float(prix)-0.05), 1)
        # On concatène notre recommandation
        takeaways += (
            f'\nPour le livre "{livre}", '
            f'nous devrions fixer notre prix à {prix_conseille:.2f}€.'
        )
    takeaways += (
        "\nCeci nous permettrais de rester compétitif, "
        "sans rogner la marge."
    )

    # On retourne le texte à intégrer au rapport
    return takeaways
