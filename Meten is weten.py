A = input("Vul een getal in! ")
B = input("Vul een getal in! ")

if A > B: 
    max = A
    min = B
    print("A is het grootste getal!")
    print("Het minimum getal is:",min,)
    print("Het maximum getal is:",max,)
elif B > A:
    max = B
    min = A
    print("A is het kleinste getal!")
    print("Het minimum getal is:",min,)
    print("Het maximum getal is:",max,)
if A == B:
    print ("A is gelijk aan B")