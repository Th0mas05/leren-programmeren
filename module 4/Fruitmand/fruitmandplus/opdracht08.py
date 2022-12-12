from fruitmandplus import fruitmand

totaal = 0
fruitmand.append({'name': 'watermeloen', 'weight': 2000, 'color': 'green', 'round': True})

for i in fruitmand:
    b = i['weight']
    totaal += b
print(totaal/1000,"Kg")