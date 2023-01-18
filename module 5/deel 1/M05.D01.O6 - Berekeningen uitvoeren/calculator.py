def optellen(nummer1: float, nummer2: float):
    print(f"{nummer1} + {nummer2} = {float(nummer1) + float(nummer2)}")
    return nummer1 + nummer2


def aftrekken(nummer1: float, nummer2: float):
    print(f"{nummer1} - {nummer2} = {float(nummer1) - float(nummer2)}")
    return nummer1 -nummer2



def vermenigvuldigen(nummer1: float, nummer2: float):
    print(f"{nummer1} * {nummer2} = {float(nummer1) * float(nummer2)}")
    return nummer1 * nummer2


def delen(nummer1: float, nummer2: float):
    print(f"{nummer1} / {nummer2} = {float(nummer1) / float(nummer2)}")
    return nummer1 / nummer2

gebruiker_nummer = 0
nog_een_ronde = True

while nog_een_ronde:
    keuze = input("""wat te doen?
    #     A) getallen optellen
    #     B) getallen aftrekken
    #     C) getallen vermenigvuldigen
    #     D) getallen delen
    #     E) getal ophogen
    #     F) getal verlagen
    #     G) getal verdubbelen
    #     H) getal halveren
    #     Kies: """).upper()

    if gebruiker_nummer:
        n1 = float(input("Welk getal: "))
        n2 = gebruiker_nummer
    elif keuze == "A" or keuze == "B" or keuze == "C" or keuze == "D":
        n1 = float(input("Getal 1: "))
        n2 = float(input("Getal 2: "))
    else:
        n1 = float(input("Welk getal: "))

    if keuze == "A":
        gebruiker_nummer += float(optellen(n1, n2))
    elif keuze == "B":
        gebruiker_nummer += aftrekken(n1, n2)
    elif keuze == "C":
        gebruiker_nummer += vermenigvuldigen(n1, n2)
    elif keuze == "D":
        gebruiker_nummer += delen(n1, n2)
    elif keuze == "E":
        gebruiker_nummer += optellen(n1, 1)
    elif keuze == "F":
        gebruiker_nummer += aftrekken(n1, 1)
    elif keuze == "G":
        gebruiker_nummer += vermenigvuldigen(n1, 2)
    elif keuze == "H":
        gebruiker_nummer += delen(n1, 2)

    nog_een_ronde = input(f"Wil je iets met {gebruiker_nummer}? (Y/N): ").upper()
    if nog_een_ronde == "N":
        nog_een_ronde = False
    elif nog_een_ronde == "Y":
        nog_een_ronde = True
    else:
        print("Foutief antwoord")