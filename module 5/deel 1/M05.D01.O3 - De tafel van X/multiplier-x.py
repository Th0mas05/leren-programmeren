def tafels(getal:int):
    for i in range(1, 11):
        print(f'{i} x {getal} = {i * getal}')

tafels(int(input("Van welk getal wilt u de tafel zien?\n\n >> ")))
