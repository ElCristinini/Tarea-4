import pybullet as p
import pybullet_data
import time
import numpy as np
import os

robot_urdf_path = "two_joint_robot_custom.urdf"

if not os.path.exists(robot_urdf_path):
    print(f"ERROR: No se encuentra el archivo {robot_urdf_path}")
    input("Presiona Enter para salir...")
    exit()

# Iniciar PyBullet
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 1)

# Cámara ajustada
p.resetDebugVisualizerCamera(cameraDistance=2, cameraYaw=45, cameraPitch=-30, cameraTargetPosition=[0, 0, 0.5])
p.setGravity(0, 0, -9.8)

# Plano
p.loadURDF("plane.urdf")

# Cargar robot
robotId = p.loadURDF(robot_urdf_path, [0, 0, 0.2], useFixedBase=True)
print(f"Robot cargado con ID: {robotId}")

# Mostrar joints disponibles
num_joints = p.getNumJoints(robotId)
print(f"Número de joints detectados: {num_joints}")
for i in range(num_joints):
    info = p.getJointInfo(robotId, i)
    print(f"Joint {i}: {info[1].decode('utf-8')}")

# Asignar sliders solo a joints articulados
joint1_slider = p.addUserDebugParameter("Joint 1", -np.pi, np.pi, 0)
joint2_slider = p.addUserDebugParameter("Joint 2", -np.pi, np.pi, 0)
speed_slider = p.addUserDebugParameter("Velocidad", 0.1, 10.0, 1.0)
pause_button = p.addUserDebugParameter("Pausar/Continuar", 1, 0, 1)

# Loop de simulación
last_pause_value = 1
try:
    while True:
        current_pause_value = p.readUserDebugParameter(pause_button)
        if current_pause_value != last_pause_value:
            print("Simulación pausada/continuada")
        last_pause_value = current_pause_value

        # Leer sliders
        joint1_value = p.readUserDebugParameter(joint1_slider)
        joint2_value = p.readUserDebugParameter(joint2_slider)
        speed = p.readUserDebugParameter(speed_slider)

        # Controlar articulaciones (revisamos los joints válidos)
        p.setJointMotorControl2(robotId, 0, p.POSITION_CONTROL, targetPosition=joint1_value, force=100)
        p.setJointMotorControl2(robotId, 1, p.POSITION_CONTROL, targetPosition=joint2_value, force=100)

        p.stepSimulation()
        time.sleep(0.01 / speed)

except KeyboardInterrupt:
    print("Simulación finalizada.")
    input("Presiona Enter para cerrar...")
    p.disconnect()
