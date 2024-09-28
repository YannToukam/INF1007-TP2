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
        bibliotheque[row[3]] = {
            "titre": row[0],
            "auteur": row[1],
            "date_publication": row[2]
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
            bibliotheque[row[3]] = {
            "titre": row[0],
            "auteur": row[1],
            "date_publication": row[2]
            }
            print(f" Le livre {row[3]} ---- {bibliotheque[row[3]]["titre"]} par {bibliotheque[row[3]]["auteur"]} ---- a été ajouté avec succès")
            nb_book += 1
        else: 
            print(f" Le livre {row[3]} ---- {bibliotheque[row[3]]["titre"]} par {bibliotheque[row[3]]["auteur"]} ---- est déjà présent dans la bibliothèque")


########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici
    for index in range(len(bibliotheque)):
        if str.lower(list(bibliotheque)[index][0]) == 's':
            new_key = 'WS' + list(bibliotheque)[index][1:]
            bibliotheque[new_key] = bibliotheque.pop(list(bibliotheque)[index])

    print(f'\n Bibliotheque avec modifications de cote : {bibliotheque} \n')




########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici


with open("emprunts.csv", newline="") as emprunts :
    reader = csv.reader(emprunts, delimiter=",", quotechar='|')
    next(reader)
    

########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici






