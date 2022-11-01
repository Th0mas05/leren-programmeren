# name of student: Thomas Kooij
# number of student: 99071821
# purpose of program: hoeveel wisselgeld je hebt moeten betalen
# function of program: het uitrekenen van wisselgeld
# structure of program: 
euroValue = 0
nrCoinsReturned = 0 
toPay = int(float(input('Amount to pay: ')))*1 # doet alles * 1 zodat het in euro's is
paid = int(float(input('Paid amount: ')))*1 # doet alles * 1 zodat het in euro's is
change = paid - toPay # doet het betaalde bedrag min het bedrag dat je moet betalen

if change > 0: # als het wisselgeld hoger als 0 is
  euroValue = 5 # is de munten value 5
  
  while change > 0 and euroValue > 0: # terwijl wisselgeld hoger als 0 is en eurovalue hoger als 0 is.
    nrCoins = change // euroValue # word change en eurovalue naar beneden afgerond

    if nrCoins > 0: # als nrcoins is groter als 0
      print('return maximal ', nrCoins, ' coins of ', euroValue, ' Euro!' ) # print die hoeveel van de munten je moet betalen
      nrCoinsReturned = int(input('How many coins of ' + str(euroValue) +  ' Euro did you return? ')) # vraagt hoeveel je er hebt ingeleverd
      change -= nrCoinsReturned * euroValue # berekent hoeveel je nog moet betalen als je niet genoeg hebt betaald.
      if change > 0.1:
        print ("you have not paid the required change")
    
   
# comment on code below: 
    if euroValue == 5:
      euroValue = 3
    elif euroValue == 3:
      euroValue = 2
    elif euroValue == 2:
      euroValue = 1
    elif euroValue == 1:
      euroValue = 1
    elif euroValue == 0.50:
      euroValue = 0.50
    else:
      euroValue = 0

euroValue = str(euroValue)
nrCoinsReturned = str(nrCoinsReturned)
print ('u heeft ' + nrCoinsReturned +' coins of ' + euroValue + ' Euro payed')

if change > 0: # als wisselgeld groter is als 0 dan zegt die hoeveel je nog moet betalen
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')

# comment on code below: geeft de value's aan hoeveel de munten waard zijn.
