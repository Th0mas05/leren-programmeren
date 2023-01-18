def naam_leeftijd():
    lst = []
    dct = {}
    stop = True
    while stop:
        naam = input("Naam:\n\n>> ")
        if naam == "stop":
            for mensen in lst:
                print(mensen["naam"] + " is " + mensen["leeftijd"] + " jaar")
            return
        else:
            dct.update({"naam": naam})
        leeftijd = input("Leeftijd:\n\n>> ")
        if leeftijd == "stop":
            for mensen in lst:
                print(mensen["naam"] + " is " + mensen["leeftijd"] + " jaar")
            return
        else:
            dct.update({"leeftijd": leeftijd})
        lst.append(dct)
        dct = {}


naam_leeftijd()