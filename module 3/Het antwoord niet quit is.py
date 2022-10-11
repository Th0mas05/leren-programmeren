score = 0 

quit = False
while quit == False:
    antwoord = input("? ")
    if antwoord.lower() == ("quit"):
        quit = True
        print (score)
        break
    else:
        score += 1
        continue
