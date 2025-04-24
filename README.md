# Simulador de Brazo Robótico en PyBullet

Este proyecto implementa una simulación en Python de un brazo robótico con dos articulaciones utilizando la librería **PyBullet**. El modelo del robot está definido en un archivo URDF personalizado y se puede controlar de forma interactiva mediante sliders que ajustan los ángulos de cada articulación y la velocidad de simulación.

El entorno de simulación puede ejecutarse localmente o dentro de un contenedor Docker, facilitando su portabilidad.

## Archivos incluidos

- `BrazoRobotico.py`: script principal que ejecuta la simulación.
- `two_joint_robot_custom.urdf`: modelo del robot.
- `Dockerfile`: configuración para ejecutar el simulador en Docker.
- `grabacion.mkv`: archivo de video que muestra el funcionamiento del simulador.
Esto se usa para que funcione de la mejor manera al momento de hacer la simulacion en el pybullet
## Cómo ver la simulación

Para observar el movimiento del brazo robótico, dirígete al archivo `mkv` dentro de este repositorio.  
Haz clic en el botón **"View raw"** para descargarlo, y luego podrás reproducirlo en tu equipo con cualquier reproductor de video compatible (como VLC o MPV).

---

Gracias por visitar el proyecto, espero que le haya gustado profesor :v
