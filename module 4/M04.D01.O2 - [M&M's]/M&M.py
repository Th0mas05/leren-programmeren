import random

kleur = ("oranje", "blauw","groen", "bruin")
hoeveelheid = []

zak = int(input("hoeveel M&m's wil je?\n\n>> "))
for i in range(zak):
    hoeveelheid.append(random.choice(kleur))


print(hoeveelheid)