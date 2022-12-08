from fruitmand import fruitmand

gewicht = sorted(fruitmand, key=lambda i: i['weight'])
for i in gewicht:
   print(f'{i["name"]}: {i["weight"]}')