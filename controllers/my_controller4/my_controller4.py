from controller import Robot
import math

robot = Robot()
timestep = int(robot.getBasicTimeStep())

nombres = ['motor1', 'motor2', 'motor3']
motores = []

for n in nombres:
    m = robot.getDevice(n)
    if m:
        m.setPosition(0.0)
        m.setVelocity(0.8)  
        motores.append(m)
    else:
        print(f"No se halla el motor {n}")

while robot.step(timestep) != -1:
    t = robot.getTime()
    
    motores[0].setPosition(2 * math.sin(t))
    
    if t > 2.0:
        motores[1].setPosition(-0.6)
        
    if t > 4.0:
        motores[2].setPosition(-0.7 * abs(math.sin(t)))