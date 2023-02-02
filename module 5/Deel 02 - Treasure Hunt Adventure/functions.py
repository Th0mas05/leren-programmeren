import time
import math
from termcolor import colored
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HUMAN_COPPER_PER_DAY
from data import COST_FOOD_HORSE_COPPER_PER_DAY
from data import COST_TENT_GOLD_PER_WEEK
from data import COST_HORSE_SILVER_PER_DAY

##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return (amount / 10)

def silver2gold(amount:int) -> float:
    return (amount / 5)

def copper2gold(amount:int) -> float:
    return round(amount / 10 /5,2)

def platinum2gold(amount:int) -> float:
    return (amount * 25)

def getPersonCashInGold(personCash:dict) -> float:
    cop2gold = copper2gold(personCash['copper'])
    silv2gold = silver2gold(personCash['silver'])
    plat2gold = platinum2gold(personCash['platinum'])
    kaas = cop2gold + silv2gold + plat2gold
    personCash = personCash['gold'] + kaas
    return personCash

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    people_amount_copper = people * COST_FOOD_HUMAN_COPPER_PER_DAY
    people_amount_copper = people_amount_copper * JOURNEY_IN_DAYS
    people_amount_gold = copper2gold(people_amount_copper)
    round(people_amount_gold,2)
    horse_amount_copper = horses * COST_FOOD_HORSE_COPPER_PER_DAY
    horse_amount_copper = horse_amount_copper * JOURNEY_IN_DAYS
    horse_amount_gold = copper2gold(horse_amount_copper)
    round(horse_amount_gold,2)
    totaalperdag = horse_amount_gold + people_amount_gold
    return round(totaalperdag,2)

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    return [item for item in list if item[key]== value]
def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs (people,"adventuring",True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs (friends,"sharewith",True)

def getAdventuringFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, "adventuring", True)

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people/2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people/3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    return (horses * silver2gold(COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS) + (tents * (COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7)) )

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    pass

def getItemsValueInGold(items:list) -> float:
    pass

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:list) -> float:
    pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

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