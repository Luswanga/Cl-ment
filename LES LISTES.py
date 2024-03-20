# LES LISTES

# EXO 1 :

#livres = ["Les trois mousquetaires" , "Roméo & Juliette", " l'avare"] # créer une liste livres avec les objets "Les 3 moustiquaires","Roméo et Juliete" et "l'avare"

#print(livres) # Affiche le contenu de la liste livres

#print(livres[1]) # Affiche le 2è objet de la liste livres

#couleurs = ["jaune", "vert", "bleu", "rouge"]

#couleurs.append(couleurs)

#print(couleurs[3])

#print(couleurs)



#livres = ["Les trois mousquetaires" , "Roméo & Juliette", " L'avare"] # créer une liste livres avec les objets "Les 3 moustiquaires","Roméo et Juliete" et "l'avare"
#
#
#      #Ajoutez un élement du même nom dans la liste
#livres.append("Les trois mousquetaires")
#livres.append("Les trois mousquetaires")
#livres.append("Les trois mousquetaires")
#livres.append("Les trois mousquetaires")
#
#livres.append("L'avare")
#livres.append("L'avare")
#livres.append("L'avare")
#
#"livres.count("Les trois mousquetaires")
#livres.count("Roméo & Juliette")
#livres.count("L'avare")
#
#print(livres.count("Les trois mousquetaires"))
#print(livres.count("Roméo & Juliette"))
#print(livres.count("L'avare"))
#print(livres) # Affiche le contenu de la liste livres
#print(livres[1]) # Affiche le premier objet de la liste livres

# EXO 2 : 

#boite_outils = ["Tournevis", "Marteau", "Clé à molette"]

#nouvel_outil = "scie"
#boite_outils.append(nouvel_outil) # Ajout Scie à la boite_outils

#outil_a_retirer = "Marteau"

#if boite_outils.count(outil_a_retirer):
#    boite_outils.remove(outil_a_retirer)

#if outil_a_retirer in boite_outils:
#    boite_outils.remove(outil_a_retirer)

#else:
#    print("L'outil que vous essayez de retirer n'est pas dans la boite à outils. ")
 
#print("Les outils présents dans la boite à outils sont : ")
#for outil in boite_outils:
#    print(outil)

#if len(boite_outils) >=3:
#    print("L'outil à la 3è position est :", boite_outils[2])
#else:
#    print("Il n'y a pas assez d'outils dans la boite pour afficher celui de la 3è position ")


# EXO 3 : LISTE DE COURSES

#liste_de_course = []
#article = []

#"def ajouter_article(article):
#    article =input(" cohoisir l'article :")
    
#liste_de_course.append(article):

#remove(article)





#print(boite_outils) # liste des outils dans la boite_outils
#print(boite_outils) # liste actuelle de la boite_outils
#outil_a_retirer = " Marteau"
#"if outil_a_retirer
#print(boite_outils) 

# EXO TUPLE
#tuple = (('Clément', 'Lili', 'Coco'))
#print(tuple)


# EXO LES DICTIONNAIRES

#voiture = {
#    'marque' : 'BMW', 
#    'color' : 'bleu',
#    'annee' : '1960'
#}

#print(voiture)

#print(voiture['marque'])


# EXO DICTIONNAIRE DE DICTIONNAIRE


employees = {
    'boss' : {'name': 'Anna','salary': 3000,'option':{'telephone':'oui','voiture de société':'non'}},
    'accountant' : {'name': 'Martin', 'salary': 2300},
    'intern' : {'name': 'Fred', 'salary': 0},
}

print(employees['boss'])   # affiche les infos de boss
print(employees['boss']['salary']) # affiche le salaire de boss
print(employees['boss']['option']['telephone'])








