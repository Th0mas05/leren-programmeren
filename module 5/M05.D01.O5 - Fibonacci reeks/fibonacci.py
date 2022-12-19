def Fibonacci(nummer):
    nul = 0
    een = 1
    if nummer == 1:
        return nul
    else:
        print(nul)
        print(een)
        for _ in range(2,nummer):
            multi = nul + een
            nul = een
            een = multi
            print(multi and nul and een) 
Fibonacci(int(input("Fibonacci reeks, Typ een positief getal hoger dan 5:\n\n>> ")))