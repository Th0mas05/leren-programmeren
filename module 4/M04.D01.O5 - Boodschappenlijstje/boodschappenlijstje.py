boodschappen = {}
keuze = input("wilt u iets toevoegen? (ja/nee)\n\n>> ").lower()

while not keuze != "ja":
    product = input("Wat wilt u toevoegen\n\n>> ").capitalize()
    hoeveelheid = int(input("hoeveelheid wilt u er van toevoegen\n\n>> "))
    if product in boodschappen:
        boodschappen[product] += hoeveelheid
    else:
        boodschappen[product] = hoeveelheid
    keuze = input("wilt u iets toevoegen?(ja/nee)\n\n>> ").lower()

print('-[ BOODSCHAPPENLIJSTJE ]-\n')
for product in boodschappen:
    hoeveelheid = str(boodschappen[product])
    print(hoeveelheid, "x" ,product)
print('\n-------------------------')