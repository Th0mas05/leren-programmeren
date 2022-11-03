from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:
a = 7
for i in range(6):
    robotArm.grab()
    if robotArm.scan == "red" or "blue" or "yellow" or "white" or "green":
        for x in range(a):
            robotArm.moveRight()
        robotArm.drop()
        for c in range(a):
            robotArm.moveLeft()
        a-= 1
    else:
        robotArm.wait()




# Na jouw code wachten tot het sluiten van de window:
