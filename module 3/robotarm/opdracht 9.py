from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
for i in range(4):
    robotArm.grab()
    for a in range(6):
        robotArm.moveRight()
    robotArm.drop()
    for b in range(5):
        robotArm.moveLeft()
