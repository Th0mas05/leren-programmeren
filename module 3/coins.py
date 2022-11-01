# name of student: 
# number of student: 
# purpose of program: hoeveel wisselgeld je hebt moeten betalen
# function of program: het uitrekenen van wisselgeld
# structure of program: 
euroValue = 0
nrCoinsReturned = 0 
toPay = int(float(input('Amount to pay: ')))*1 
paid = int(float(input('Paid amount: ')))*1 
change = paid - toPay 

if change > 0: 
  euroValue = 5 
  
  while change > 0 and euroValue > 0: 
    nrCoins = change // euroValue 

    if nrCoins > 0: 
      print('return maximal ', nrCoins, ' coins of ', euroValue, ' Euro!' ) 
      nrCoinsReturned = int(input('How many coins of ' + str(euroValue) +  ' Euro did you return? ')) 
      change -= nrCoinsReturned * euroValue 
      if change > 0.1:
        print ("you have not paid the required change")
    
   
# comment on code below: 
    if euroValue == 5:
      euroValue = 3
    elif euroValue == 2:
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
