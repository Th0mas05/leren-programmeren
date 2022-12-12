from fruitmand import fruitmand

naam = []
kleuren = []
gewicht = []

for i in fruitmand:
    naam.append(i['name'])
naam.sort(key=len, reverse=True) #de gesorteerde lijst is in aflopende volgorde
naam.sort(key=len, reverse=True) #de gesorteerde lijst is omgekeerd (of gesorteerd in aflopende volgorde)

for i in fruitmand:
    if i['name'] == naam[0]:
        kleuren.append(i['color'])
        gewicht.append(i['weight'])

meeste_letters = len(naam[0])

print(f"De '{naam[0]}' ({meeste_letters} letters) heeft een {kleuren[0]} kleur en een gewicht van {gewicht[0]}G")