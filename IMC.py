poids = float(input("Quel est votre poids : "))
taille = float(input("Quelle est votre taille : "))

imc = poids / (taille ** 2)

print("votre IMC est = " + str(imc))

poids_insuffisant = imc < 18.5
poids_normal = 18.5 <= imc >= 24.9
surpoids = 25 <= imc >= 29.9
obesite = imc >= 30

if poids_insuffisant: 
    print("poifs insuffisant et risques pour la santé ")

if poids_normal:
    print("poids normal et pas de risques pour la santé")

if surpoids:
    print("pas de risques pour la santé")

if obesite:
    print("Obésité, risque accru de développer certaines maladies")
