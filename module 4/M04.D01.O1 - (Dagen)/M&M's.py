import random

kleur = ("oranje", "blauw","groen", "bruin")
hoeveelheid = []

zak = int(input("hoeveel M&m's wil je?\n\n>> "))
hoeveelheid.append(zak)
mNms = random.choices(kleur, k=hoeveelheid)

print(hoeveelheid + mNms)
