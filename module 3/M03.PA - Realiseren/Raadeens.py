import random
score = 0

for raden in range(0, 20):
    
    getal = random.randint(1,1000)
    
    for vraag in range(0, 10):
        invoer = int(input("Gok een getal tussen de 1 en de 1000\n\n>> "))
        
        if invoer > getal:
            print("Lager!")
        elif invoer < getal:
            print("Hoger!")
        if invoer == getal:
            print("Geraden!")
            score = score + 1
            break
        elif invoer > getal - 20 and invoer < getal + 20:
            print("Je poten staan in de fik zo dichtbij ben je!")
        elif invoer > getal - 50 and invoer < getal + 50:
            print("De thermostaat slaat op hol, want je bent warm!")
        
        print(getal)

    print()      
    print("Het getal was", getal)
    print("Je hebt momenteel", score, "punt(en) gescoord!")
    print()
    invoer2 = input("Wil je nog een getal raden? Ja of Nee!\n\n>> ").lower()
    if invoer2 == "nee" and raden < 19:
        print("Eindscore:", score, "punt(en)")
        break
    else:
        print(score)