# UTILISER LES MODULES ( BIBLIOTHEQUES PYTHON)

# PROGRAMME 1 : Renvoie de la factorielle d'un nombre

#from math import factorial

#print(factorial(6))


#PROGRAMME 2 : Fonction qui calcule le périmètre d'un cercle

#from math import pi

#rayon=int(input("quel est le rayon  ? \n" ))

#per=2*pi*rayon
#surf=pi*(rayon**2)

#print("le périmètre du cercle est : " , per)
#print("la surface du cercle est : ", surf)


#PROGRAMME 3 : LES DATETIME

#from datetime import datetime
#print(datetime.today())

#PROGRAMME 4 : AJOUTER NOMBRE DE JOURS A LA DATE ACTUELLE, exemple +7 jours

#from datetime import timedelta, date

#date_ulterieure=date.today()+ timedelta(days=30)

#print(date_ulterieure)



#PROGRAMME 5 : RENVOIE HEURE ACTUELLE 

#importing datetime module for now()  
#from datetime import datetime, timedelta  
  
# using now() to get present_time  
#present_time = datetime.now()  
  
#time formatting
#'{:%H:%M:%S}'.format(present_time)    
   
#print("Present time at greenwich meridian is " ,end = "") 

#print(present_time)


#PROGRAMME 6: DATE ACTUELLE ET HEURE ACTUELLE + HEURE ( Exemple +3 heures)

#importing datetime module for now()  
#from datetime import datetime, timedelta  
  
# using now() to get present_time  
#present_time = datetime.now()  
  
#time formatting
#'{:%H:%M:%S}'.format( present_time )    
   
#print("Present time at greenwich meridian is " ,end = "")  
#print( present_time )
  
#updated_time = datetime.now() + timedelta(hours=3)
#print( updated_time )


# PROGRAMME 6 ( BIS ) : DATE ACTUELLE ET HEURE ACTUELLE + HEURE (Exemple +3  heures)

#from datetime import datetime, timedelta
  
#updated = ( datetime.now() +
#           timedelta( hours=3 )).strftime('%H:%M:%S')
  
#print( updated )


# LES LISTES

#livres = ["Les trois mousquetaires" , "Roméo & Juliette", " l'avare"] # créer une liste livres avec les objets "Les 3 moustiquaires","Roméo et Juliete" et "l'avare"

#print(livres) # Affiche le contenu de la liste livres

#print(livres[1]) # Affiche le 2è objet de la liste livres

#couleurs = ["jaune", "vert", "bleu", "rouge"]

#couleurs.append(couleurs)

#print(couleurs[3])

#print(couleurs)



livres = ["Les trois mousquetaires" , "Roméo & Juliette", " L'avare"] # créer une liste livres avec les objets "Les 3 moustiquaires","Roméo et Juliete" et "l'avare"


      #Ajoutez un élement du même nom dans la liste
livres.append("Les trois mousquetaires")
livres.append("Les trois mousquetaires")
livres.append("Les trois mousquetaires")
livres.append("Les trois mousquetaires")

livres.append("L'avare")
livres.append("L'avare")
livres.append("L'avare")

livres.count("Les trois mousquetaires")
livres.count("Roméo & Juliette")
livres.count("L'avare")

print(livres.count("Les trois mousquetaires"))
print(livres.count("Roméo & Juliette"))
print(livres.count("L'avare"))
print(livres) # Affiche le contenu de la liste livres
print(livres[1]) # Affiche le premier objet de la liste livres
















