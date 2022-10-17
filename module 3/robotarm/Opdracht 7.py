from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
robotArm.moveRight()
for a in range (5): 
    for x in range(6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    robotArm.moveRight()
    robotArm.moveRight()