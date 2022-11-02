# name of student: Thomas Kooij
# number of student: 99071821
# purpose of program: hoeveel wisselgeld je hebt moeten betalen
# function of program: het uitrekenen van wisselgeld
# structure of program:

nrCoinsReturned500 = 0
nrCoinsReturned200 = 0
nrCoinsReturned100 = 0
nrCoinsReturned50 = 0
nrCoinsReturned20 = 0
nrCoinsReturned10 = 0
nrCoinsReturned5 = 0
nrCoinsReturned2 = 0
nrCoinsReturned1 = 0

toPay = int(float(input('Amount to pay: ')))*100 # doet alles * 1 zodat het in euro's is
paid = int(float(input('Paid amount: ')))*100 # doet alles * 1 zodat het in euro's is
change = paid - toPay # doet het betaalde bedrag min het bedrag dat je moet betalen

if change > 0: # als het wisselgeld hoger als 0 is
  coinValue = 500 # is de munten value 500
  
  while change > 0 and coinValue > 0: # terwijl wisselgeld hoger als 0 is en eurovalue hoger als 0 is.
    nrCoins = change // coinValue # wordt change en eurovalue naar beneden afgerond

    if nrCoins > 0: # als nrcoins is groter als 0
      print('return maximal',nrCoins,'coins of',coinValue,'cents!' ) # print die hoeveel van de munten je moet betalen
      nrCoinsReturned = int(input('How many coins of '+ str(coinValue) + ' cents did you return? ')) # vraagt hoeveel je er hebt ingeleverd
      change -= int(nrCoinsReturned) * coinValue # berekent hoeveel je nog moet betalen als je niet genoeg hebt betaald.
      if change > 0:
        print ("you have not paid the required change")
    
   
# comment on code below: 
    if coinValue == 500:
      nrCoinsReturned500 = int(nrCoinsReturned)
      coinValue = 200
    elif coinValue == 200:
      nrCoinsReturned200 = int(nrCoinsReturned)
      coinValue = 100
    elif coinValue == 100:
      nrCoinsReturned100 = int(nrCoinsReturned)
      coinValue = 50
    elif coinValue == 50:
      nrCoinsReturned50 = int(nrCoinsReturned)
      coinValue = 20
    elif coinValue == 20:
      nrCoinsReturned20 = int(nrCoinsReturned)
      coinValue = 10
    elif coinValue == 10:
      nrCoinsReturned10 = int(nrCoinsReturned)
      coinValue = 5
    elif coinValue == 5:
      nrCoinsReturned5 = int(nrCoinsReturned)
      coinValue = 2
    elif coinValue == 2:
      nrCoinsReturned2 = int(nrCoinsReturned)
      coinValue = 1
    else:
      coinValue = 0


if change > 0: # als wisselgeld groter is als 0 dan zegt die hoeveel je nog moet betalen
  print('Change not returned: ', str(change) +' cents')
else:
  print('done')

# comment on code below: geeft de value's aan hoeveel de munten waard zijn.
print (' _____________________________________________________________ ')
print ('|                                                             |')
print ('| u heeft '+ str(nrCoinsReturned500) +' coins of 5 Euro payed |')
print ('| u heeft '+ str(nrCoinsReturned200) +' coins of 2 Euro payed |')
print ('| u heeft '+ str(nrCoinsReturned100) +' coins of 1 Euro payed |')
print ('| u heeft '+ str(nrCoinsReturned50) +' coins of 50 cent payed |')
print ('| u heeft '+ str(nrCoinsReturned20) +' coins of 20 cent payed |')
print ('| u heeft '+ str(nrCoinsReturned10) +' coins of 10 cent payed |')
print ('| u heeft '+ str(nrCoinsReturned5) +' coins of 5 cent payed |')
print ('| u heeft '+ str(nrCoinsReturned2) +' coins of 2 cent payed |')
print ('| u heeft '+ str(nrCoinsReturned1) +' coins of 1 cent payed |')
print ('|_____________________________________________________________|')