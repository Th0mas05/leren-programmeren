deelnemers = []
aantal = len(deelnemers)
genoeg_namen = False

while aantal < 3:
    print "voeg minimaal {3 - aantal} deelnemers toe"
    voegnaam = input "Voeg een naam toe: "
    if voegnaam in deelnemers:
        print "Naam bestaat al
    else:
        deelnemers.append(voegnaam)
        aantal = len(deelnemers)

while not genoeg_namen:
    print "type quit om te stoppen"
    voegnaam = input"Voeg nog een naam toe:\n\n>> "
    if voegnaam == "quit":
        break
    elif voegnaam in deelnemers:
        print "Naam bestaat al"
    else:
        deelnemers.append(voegnaam)

shuffle(deelnemers)

persoon = deelnemers[-1]
for mens in deelnemers:
    print "{persoon} heeft {mens} getrokken"
    persoon = mens