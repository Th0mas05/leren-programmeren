from fruitmandplus import fruitmand
import random

fruit = int(input("Geef een getal\n\n >> "))
random_fruit = random.randint(0,6)

for i in range(0,fruit):
    print(fruitmand[random_fruit]['name'])