
personen = input("Met hoeveel personen bent u? ")
personen = int(personen)
ticket = 7.45
prijs = personen*ticket

gameseat = 0.074
tijd = input("Hoe veel minuten wilt u in de SUPER VR GAME SEAT? ")
tijd = int(tijd)
prijsgame = gameseat*tijd*personen

totaal = prijs+prijsgame

print("Dit geweldige dagje-uit met",personen, "personen in de Speelhal met" ,tijd, "minuten VR kost je maar",totaal, "euro")

