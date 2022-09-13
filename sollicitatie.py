mogenlijkeKandidaat = False

print("Hoeveel jaar ervaring heeft met dieren dresuur?")
dierenDresuurErvaring = int(input())

print("Hoeveel jaar ervaring heeft u met jongleren?")
jongleerErvaring = int(input())

print("Hoeveel jaar praktijk ervaring heeft u met acrobatiek?")
acrobatiekErvaring = int(input())

input("Hoeveel katten heeft u?\n")
input("Hoeveel honden heeft u?\n")

if(dierenDresuurErvaring > 4 or jongleerErvaring > 5 or acrobatiekErvaring > 3):
    print("Ben u in het bezit van een MBO-4 ondernemen diploma J/N")
    ondernemenDiploma = input()

    if(ondernemenDiploma == "j" or ondernemenDiploma == "J"):
        print("Bent u in het bezig van een geldig vrachtwagen rijbewijs? J/N")
        vrachtwagenRijbewijs = input()

        if(vrachtwagenRijbewijs == "j" or vrachtwagenRijbewijs == "J"):
            print("Bent u in het bezit van een hoge hoed? J/N")
            hogeHoed = input()

            input("Hoeveel jaren één wieler ervaring heeft u?\n")
            input("Hoeveel uur heeft u Bassie en Adriaan gezien?\n")
            if(hogeHoed == "j" or hogeHoed == "J"):
                print("Wat is uw geslacht? M/V")
                geslacht = input()

                if(geslacht == "m" or geslacht == "M"):
                    print("Hoe breed is uw snor in centimeters?")
                    breedteSnor = int(input())
                    if(breedteSnor > 10):
                        print("Wat is uw lengte in centimeters?")
                        lengte = int(input())

                        if(lengte > 150):
                            print("Wat is uw gewicht in kilogram?")
                            gewicht = int(input())
                            if(gewicht > 90):
                                print("Bent u in het bezit van een certificaat 'Overleven met gevaalijk personeel' J/N")
                                certOveleven = input()
                                if(certOveleven == "j" or certOveleven == "J"):
                                    mogenlijkeKandidaat = True

                elif(geslacht == "v" or geslacht == "V"):
                    print("Welke kleur is uw haar")
                    haarkleur = input()

                    if(haarkleur == "Rood" or haarkleur == "rood"):
                        print("Heeft u krullen? J/N")
                        krullen = input()

                        if(krullen == "j" or krullen == "J"):
                            print("Hoelang zijn de krullen in centimeters?")
                            krulLengte = int(input())
                            if(krulLengte > 20):
                                print("Wat is uw lengte in centimeters?")
                                lengte = int(input())
                                if(lengte > 150):
                                    print("Wat is uw gewicht in kilogram?")
                                    gewicht = int(input())
                                    if(gewicht > 90):
                                        print("Bent u in het bezit van een certificaat 'Overleven met gevaalijk personeel' J/N")
                                        certOveleven = input()
                                        if(certOveleven == "j" or certOveleven == "J"):
                                            mogenlijkeKandidaat = True

if(mogenlijkeKandidaat == False):
    print("U komt helaas niet in aanmerking voor onze vacature, tot ziens.")
else:
    print("Gefeliciteerd! U komt in aanmerking voor de vacature.")