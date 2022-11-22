import random
i = random.randint(1,1000)

Pogingen = 9
punten = 1

a = i + 50
b = i + 20
c = i - 50
d = i - 20
e = i + 51
f = i - 51



while Pogingen == 0 or punten < 20:
    print("gok een nummer tussen 1 en 1000 , als u wilt stoppen typ stop")
    gok = int(input("gok een nummer: "))
    if gok == i :
        punten += 1
        print("geraden! U heeft nu " , punten , "punt!")
        print("Nog een getal raden?")
        i = random.randint(1,1000)
        if punten == 20:
            break
    elif gok == "stop":
        break
    elif gok > e :
        print("Uw gok is hoger! U mag",  Pogingen , "raden")
        Pogingen -= 1
        if Pogingen == 0:
            break
    elif gok < f :
        print("Uw gok is lager! U mag",  Pogingen , "raden")
        Pogingen -= 1
        if Pogingen == 0:
            break
    elif gok < a and gok > b :
        print("U bent warm! U mag",  Pogingen , "raden")
        Pogingen -= 1
        if Pogingen == 0:
            break
    elif gok < b and gok > i :
        print("U bent heel warm! U mag", Pogingen , "raden")
        Pogingen -= 1
        if Pogingen == 0:
            break
    elif gok  > c and gok < d :
        print("U bent warm! U mag",  Pogingen , "raden")
        Pogingen -= 1
        if Pogingen == 0:
            break
    elif gok > d and gok < i :
        print("U bent heel warm!  U mag",  Pogingen , "raden")
        Pogingen -= 1
        if Pogingen == 0:
            break
if punten == 20:
    print("Goed gedaan! u bent klaar , uw eindscore is" , punten)
elif gok == 00:
    print("U bent gestopt met de game")
else:
    print("Helaas , U heeft verloren")