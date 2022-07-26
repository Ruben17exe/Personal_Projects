from controller import Robot, Motor, DistanceSensor
import pandas as pd
import joblib

robot = Robot()

model = joblib.load("trained_model.pkl")

timestep = int(robot.getBasicTimeStep())

front_sensor = robot.getDevice("front_sensor")
front_sensor.enable(timestep)
right_sensor = robot.getDevice("right_sensor")
right_sensor.enable(timestep)
left_sensor = robot.getDevice("left_sensor")
left_sensor.enable(timestep)

motor = robot.getDevice("motor1")
motor.setPosition(float("inf"))
motor.setVelocity(0.0)

motor2 = robot.getDevice("motor2")
motor2.setPosition(float("inf"))
motor2.setVelocity(0.0)

vel = 7

while robot.step(timestep) != -1:

    front_dist = front_sensor.getValue()
    right_dist = right_sensor.getValue()
    left_dist = left_sensor.getValue()

    samples = [[left_dist, front_dist, right_dist]]
    decision = int(model.predict(samples))
    
    if decision == 1:
        motor.setVelocity(vel)
        motor2.setVelocity(vel)
    elif decision == 2:
        motor.setVelocity(vel - 2)
        motor2.setVelocity(-vel - 2)
    elif decision == 3:
        motor.setVelocity(-vel - 2)
        motor2.setVelocity(vel - 2)
    elif decision == 0:
        motor.setVelocity(-vel)
        motor2.setVelocity(-vel)



