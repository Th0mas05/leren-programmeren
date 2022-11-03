from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')

robotArm.speed = 2
a = 8
for i in range(9):
    robotArm.grab()
    if robotArm.scan() == "red":
        for i in range(9):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(a):
            robotArm.moveLeft()
        a -= 1
    else:
        robotArm.drop()
        robotArm.moveRight()
        a -= 1
robotArm.wait()
        


    