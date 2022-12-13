from random import shuffle

namen_lijst = []
aantal = len(namen_lijst)
deelnemers = False

while aantal < 3:
    print(f"voeg minimaal {3 - aantal} namen toe")
    voegnaamtoe = input("Voeg een naam toe:\n\n>> ").capitalize()
    if voegnaamtoe in namen_lijst:
        print("Naam bestaat al\n")
    else:
        namen_lijst.append(voegnaamtoe)
        aantal = len(namen_lijst)

while not deelnemers:
    print("type quit om te stoppen\n")
    voegnaamtoe = input("Voeg nog een naam toe:\n\n>> ").capitalize()
    if voegnaamtoe.lower() == "quit":
        break
    elif voegnaamtoe in namen_lijst:
        print("Naam bestaat al\n")
    else:
        namen_lijst.append(voegnaamtoe)

shuffle(namen_lijst)

persoon = namen_lijst[-1]
for mensen in namen_lijst:
    print(f"{persoon} heeft {mensen} getrokken\n")
    persoon = mensen