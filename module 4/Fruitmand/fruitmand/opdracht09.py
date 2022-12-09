from fruitmand import fruitmand

kleuren = []

for i in fruitmand:
    if i['name'] == 'druif':
        fruitmand.remove(i)

for i in fruitmand:
    if i['color'] not in kleuren:
        kleuren.append(i['color'])

print(kleuren)