from controller import Robot, Motor, Keyboard, DistanceSensor

robot = Robot()

timestep = int(robot.getBasicTimeStep())

keyboard = Keyboard()
keyboard.enable(timestep)

motor = robot.getDevice("motor1")
motor.setPosition(float("inf"))
motor.setVelocity(0.0)

motor2 = robot.getDevice("motor2")
motor2.setPosition(float("inf"))
motor2.setVelocity(0.0)

while robot.step(timestep) != -1:

    key = keyboard.getKey()
    # print("key pressed: ", key)
    if key == 315:
        motor.setVelocity(7)
        motor2.setVelocity(7)
    elif key == 317:
        motor.setVelocity(-7)
        motor2.setVelocity(-7)
    elif key == 316:
        motor.setVelocity(3)
        motor2.setVelocity(-3)
    elif key == 314:
        motor.setVelocity(-3)
        motor2.setVelocity(3)
    else:
        motor.setVelocity(0)
        motor2.setVelocity(0)
        
