import random

laag = 1
hoog = 1000
round = 0
score = 0

# loop waarmee je alle 20 rondes uitvoert
while round < 20:
    round += 1
    count = 0
    num = random.randint(laag, hoog)
    
    print("Ronde ", round)
    if round < 19:
        print("Nog een getal raden?")

    while count < 10:
	    count += 1

    gok = int(input("Gok een nummer: "))
    
    if num == gok:
            print("Goed gedaan! Je hebt ",count, " gokken gedaan voordat je het goed had. Score: ", score)
    elif num > gok:
            print("Je hebt te klein gegokt!")
    elif num < gok:
            print("Je hebt te hoog gegokt!")

    if count >= 10:
        print("Het nummer was", num)
        print("Veel geluk voor de volgende keer!")