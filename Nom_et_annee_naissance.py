# Demande le nom et l'âge qu'aura la personne en 2050
# Programme 1
     
#def calculate_age_in_2050(name, year):
#    age=2050-year
#    print(f'{name} aura {age} en 2050 ')

#username = input('Ton nom \n')
#birth_year=int(input('ton année de naissance \n '))

#calculate_age_in_2050(username, birth_year)



# Programme 2

#def calculate_age_in_2050(year):
#    age = 2050-year
#    return age

#username = input('Ton nom \n')
#birth_year = int(input('Ton année de naissance \n')) 
#calculated_age = calculate_age_in_2050(birth_year)
#print(f'{username} aura {calculated_age}')



# Programme 3

def calculate_age_in(birthyear, given_year):
    age = given_year - birth_year
    return age

birth_year = int(input('Ton année de naissance\n'))
today = int(input("Année d'aujourd'hui \n"))
future = int(input("Dans quelle année veux-tu avoir ton âge ? \n"))

age_today = calculate_age_in(birth_year, today)
age_future = calculate_age_in(birth_year, future)

print(f"tu as {age_today} ans aujourd'hui et en {future} tu auras {age_future} ans")




