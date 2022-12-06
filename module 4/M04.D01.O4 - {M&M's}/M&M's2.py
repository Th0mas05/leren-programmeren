import random

kleur = ["Rood", "Blauw", "Groen", "Geel", "Bruin"]
zak = {}
keuze = int(input("Hoeveel M&M's wilt U toevoegen? \n\n>> "))


for i in range(keuze):
    a = random.randint(0, 5)
    if kleur[a] not in zak:
        zak.update({kleur[a]: 1})
    else:
        x = zak.get(kleur[a]) + 1
        zak.update({kleur[a]: x})

print(zak)