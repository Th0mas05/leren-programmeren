antwoord_ja = ["Ja", "J", "ja", "j"]
antwoord_nee = ["Nee", "N", "nee", "n"]

print("""
WELKOM! LATEN WE HET AVONTUUR BEGINNEN!!!!

Je staat voor je huis en je ziet een man naar je toe rennen en dringend om onderdak vragen.

Bied je hem onderdak?. (Ja / Nee)
""")

ant1 = input(">> ")

if ant1 in antwoord_ja:
    print("\nNa 2 minuten komt de politie naar uw huis en vraagt U of de dief in uw huis is of niet. Zeg je (Ja / Nee)?\n")

    ant2 = input(">>")

    if ant2 in antwoord_ja:
        print("\nJe bent een eerlijk persoon. Hij was een dief en jij hebt gewonnen!")

    elif ant2 in antwoord_nee:
        print("\nJe hebt een dief geholpen en je gaat nu naar de gevangenis. GAMEOVER!")

    else:
        print("\nGeen valide antwoord!")

elif ant1 in antwoord_nee:
    print("\nNu probeert hij je te vermoorden. Wil je hem neerslaan? (Ja / Nee)\n")

    ant3 = input(">> ")

    if ant3 in antwoord_ja:
        print("\nGefeliciteerd! Hij was een dief en jij hielp de politie om hem te pakken met je moed.")

    elif ant3 in antwoord_nee:
        print("\nSorry! Je bent dood. Hij was een dief en hij heeft jou vermoord. GAME OVER")

    else:
        print("\nGeen valide antwoord!")

else:
    print("\nGeen valide antwoord!")