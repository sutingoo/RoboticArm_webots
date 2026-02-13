from controller import Robot

# Inicializar el robot
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Configurar motores
nombres_motores = ['motor1', 'motor2', 'motor3', 'motor4']
motores = []

for nombre in nombres_motores:
    m = robot.getDevice(nombre)
    m.setPosition(0.0) # Posición inicial
    m.setVelocity(1.0) # Velocidad de movimiento
    motores.append(m)

# Bucle principal
while robot.step(timestep) != -1:
    # Ejemplo: mover el motor 1 a 1.5 radianes
    motores[0].setPosition(1.5)
    # Mover el hombro (motor 2) de forma oscilatoria
    import math
    motores[1].setPosition(math.sin(robot.getTime()))