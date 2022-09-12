
geel = input("Is de kaas geel? ")
if  geel.lower()  == "ja": 
    gaten = input("Zitten er gaten in? ")
    if gaten.lower() == "ja":
        duur = input("Is de kaas belagelijk duur? ")
        if duur.lower() == "ja":
            print("Uw kaas is de Emmenthaler ")
        elif duur.lower() == "nee": 
            print("Uw kaas is de Leerdammer") 
        else:
            print("Geen valide keuze! kiest uit JA of NEE")  
    elif gaten.lower() == "nee":
        hard = input("Is de kaas hard als steen? ")
        if hard.lower() == "ja":
            print("Uw kaas is de Parmigiano Reggiano")
        elif hard.lower() == "nee":
            print("Uw kaas is de Goudse Kaas")
        else:
            print("Geen valide keuze! kiest uit JA of NEE")
    else:
        print("Geen valide keuze! kiest uit JA of NEE")
elif geel.lower() == "nee": 
    schimmel = input("Heeft de kaas blauwe schimmel? ")
    if schimmel.lower() == "ja":
        korst = input("Heeft de kaas een korst? ")
        if korst.lower() == "ja":
            print("Uw kaas is de Blue de Rochbaron ")
        elif korst.lower() == "nee": 
            print("Uw kaas is de d'Ambert")   
        else:
            print("Geen valide keuze! kiest uit JA of NEE")
    elif schimmel.lower() == "nee":
        korst2 = input("Heeft de kaas een korst? ")
        if korst2.lower() == "ja":
            print("Uw kaas is de Camembert")
        elif korst2.lower() == "nee":
            print("Uw kaas is de Mozzarella")
        else:
            print("Geen valide keuze! kiest uit JA of NEE")
    else:
        print("Geen valide keuze! kiest uit JA of NEE")
else:
    print("Geen valide keuze! kiest uit JA of NEE")



