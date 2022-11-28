import random

kleur = ["Rood", "Blauw", "Groen", "Geel", "Bruin"]
zak = {}

keuze = int(input("Hoeveel M&M's wilt U?\n\n >> "))

for i in range(keuze):
    a = random.randint(0, 5)
    if kleur[a] not in zak:             # Als de kleur er niet in zit gaat hij automatisch op 1
        zak.update({kleur[a]: 1})
    else:
        x = zak.get(kleur[a]) + 1       # Hij pakt een kleur en kiest er random 1 uit en vervolgens doet hij +1 
        zak.update({kleur[a]: x})       # vervolgens update hij hem zodat het verschijnt in die print

print(zak)