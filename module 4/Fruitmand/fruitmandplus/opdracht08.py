from fruitmandplus import fruitmand

fruitmand.append({'name': 'watermeloen', 'weight': 2000, 'color': 'green', 'round': True})

totaal = fruitmand[0]['weight'] + fruitmand[1]['weight'] + fruitmand[2]['weight'] + fruitmand[3]['weight'] + fruitmand[4]['weight'] + fruitmand[5]['weight'] + fruitmand[6]['weight'] + fruitmand[7]['weight']
print(totaal/1000,"Kg")