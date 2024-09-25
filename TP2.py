import csv
"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : XX
Numéro d'équipe :  YY
Noms et matricules : Nom1 (Yann Toukam), Nom2 (Matricule2)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici

with open("collection_bibliotheque.csv", newline="") as collection_bilbio :
    reader = csv.reader(collection_bilbio, delimiter=",", quotechar='|')
    bibliotheque = {}
    array_cote = []
    nb_book = 1
    next(reader)
    for row in reader :
        bibliotheque[f"livre{nb_book}"] = {
            "titre": row[0],
            "auteur": row[1],
            "date_publication": row[2],
            "cote_rangement": row[3]
        }
        array_cote.append(row[3])
        nb_book += 1


    print(f'\n Bibliotheque initiale : {bibliotheque} \n')

########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici
with open("nouvelle_collection.csv", newline="") as nouvelle_collection :
    reader = csv.reader(nouvelle_collection, delimiter=",", quotechar='|')
    next(reader)
    for row in reader :
        if row[3] not in array_cote:
            bibliotheque[f"livre{nb_book}"] = {
            "titre": row[0],
            "auteur": row[1],
            "date_publication": row[2],
            "cote_rangement": row[3]
            }
            print(f" Le livre {bibliotheque[f"livre{nb_book}"]["cote_rangement"]} ---- {bibliotheque[f"livre{nb_book}"]["titre"]} par {bibliotheque[f"livre{nb_book}"]["auteur"]} ---- a été ajouté avec succès")
            nb_book += 1


########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici
    for key, info in bibliotheque.items():
         if info["cote_rangement"][0] == "S":
            info["cote_rangement"] = "WS" + info["cote_rangement"][1:]

    print(f'\n Bibliotheque avec modifications de cote : {bibliotheque} \n')




########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici






