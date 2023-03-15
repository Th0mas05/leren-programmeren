print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")

while True:
    aantal_bolletjes = input("Hoeveel bolletjes wilt u? ")

    if aantal_bolletjes.isdigit():
        aantal_bolletjes = int(aantal_bolletjes)

        if aantal_bolletjes <= 3:
            break
        elif 4 <= aantal_bolletjes <= 8:
            print(f"Dan krijgt u van mij een bakje met {aantal_bolletjes} bolletjes.")
            break
        else:
            print("Sorry, zulke grote bakken hebben we niet.")
    else:
        print("Sorry, dat snap ik niet...")

while True:
    bakje_of_hoorntje = input(f"Wilt u deze {aantal_bolletjes} bolletje(s) in een hoorntje of een bakje? ")

    if bakje_of_hoorntje.lower() == "hoorntje" or bakje_of_hoorntje.lower() == "bakje":
        print(f"Hier is uw {bakje_of_hoorntje.lower()} met {aantal_bolletjes} bolletje(s).")
        nog_meer_bestellen = input("Wilt u nog meer bestellen? (ja/nee) ")

        if nog_meer_bestellen.lower() == "ja":
            continue
        elif nog_meer_bestellen.lower() == "nee":
            print("Bedankt en tot ziens!")
            break
        else:
            print("Sorry, dat snap ik niet...")
    else:
        print("Sorry, dat snap ik niet...")
