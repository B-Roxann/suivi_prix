from bs4 import BeautifulSoup


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
# Fichier booky.html : titre : div class="produit" h2 class="titre" prix : p class="prix"
# Fichier pagezen.html : titre : li class="livre" div class="titre-livre"  prix : p class="prix"
# Fichier lireplus.html : titre : article class="livre" header  prix : div class="meta" span class="prix"

list_of_website = ["data/booky.html", "data/pagezen.html", "data/lireplus.html"]

dictionnary_of_product = dict()

for web_site in list_of_website:
    with open(web_site, mode="r", encoding="utf-8") as file:
        page_soup = BeautifulSoup(file, "html.parser")

        # On rajoute à notre dictionnaire les titres des sites scrapés
        site = page_soup.title.string
        dictionnary_of_product[site] = {}

        # On parcourt chaque produit et y récupère les informations nécessaire
        product_list = page_soup.find_all("div", class_="produit")
        list_of_product = dict()

        for product in product_list:
            # On ajoute le nom du livre
            name = product.find("h2").string
            list_of_product[name] = {}

            # A ce livre on ajoute son prix
            price = product.find("p", class_="prix").get_text()
            list_of_product[name]["prix :"] = price

            # Et sa description
            description = product.find("p", class_="description").get_text()
            list_of_product[name]["description :"] = description

        # On ajoute notre liste de produits pour le site parcouru
        dictionnary_of_product[site] = list_of_product
        print(dictionnary_of_product)
