import os
os.system("cls")


lista = ["ägg", "mjölk", "mjöl", "smör", "juice", "mjukost"]


print("""
      välkommen till min lista
      skriv för att lägga till
      skriv existerande sak för att ta bort 
      skriv "exit" för att gå ut ur program
      """)

while True:
    print("din lista just nu: ")
    for i in lista:
        print(i)
    
    check1 = input(": ")
    
    if check1.lower() == 'exit':
        print("stänger ner...")
        exit()

    if check1 in lista:
        print(check1, "existerar... tar bort...")
        lista.remove(check1)
    else:
        print(check1, "existerar inte... lägger till...")
        lista.append(check1)