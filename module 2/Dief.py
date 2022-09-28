import random

antwoord_ja = ["Ja", "J", "ja", "j"]
antwoord_nee = ["Nee", "N", "nee", "n"]
procent = random.randint(1,100)

print("""
WELKOM! LATEN WE HET AVONTUUR BEGINNEN!!!!

Je staat voor je huis en je ziet een man naar je toe rennen en dringend om onderdak vragen.

Bied je hem onderdak?. (Ja / Nee)
""")

ant1 = input(">> ")

if ant1 in antwoord_ja:
    print("Na 2 minuten komt de politie naar uw huis en vraagt U of een dief in uw huis heeft?. Zeg je (Ja / Nee)?")
    ant2 = input(">> ")

    if ant2 in antwoord_ja:
        print("Je bent een eerlijk persoon. Hij was een dief en jij hebt gewonnen!")

    elif procent < 50:
        ant2 in antwoord_nee
        print("Je hebt een dief geholpen en je gaat nu naar de gevangenis. GAMEOVER!")
    else:
        print("Je hebt een dief geholpen, maar de politie kwam er niet achter! Je hebt een deel van de buit gekregen als beloning.")

elif ant1 in antwoord_nee:
    print("Nu probeert hij je te vermoorden. Wil je hem neerslaan? (Ja / Nee)")
    ant3 = input(">> ")

    if ant3 in antwoord_ja:
        print("Ga je een wapen gebruiken? ")
        wapen = input(">> ")
    
        if wapen in antwoord_ja:
            print("Je kijkt in de besteklade wat kies je? Mes, vork of lepel?")
            soortwapen = input(">> ")
            
            if soortwapen == "mes" or soortwapen == "vork":
                print("Gefeliciteerd! Hij was een dief en jij hielp de politie om hem te overmeesteren!")
            else:
                print("Sorry! Je bent dood. Hij was een dief en hij heeft jou vermoord. GAME OVER")
                
        elif wapen in antwoord_nee:
            print("Sorry! Je bent dood. Hij was een dief en hij heeft jou vermoord. GAME OVER")
    else:
            print("Sorry! Je bent dood. Hij was een dief en hij heeft jou vermoord. GAME OVER")
else:
    print("Geen valide antwoord!")