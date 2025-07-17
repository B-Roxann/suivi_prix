from bs4 import BeautifulSoup


# Informations sur les sites à parcourrir
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


# Parse des données HTML du site
def parse_data(adresse_web_site):

    with open(adresse_web_site, mode="r", encoding="utf-8") as file:
        page_soup = BeautifulSoup(file, "html.parser")
    return page_soup


# Extraction des données par site : liste produits et leurs informations
def Extract(web_site_list):

    concurrents = dict()

    for site in web_site_list:
        page_soup = parse_data(site["adresse"])
        liste_des_produits = Extract_product_list(site, page_soup)
        informations_produits = Extract_data(liste_des_produits, site)
        concurrents[site["nom"]] = {}
        concurrents[site["nom"]] = informations_produits
    return concurrents


# Exctraction de la liste des produits via leur balise et classe
def Extract_product_list(web_site_dictionnaire, page_soup):

    liste_produits = (
        page_soup.find_all(
            web_site_dictionnaire["balise_produit"],
            class_=web_site_dictionnaire["classe_produit"]
        )
    )
    return liste_produits


# Extraction des données produits et construction de la liste d'information
def Extract_data(liste_des_produits, web_site_dictionnaire):

    informations_produits = dict()

    for produit in liste_des_produits:
        titre = extract_title(produit, web_site_dictionnaire)
        prix = extract_price(produit, web_site_dictionnaire)
        informations_produits[titre] = {}
        informations_produits[titre]["prix :"] = prix

    return informations_produits


# Extraction du titre du produit
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


# Extraction du prix du produit
def extract_price(produit, web_site_dictionnaire):

    prix = (
        produit.find(
            web_site_dictionnaire["balise_prix"],
            class_=web_site_dictionnaire["classe_prix"]
        ).get_text()
    )

    return prix
