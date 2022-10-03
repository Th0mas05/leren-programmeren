from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
for groen in range(3):
    robotArm.moveRight()
robotArm.drop()

for wit in range(3):
    robotArm.moveLeft()

robotArm.grab()
for wit in range(2):
    robotArm.moveRight()
robotArm.drop()

for blauw in range(2):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()

robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()

robotArm.moveRight()
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.moveLeft()
robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()