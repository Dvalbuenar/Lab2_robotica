from robodk.robolink import *    # API para comunicarte con RoboDK
from robodk.robomath import *    # Funciones matemáticas
import math

#------------------------------------------------
# 1) Conexión a RoboDK e inicialización
#------------------------------------------------
RDK = Robolink()

# Seleccionar un robot (popup si hay más de uno)
robot = RDK.ItemUserPick("Selecciona un robot", ITEM_TYPE_ROBOT)
if not robot.Valid():
    raise Exception("No se ha seleccionado un robot válido.")

#------------------------------------------------
# 2) Cargar el Frame (ya existente) donde quieres dibujar
#    Ajusta el nombre si tu Frame se llama diferente
#------------------------------------------------
frame_name = "Frame_from_Target1"
frame = RDK.Item(frame_name, ITEM_TYPE_FRAME)
if not frame.Valid():
    raise Exception(f'No se encontró el Frame "{frame_name}" en la estación.')

# Asignamos este frame al robot
robot.setPoseFrame(frame)
# Usamos la herramienta activa
robot.setPoseTool(robot.PoseTool())

# Ajustes de velocidad y blending
robot.setSpeed(100)   # mm/s - Ajusta según necesites
robot.setRounding(5)  # blending (radio de curvatura)

#------------------------------------------------
# 3) Parámetros de la figura Lissajous
#------------------------------------------------
num_points = 720         # Cuántos puntos muestreamos (mayor = más suave)
A = 150                  # Amplitud en el eje X
B = 150                  # Amplitud en el eje Y
a = 3                    # Número de oscilaciones en el eje X
b = 2                    # Número de oscilaciones en el eje Y
z_surface = 0            # Z=0 en el plano del frame
z_safe = -50              # Altura segura para aproximarse y salir

#------------------------------------------------
# 4) Movimiento al centro en altura segura
#------------------------------------------------
# El centro de la figura Lissajous (x=0, y=0) corresponde a x=0, y=0
robot.MoveJ(transl(0, 0, z_surface + z_safe))

# Bajamos a la "superficie" (Z=0)
robot.MoveL(transl(0, 0, z_surface))

#------------------------------------------------
# 5) Dibujar la figura de Lissajous
#    x = A * sin(a * theta)
#    y = B * sin(b * theta)
#------------------------------------------------
# Recorremos theta de 0 a 2*pi (una vuelta completa)
full_turn = 2 * math.pi  # Un ciclo completo (0 a 2pi)

for i in range(num_points + 1):
    # Fracción entre 0 y 1
    t = i / num_points
    # Ángulo actual
    theta = full_turn * t

    # Calculamos las posiciones X y Y en el plano
    x = A * math.sin(a * theta)
    y = B * math.sin(b * theta)

    # Movemos linealmente (MoveL) en el plano del Frame
    robot.MoveL(transl(x, y, z_surface))

# Al terminar, subimos de nuevo para no chocar
robot.MoveL(transl(x, y, z_surface + z_safe))

print(f"¡Figura (Lissajous) completada en el frame '{frame_name}'!")

