from random import shuffle

namen = []
aantal = len(namen)
deelnemers = False

while aantal < 3:
    print(f"voeg minimaal {3 - aantal} namen toe")
    voegnaam = input("Voeg een naam toe:\n\n>> ")
    if voegnaam in namen:
        print("Naam bestaat al\n")
    else:
        namen.append(voegnaam)
        aantal = len(namen)

while not deelnemers:
    print("type quit om te stoppen\n")
    voegnaam = input("Voeg nog een naam toe:\n\n>> ")
    if voegnaam.lower() == "quit":
        break
    elif voegnaam in namen:
        print("Naam bestaat al\n")
    else:
        namen.append(voegnaam)

shuffle(namen)

persoon = namen[-1]
for mensen in namen:
    print(f"{persoon} heeft {mensen} getrokken\n")
    persoon = mensen