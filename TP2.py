import csv
from datetime import date
import json

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
    reader = csv.reader(collection_bilbio)
    bibliotheque = {}
    next(reader)
    for row in reader :
        bibliotheque[row[3]] = {
            "titre": row[0],
            "auteur": row[1],
            "date_publication": row[2]
        }

    print(f'\n Bibliotheque initiale : \n\n{bibliotheque} \n\n')

########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici
with open("nouvelle_collection.csv", newline="") as nouvelle_collection :
    reader = csv.reader(nouvelle_collection)
    next(reader)
    for row in reader :
        if row[3] not in bibliotheque:
            bibliotheque[row[3]] = {
            "titre": row[0],
            "auteur": row[1],
            "date_publication": row[2]
            }
            print(f" Le livre {row[3]} ---- {bibliotheque[row[3]]["titre"]} par {bibliotheque[row[3]]["auteur"]} ---- a été ajouté avec succès")
        else: 
            print(f" Le livre {row[3]} ---- {bibliotheque[row[3]]["titre"]} par {bibliotheque[row[3]]["auteur"]} ---- est déjà présent dans la bibliothèque")


########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici
    '''
    for key, value in bibliotheque.items():
        if value['auteur'] == 'William Shakespeare':
            new_key = 'WS' + list(bibliotheque)[index][1:]
            bibliotheque[new_key] = bibliotheque.pop(key)
    '''

    for livre in [livre for livre in bibliotheque.items() if livre[1]['auteur'] == 'William Shakespeare']:
        new_key = 'WS' + livre[0][1:]
        bibliotheque[new_key] = bibliotheque.pop(livre[0])


    print(f'\n Bibliotheque avec modifications de cote : \n\n{bibliotheque} \n')


########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici

with open("emprunts.csv", newline="") as emprunts :
    reader = csv.reader(emprunts)
    next(reader)

    for key, value in bibliotheque.items():
        value['emprunts'] = 'disponible'
        
    
    for item in reader:
        bibliotheque[item[0]]['emprunts'] = 'emprunté'
        bibliotheque[item[0]]['date_emprunt'] = item[1]
    
    print(f' \nBibliotheque avec ajout des emprunts : \n\n{bibliotheque} \n')
    
        
    

########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici

delai_retour = 30
delai_perdu = 365
print('\nLivres en retard avec frais: \n')
for key, value in bibliotheque.items():
    if value['emprunts'] == 'emprunté':
        delai = (date.today() - date.fromisoformat(value['date_emprunt'])).days
        
        if (delai > delai_retour):
            montant = (delai - delai_retour) * 2
            value['frais_retard'] = "100 $" if montant >= 100 else str(montant) + " $"
            
        if(delai >= delai_perdu):
            value['livres_perdus'] = True
        
        print(value)
            
print(f'\n\n \nBibliotheque avec ajout des retards et frais :\n\n{bibliotheque} \n')