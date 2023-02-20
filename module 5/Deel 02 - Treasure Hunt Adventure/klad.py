from functions import getInvestorsCuts , getAdventuringInvestors
from data import friends , investors , mainCharacter

profitGold = 500
fellowship_adventurCut = 5
aftrek_goud = sum(getInvestorsCuts(profitGold,investors))
adventurCut = (profitGold -  aftrek_goud) / fellowship_adventurCut
print(adventurCut)

profitGold = 500
fellowship_adventurCut = 5
adventurCut = (profitGold - sum(getInvestorsCuts(profitGold,investors))) / fellowship_adventurCut

print(adventurCut)