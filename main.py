from bs4 import BeautifulSoup
import csv

'''
Sujet
Extraire automatiquement les titres et prix des livres depuis les fichiers HTML

Structurer les données dans un fichier CSV

Analyser les prix :

Déterminer les livres les moins chers

Afficher les prix moyens par livre

Détecter un concurrent systématiquement plus cher ou moins cher

Générer un rapport écrit (.txt ou terminal) avec des recommandations marketing

'''

# Première partie : extraire automatiquement les titres et prix des livres
# Fichier booky.html :
#   titre : div class="produit" h2 class="titre"
#   prix : p class_="prix"

# Fichier pagezen.html :
#   titre : li class="livre" div class="titre-livre"
#   prix: p class="prix"

# Fichier lireplus.html :
#   titre : article class="livre" header
#   prix : div class_="meta" span class="prix"


def web_site_list():

    web_site_list = []
    booky = dict()
    lireplus = dict()
    pagezen = dict()

    booky = {
        "nom": "booky",
        "adresse": "data/booky.html",
        "balise_produit": "div",
        "classe_produit": "produit",
        "balise_titre": "h2",
        "classe_titre": "titre",
        "balise_prix": "p",
        "classe_prix": "prix"
    }
    lireplus = {
        "nom": "lireplus",
        "adresse": "data/lireplus.html",
        "balise_produit": "article",
        "classe_produit": "livre",
        "balise_titre": "h3",
        "classe_titre": "",
        "balise_prix": "span",
        "classe_prix": "prix"
    }
    pagezen = {
        "nom": "pagezen",
        "adresse": "data/pagezen.html",
        "balise_produit": "li",
        "classe_produit": "livre",
        "balise_titre": "div",
        "classe_titre": "titre-livre",
        "balise_prix": "p",
        "classe_prix": "prix"
    }

    web_site_list = [booky, lireplus, pagezen]
    return web_site_list


def parse_data(adresse_web_site):

    with open(adresse_web_site, mode="r", encoding="utf-8") as file:
        page_soup = BeautifulSoup(file, "html.parser")
    return page_soup


def Extract(web_site_list):

    concurrents = dict()

    for site in web_site_list:
        page_soup = parse_data(site["adresse"])
        liste_des_produits = Extract_product_list(site, page_soup)
        informations_produits = Extract_data(liste_des_produits, site)
        concurrents[site["nom"]] = {}
        concurrents[site["nom"]] = informations_produits
    return concurrents


def Extract_product_list(web_site_dictionnaire, page_soup):

    liste_produits = (
        page_soup.find_all(
            web_site_dictionnaire["balise_produit"],
            class_=web_site_dictionnaire["classe_produit"]
        )
    )
    return liste_produits


def Extract_data(liste_des_produits, web_site_dictionnaire):

    informations_produits = dict()

    for produit in liste_des_produits:
        titre = extract_title(produit, web_site_dictionnaire)
        prix = extract_price(produit, web_site_dictionnaire)
        informations_produits[titre] = {}
        informations_produits[titre]["prix :"] = prix

    return informations_produits


def extract_title(produit, web_site_dictionnaire):

    if not web_site_dictionnaire["classe_titre"] == "":
        titre = (
            produit.find(
                web_site_dictionnaire["balise_titre"],
                class_=web_site_dictionnaire["classe_titre"]
            ).get_text()
        )
    else:
        titre = produit.find(web_site_dictionnaire["balise_titre"]).get_text()

    return titre


def extract_price(produit, web_site_dictionnaire):

    prix = (
        produit.find(
            web_site_dictionnaire["balise_prix"],
            class_=web_site_dictionnaire["classe_prix"]
        ).get_text()
    )

    return prix


'''2nde partie du projet :
   Structurer les données dans un fichier CSV

Dans un premier temps:
    On va créer un fichier avec le nom du site

Dans un second temps:
    On va créer les en-tetes du fichier csv : titre, prix

Enfin:
    On va écrire grâce à une boucle dans le fichier csv
'''


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


def write_csv_file(liste_concurrents):
    en_tete = ["Titre", "Prix"]

    # Pour chaque site, on va créer un fichier .csv
    for site_concurrent, livres in liste_concurrents.items():
        with open(
            f"{site_concurrent}.csv",
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


# Ici le code du programme :
liste_concurrents = []  # Déclaration variable
liste_web = web_site_list()  # On spécifie les variables pour chaque site
liste_concurrents = Extract(liste_web)  # On scrap nos données
write_csv_file(liste_concurrents)  # On écrits nos fichiers csv
