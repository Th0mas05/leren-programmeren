import time
from termcolor import colored
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HUMAN_COPPER_PER_DAY
from data import COST_FOOD_HORSE_COPPER_PER_DAY
from data import COST_TENT_GOLD_PER_WEEK
from data import COST_HORSE_SILVER_PER_DAY
from data import COST_INN_HUMAN_SILVER_PER_NIGHT
from data import COST_INN_HORSE_COPPER_PER_NIGHT
import math
##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return round(amount/10,2)

def silver2gold(amount:int) -> float:
    return round(amount/5,2)

def copper2gold(amount:int) -> float:
    return round(amount/10/5,2)

def platinum2gold(amount:int) -> float:
    return round(amount*25,2)

def getPersonCashInGold(personCash:dict) -> float:
    gold1 = platinum2gold(personCash['platinum'])
    gold2 = silver2gold(personCash['silver'])
    gold3 = copper2gold(personCash['copper'])
    golderbij = gold1 + gold2 + gold3
    personCash = personCash['gold'] + golderbij
    return personCash

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    peopleCost = copper2gold(people * COST_FOOD_HUMAN_COPPER_PER_DAY * JOURNEY_IN_DAYS )
    horsesCost = copper2gold(horses * COST_FOOD_HORSE_COPPER_PER_DAY * JOURNEY_IN_DAYS)
    return round(peopleCost + horsesCost,2)
    

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    return [item for item in list if item[key] == value]

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
    namelist = []
    for i in range (len(friends)):
        if friends[i]['adventuring'] and friends[i]['shareWith'] == True:
            namelist.append(friends[i])
    return (namelist)

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2)
def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    return (horses * silver2gold(COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS) + (tents * (COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7)) )
##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    nieuwelijst = []
    for i in range (len(items)):
        nieuwelijst.append(str(items[i]['amount']) + str(items[i]['unit']) + " " + str(items[i]['name']))
    nieuwelijst = str(nieuwelijst)
    nieuwelijst = nieuwelijst.replace("[", "")
    nieuwelijst = nieuwelijst.replace("]", "")
    nieuwelijst = nieuwelijst.replace("'", "")
    return nieuwelijst
def getItemsValueInGold(items:list) -> float:
    goldtotal = 0
    for i in range (len(items)):
        typengeld = (items[i]['price']['type'])
        if typengeld == 'copper':
            goldtotal += copper2gold(items[i]['amount'] * items[i]['price']['amount'])
        elif typengeld == 'platinum':
            goldtotal += platinum2gold(items[i]['amount'] * items[i]['price']['amount'])
        elif typengeld == 'silver':
            goldtotal += silver2gold(items[i]['amount'] * items[i]['price']['amount'])
        elif typengeld == 'gold':
            goldtotal += (items[i]['amount'] * items[i]['price']['amount'])
    return round(goldtotal,2)

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    goldtotal = 0
    for i in range (len(people)):
        golderbij = getPersonCashInGold(people[i]['cash'])
        goldtotal += golderbij
    return goldtotal
##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    nieuwelijst = []
    for i in range (len(investors)):
        procenten = investors[i]['profitReturn']
        if procenten <10:
            nieuwelijst.append(investors[i])
    return (nieuwelijst)

def getAdventuringInvestors(investors:list) -> list:
    namelist = []
    for i in range (len(investors)):
        profitreturn = investors[i]['profitReturn']
        if profitreturn <10 and investors[i]['adventuring'] == True:
            namelist.append(investors[i])
    return (namelist)

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    aantalmee = len(getAdventuringInvestors(investors))
    tentcostjourney = COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7)
    horsecostjourney = silver2gold(COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS * aantalmee
    horsesCost = copper2gold(aantalmee * COST_FOOD_HORSE_COPPER_PER_DAY * JOURNEY_IN_DAYS)
    investorCostfood = copper2gold(COST_FOOD_HUMAN_COPPER_PER_DAY * JOURNEY_IN_DAYS * aantalmee)
    costgear = getItemsValueInGold(gear)
    return round(tentcostjourney + horsecostjourney + investorCostfood + costgear + horsesCost,2)

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    horsegoldPerNight = copper2gold (COST_INN_HORSE_COPPER_PER_NIGHT*horses)
    humangoldPerNight = silver2gold (COST_INN_HUMAN_SILVER_PER_NIGHT*people)
    totalCostPerNight = horsegoldPerNight + humangoldPerNight
    nights = math.floor(leftoverGold / totalCostPerNight)
    return nights
def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    horsegoldPerNight = copper2gold (COST_INN_HORSE_COPPER_PER_NIGHT*horses)
    humangoldPerNight = silver2gold (COST_INN_HUMAN_SILVER_PER_NIGHT*people)
    totalCostPerNight = horsegoldPerNight + humangoldPerNight
    totalcost = round(totalCostPerNight * nightsInInn,2)
    return totalcost

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    totalInvestorCut = []
    for i in range (len(investors)):
        procenten = investors[i]['profitReturn']
        if procenten <10:
            totalInvestorCut.append(round(profitGold / 100 * procenten,2))
    return totalInvestorCut

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:list) -> float:
    for i in range (len(investorsCuts)):
        profitGold = profitGold - investorsCuts[i]
    fellowsshipcut = profitGold / fellowship
    return round(fellowsshipcut,2)

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []
    earnings.append(profitGold)
    # haal de juiste inhoud op
    adventuringFriends = getAdventuringFriends(friends)
    interestingInvestors = getInterestingInvestors(investors)
    adventuringInvestors = getAdventuringInvestors(investors)
    investorsCuts = getInvestorsCuts(profitGold, investors)
    goldCut = getAdventurerCut(profitGold, investorsCuts, len(people))
    # verdeel de uitkomsten
    
    for person in people:
        start = 0
        end = 0
        name = person.get('name', '')
        start = person.get('cash', {}).get('gold', 0)
        print (name,start)
        if person in adventuringFriends:
            end = start + goldCut
        elif person in interestingInvestors or person in adventuringInvestors:
            getInvestorsCut = (len(investors)) 
            

        earnings.append({
            'name'   : name,
            'start'  : start,
            'end'    : end
        })

    return earnings

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()