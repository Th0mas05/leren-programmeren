# Thomas Kooij, Pizzacalculator

small  = 6.99   
medium = 11.95    
large  = 17.45     

print("|--------------------------|")
print("|   small  pizza   €6.99   |")
print("|   medium pizza   €11.95  |")
print("|   large  pizza   €17.45  |")
print("|--------------------------|")


repeat = True
while repeat == True:

    size = input("Welke grootte pizza wilt u? ")
    if size.lower() == "small":
        kaas = 1
        repeat = False
    if size.lower() == "medium":
        kaas = 2
        repeat = False
    if size.lower() == "large":
        kaas = 3
        repeat = False

succes = False
while succes == False:
    try:
        amount = input("Hoeveel pizza's wilt u? ")
        amount = int(amount)
        succes = True
    except:  
        print("Dit is geen getal")

    if succes == True:
        if kaas == 1:
            totaalprijs = small * amount
        elif  kaas == 2:
            totaalprijs = medium * amount  
        elif  kaas == 3:
            totaalprijs = large * amount 

        print("|--------------------------               ")
        print("|  " +str(amount)+ "x "+str(size)+" pizza ")
        print("|                                         ")
        print("|--------------------------               ")
        print("| €",totaalprijs,"                        ")

