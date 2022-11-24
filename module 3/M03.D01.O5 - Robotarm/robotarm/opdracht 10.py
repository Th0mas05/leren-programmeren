from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')

x = 9
for blok in range(5):
    robotArm.grab()
    for y in range(x):
     robotArm.moveRight()
    robotArm.drop()
    x -= 1
    for y in range(x):
     robotArm.moveLeft()
    x -= 1
robotArm.wait()