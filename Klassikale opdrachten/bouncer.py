leeftijd = input("Wat is uw leeftijd? ")
leeftijd = int(leeftijd)

if leeftijd > 17:
    naam = input("Wat is uw naam? ")
    if naam.lower() in ["rudi",  "kjeld",  "Arnold",  "Jeroen"]:
        print("U krijgt een sticker en mag doorlopen.")
    elif leeftijd > 20:
        print("U krijgt een bandje om alcohol te bestellen.")
    else:
        print("Alleen u krijgt geen bandje voor alcohol, vanwege dat U daar minimaal 21 jaar moet wezen. ")
else:
    print("U bent te jong en je moet buiten blijven!")


print("_________________")
print("| Cola = €1,00   |")
print("| Bier = €1,50   |")
print("|________________|")

drinken = input("Wat wilt u drinken? A) bier of B) cola: ")
if drinken.lower == "A":
    bandje = input("Kunt U uw bandje laten zien? ")
    if bandje.lower() == "ja":
        print("Veel plezier met uw biertje")
    elif bandje.lower() == "nee":
        print("U heeft geen bandje dus krijgt U geen alcohol!")
    else:
        print("Geen valide antwoord.")
else:
    print("lasld")
