# Suivi des prix concurrents pour une librairie en ligne

# DESCRIPTION
Ce projet est réalisé dans le cadre d'une auto-formation développeur Python à l'aide des ressources :
OpenClassRooms : Développeur d'application Python
https://openclassrooms.com/fr/paths/879-developpeur-dapplication-python

et de la conception d'un exercie, en lien avec les cours, par ChatGPT.

Il permet d'analyser les prix d'une sélection de livres proposés par plusieurs concurrents à partir de fichier HTML fictifs. (ChatGPT)
Le but étant d'en extraire les données, de les structurer en fichier .csv et d'en tirer des analyses et conclusions marketing automatisées pour notre client fictif.

# FONCTIONNALITES PRINCIPALES
- Scraping de pages HTML de concurrents fictifs
- Extraction des données utiles pour les analyses
- Structuration des données en CSV
- Analyse des prix
- Détection des concurrents les plus et moins chers
- Création d'un rapport marketing automatisé (.txt)

# STRUCTURE DU PROJET
'''
.
├── csv/                          # Fichier CSV
│    └── prix_concurrents.csv        # Données extraites
├── data/                         # Fichiers HTML des concurrents  
├── source/                       # Fichiers Python
│    └── main.py                     # Script principal
│    └── extract_data.py             # Fonctions pour l'extraction de données
│    └── structuring_data.py         # Fonctions pour la génération du CSV
│    └── analysing_data.py           # Fonctions pour l'analyse des données
│    └── analysis_report.py          # Fonctions pour le rapport
├── rapport.txt                      # Rapport final
└── README.md                        # Présentation du projet
'''

# LANCER LE PROJET

## PREREQUIS
- Python 3.13.x
- Modules : bs4, csv, collections


# RESULTAT ATTENDU

Le programme génère un fichier 'rapport.txt' avec les informations suivantes :

- Pour chaque livre :
    - Le prix le plus bas et quel site le propose
    - Le prix le plus élevé et quel site le propose
    - Le prix moyen
- Une analyse générale par site
- Une recommandation marketing claire


# CE QUE CE PROJET DEMONTRE

- Maîtrise du scraping web avec BeautifulSoup
- Structuration et nettoyage des données
- Analyse basique de données en Python
- Production d'un livrable automatisé
- Organisation de projet et documentation


# Notes personnelles

Il va sans dire que ce projet est le premier d'un long parcour,
Je ne manquerai pas d'améliorer mes compétences pour produire des livrables
encore plus performants et mieux documentés.

Pourquoi ne pas faire tout de suite plus performants et mieux documentés ?
Parce que j'ai voulu jouer le jeu d'avoir du temps imparti,
Et que vouloir sauter des étapes ne me rendra pas meilleur.

J'ai réalisé ce programme en passant des heures à me torturer les méninges
pour sortir ces fonctions.
En progressant dans le projet j'ai déjà modifié la majeur partie de ces fonctions que j'ai trouvé en premier lieu correctes, mais qui par la suite
ne m'ont pas permises mon avancée.

Je suis sûr de faire mieux la prochaine fois et j'en palpite d'impatience.

Si vous avez pris le temps de lire jusqu'ici ou même juste d'ouvrir mon projet, je vous en remercie.

Ce n'est pas grand chose peux être pour vous, mais aujourd'hui je suis fier de moi et je tarde de passer à la suite.

Passez une bonne journée.

Roxann.