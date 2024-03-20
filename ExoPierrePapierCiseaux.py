#prenomjoueur1=input("quel est ton nom ? \n")
#choixj1=input("Quel est ton choix ? \n")

#prenomjoueur2=input("quel est ton nom ? \n")
#choixj2=input("Quel est ton choix ? \n")

#if choixj1 == "pierre" and choixj2 == "ciseaux":
#    print(prenomjoueur1 +"gagne")
#if choixj1 == "feuille" and choixj2 == "pierre":
 #   print(prenomjoueur1 +" gagne")




#etage_actuel=int(input("A quel étage vous trouvez-vous ?"))

#if etage_actuel <= 13:
    #nbr_vers13=13-etage_actuel
#else:
#    nbr_vers13=etage_actuel-13

#total_floor = nbr_vers13 + (13 - (-2))

#print("Nombre d'étages parcourus jusqu'au 13ème étage :", nbr_vers13)
#print("Nombre total d'étages parcourus :", total_floor)



fruit_pomme = "pomme"
prix_pomme = 5
fruit_orange = "orange"
prix_orange = 7
fruit_banane = "banane"
prix_banane = 9

print("voici la liste d'articles et leurs prix :  \n")
print(fruit_pomme + " = " + str(prix_pomme) + " Eur")
print(fruit_orange + " = " + str(prix_orange) + " Eur")
print(fruit_banane + " = " + str(prix_banane) + " Eur")

caisse_pomme = 0

choix_fruit = input("choisir votre fruit \n")

if choix_fruit == fruit_pomme:
    print("Payez : " , prix_pomme)
    caisse_pomme = 0 + prix_pomme
    print("caisse pomme est : ", caisse_pomme )

if choix_fruit == fruit_orange:
    print("Payez : " , prix_orange)
    caisse_orange = 0 + prix_orange
    print("caisse orange : ", caisse_orange)

if choix_fruit == fruit_banane:
    print("Payez : " , prix_banane)
    caisse_banane = 0 + prix_banane
    print("caisse banane : ", caisse_banane)
    
choix_fruit = input("choisir votre fruit \n")

if choix_fruit == fruit_pomme:
    print("Payez : " , prix_pomme)
    caisse_pomme = 0 + prix_pomme
    print("caisse pomme est : ", caisse_pomme )

if choix_fruit == fruit_orange:
    print("Payez : " , prix_orange)
    caisse_orange = 0 + prix_orange
    print("caisse orange : ", caisse_orange)

if choix_fruit == fruit_banane:
    print("Payez : " , prix_banane)
    caisse_banane = 0 + prix_banane
    print("caisse banane : ", caisse_banane)
    
choix_fruit = input("choisir votre fruit \n")

if choix_fruit == fruit_pomme:
    print("Payez : " , prix_pomme)
    caisse_pomme = 0 + prix_pomme
    print("caisse pomme est : ", caisse_pomme )

if choix_fruit == fruit_orange:
    print("Payez : " , prix_orange)
    caisse_orange = 0 + prix_orange
    print("caisse orange : ", caisse_orange)

if choix_fruit == fruit_banane:
    print("Payez : " , prix_banane)
    caisse_banane = 0 + prix_banane
    print("caisse banane : ", caisse_banane)
    

caisse = caisse_pomme + caisse_orange + caisse_banane
print("Total caisse : ", caisse)




















