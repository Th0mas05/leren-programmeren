from random import randint

play = True
ronde = 1
bomb = randint(1,1)
score = 0

while play == True:

    geuss = input("Ronde "+str(ronde)+": Op welk getal denkt U dat de bom ligt ")

    ronde = ronde + 1
    nextRound = input("Wilt nu naar ronde "+str(ronde)+" (Y/N)? ").lower()

    if nextRound == "n":
        play = False
    
    print(score)

