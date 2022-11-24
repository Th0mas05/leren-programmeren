from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
robotArm.speed = 3
for i in range(0,8):
    robotArm.moveRight()
for k in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == ("white"):
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()




robotArm.wait()