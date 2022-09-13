croissant = 0.39
aantal = input("Hoeveel croissants wilt u? ")
aantal = int(aantal)
totaalcroissant = (croissant*aantal)

stokbrood = 2.78
aantal2 = input("Hoeveel stokbroden wilt u? ")
aantal2 = int(aantal2)
totaalstokbrood = (stokbrood*aantal2)

kortingsbon = -0.50
aantal3 = input("Hoeveel kortingsbonnen heeft u? ")
aantal3 = int(aantal3)
totaalkortingsbon = (kortingsbon*aantal3)

prijs = totaalcroissant+totaalstokbrood

print("De feestlunch kost je bij de bakker" ,prijs, "euro voor de" ,aantal, "croissantjes en de" ,aantal2, "stokbroden als de" ,aantal3, "kortingsbonnen nog geldig zijn!")