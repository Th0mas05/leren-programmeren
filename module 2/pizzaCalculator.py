# Thomas Kooij, Pizzacalculator


small  = 6.99      # Prijs in euro
medium = 11.95     # Prijs in euro
large  = 17.45     # Prijs in euro

print("|--------------------------|")
print("|   small  pizza   €6.99   |")
print("|   medium pizza   €11.95  |")
print("|   large  pizza   €17.45  |")
print("|--------------------------|")

#keuze grootte pizza
size = input("Kies de grootte van uw pizza: ")
if  size.lower()  == ("small"): 
    kaas = 1
    print("U heeft een small pizza gekozen")
elif size.lower() == ("medium"): 
    kaas = 2
    print("U heeft een medium pizza gekozen")
elif size.lower() == ("large"): 
    kaas = 3
    print("U heeft een large pizza gekozen")

#keuze hoeveelheid pizza's
amount = input("Hoeveel pizza's wilt u? ")
amount = int(amount)

if kaas == 1:
    totaalprijs = small * amount
elif  kaas == 2:
    totaalprijs = medium * amount  
elif  kaas == 3:
    totaalprijs = large * amount 

print("|--------------------------               ")
print("|  " +str(amount)+ "x "+str(size)+" pizza ")
print("|                                         ")
print("|--------------------------               ")
print("| €",totaalprijs,"                        ")