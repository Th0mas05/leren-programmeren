from fruitmandplus import fruitmand


gevonden = False
rondeTrue = 0
rondeFalse = 0

while not gevonden:
    vraagkleur = input("Welke kleur kies je? (ENGELS!)\n\n >> ").lower()
    for i in fruitmand:
        if vraagkleur == i['color']:
            if i['round']:
                rondeTrue += 1
            else:
                rondeFalse += 1
            gevonden = True
    if not gevonden:
        print(f"De kleur {vraagkleur} zit er niet in de fruitmand")

if rondeTrue > rondeFalse:
    print(f'Er zijn {rondeTrue - rondeFalse} meer ronde vruchten dan niet ronde vruchten in de kleur {vraagkleur}')
elif rondeTrue < rondeFalse:
        print(f'Er zijn {abs(rondeTrue - rondeFalse)} minder ronde vruchten dan niet ronde vruchten in de kleur {vraagkleur}')
else:
    print(f'Er zijn {rondeTrue} ronde vruchten en {rondeFalse} niet ronde vruchten in de kleur {vraagkleur}')