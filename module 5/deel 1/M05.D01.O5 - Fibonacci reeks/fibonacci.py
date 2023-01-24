def fibonacci(nummer):
    nul, een = 0, 1
    while nul < nummer:
        print(nul, end=',')
        nul, een = een, nul+een
    print()
fibonacci(35)