##m mon enseignement dpoit encoder 6 notes de cours pour un élève

nombre_d_interrogation = 6
total_note=0

for i in range(nombre_d_interrogation):

    note =input("Quelle note voulez-vous encoder ?")
    print("vous avez encoder" + note)
    total_note=total_note+int(note)

moyenne_note=total_note/nombre_d_interrogation

print(moyenne_note)