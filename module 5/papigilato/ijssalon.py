def welcome_message():
    print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")

def ask_bolletjes():
    bolletjes = input("Hoeveel bolletjes wilt u?\n>> ")
    if bolletjes.isdigit():
        bolletjes = int(bolletjes)
        if bolletjes >= 1 and bolletjes <= 3:
            return bolletjes
        elif bolletjes >= 4 and bolletjes <= 8:
            print(f"Dan krijgt u van mij een bakje met {bolletjes} bolletjes")
            return bolletjes
        elif bolletjes > 8:
            print("Sorry, zulke grote bakken hebben we niet")
            return ask_bolletjes()
    else:
        print("Sorry dat snap ik niet...")
        return ask_bolletjes()

def ask_hoorntje_of_bakje(bolletjes):
    keuze = input(f"Wilt u deze {bolletjes} bolletje(s) in een hoorntje of een bakje?\n>> ")
    if keuze.lower() == "hoorntje" or keuze.lower() == "bakje":
        return keuze
    else:
        print("Sorry, dat snap ik niet...")
        return ask_hoorntje_of_bakje(bolletjes)

def serve_ijs(bolletjes, keuze):
    print(f"Hier is uw {keuze} met {bolletjes} bolletje(s).")
    antwoord = input("Wilt u nog meer bestellen?\n>> ")
    if antwoord.lower() == "ja":
        return True
    elif antwoord.lower() == "nee":
        print("Bedankt en tot ziens!")
        return False
    else:
        print("Sorry, dat snap ik niet...")
        return serve_ijs(bolletjes, keuze)

def bestel_ijs():
    welcome_message()
    while True:
        bolletjes = ask_bolletjes()
        keuze = ask_hoorntje_of_bakje(bolletjes)
        if not serve_ijs(bolletjes, keuze):
            break

bestel_ijs()
