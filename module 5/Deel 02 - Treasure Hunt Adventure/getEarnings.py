from data import *
from functions import *

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    # haal de juiste inhoud op
    adventuringFriends = getAdventuringFriends(friends)
    interestingInvestors = getInterestingInvestors(investors)
    investorsCuts = getInvestorsCuts(profitGold , interestingInvestors)
    goudToAvonturier = 0.0

    #lijst maken 
    people = [mainCharacter] + adventuringFriends + interestingInvestors
    fellowship = [mainCharacter] + adventuringFriends #voor het delen van goud
    earnings = []

    # verdeel de uitkomsten
    for index in range (len(interestingInvestors)): #Delen van goud voor Investors
        startCash = round(getPersonCashInGold(interestingInvestors[index]['cash']) , 2)
        investorsGoud = (round(profitGold / 100 * interestingInvestors[index][ 'profitReturn'] , 2)) + startCash
        earnings.append({
                'name'   : interestingInvestors[index]['name'],
                'start'  : startCash,
                'end'    : investorsGoud
            })
    
    for gold in investorsCuts:
            profitGold -= gold #goud van investors aftrekken  
    adventurCut = round(profitGold / len(fellowship) ,2)
    
    for teller in range (len(adventuringFriends)): #Delen van goud voor Adventuring
        startCash = round(getPersonCashInGold(people[teller]['cash']) , 2)
        goudToAvonturier += 10        
        endCash = startCash + (adventurCut-10)
        earnings.append({
                'name'   : people[teller]['name'],
                'start'  : startCash,
                'end'    : endCash
            })
        profitGold -= adventurCut
    
    mainCharacter_startCash = round(getPersonCashInGold(mainCharacter['cash']) , 2)
    mainCharacter_endCash = mainCharacter_startCash + goudToAvonturier + adventurCut
    earnings.append({
                'name'   : mainCharacter['name'],
                'start'  : mainCharacter_startCash,
                'end'    : mainCharacter_endCash
            })
    return earnings
