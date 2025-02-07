# Laboratorio 2 de Robótica 
## Análisis y Operación del Manipulador Motoman MH6
### Autores:
Jonathan Andrés Jiménez Trujillo

Daniel Felipe Valbuena Reyes

  ## Cuadro comparativo de Motoman MH6 y IRB140.
  | **Item** | **Motoman MH6** | **IRB140** |
  |:---------|:----------------|:-----------|
  | **Carga máxima** | 6 kg | 6 kg |
  | **Alcance** | 1.42 m | 0.8 m |
  | **Grados de libertad** | 6 | 6 |
  | **Velocidad** |  |  |
  | Eje 1 | 140°/s | 200°/s |
  | Eje 2 | 130°/s | 200°/s |
  | Eje 3 | 135°/s | 260°/s |
  | Eje 4 | 270°/s | 360°/s |
  | Eje 5 | 270°/s | 360°/s |
  | Eje 6 | 400°/s | 450°/s |
  | **Aplicaciones** | Tiene aplicaciones normalmente en áreas como montaje y ensamble, soldadura y corte, carga y descarga de materiales, inspección visual, entre otros. | Aplicaciones como manipulación de piezas y ensamblaje, manipulación de componentes pequeños, carga y descarga automatizada, entre otros. |
  | **POSE Accuracy (mm)** | 0.08 | 0.02 |
  | **Peso** | 130 kg | 98 kg |
  | **Espacio de trabajo** | ![image](https://github.com/user-attachments/assets/27c0c3b3-9e19-4acf-aade-b0b15fd497ea) | ![image](https://github.com/user-attachments/assets/7f496555-e9cc-4878-9acb-975518791878) |

  
  ## Descripción de las configuraciones de home del Motoman MH6
  Para las diferencias entre las posiciones de Home 1 y Home 2, es una ligera variación entre la posición del manipulador, pues en la primera disposición del Home, tenemos que todas las articulaciones del manipulador se encuentran a 0 grados. Sin embargo, en la segunda posicion de Home, tenemos una variación en las articulaciónes 2 y 3, que tienen un valor de 45° y -45° respectivamente, por lo que el manipulador se encuentra como en una posición encogida, ocupando menos espacio y altura que en la primera configuración. 

La selección de la posición de Home, dependera de las necesidades que tenga el usuario, por ejemplo en la primera, se facilita el acceso a todas las partes del manipulador como para hacer mantenimiento, y en la segunda, como se mencionó anteriormente, para ocupar menos espacio en el lugar de trabajo y tener sensación de estar recogido.
  
  ## Procedimiento detallado manipulación de Motoman
En el manipulador Momotman, como en el ABB IRB 140 en que hicimos el primer laboratorio, se puede realizar movimiento por ejes, modificando el ángulo de cada una de las articulaciones, o por el sistema de coordenadas cartesianas.

1. En el teach pendant seleccionamos la opción de manejo manual, se consigue girando la llave a la posiciónde "Teach".
2. Mediante la tecla "Coord", podemos hacer la selección de las coordenadas que queremos utilizar.
3. Se puede hacer la configuración de la velocidad de operación del manipulador, como lo veremos más adelante.
4. Se pulsa el boton de Enable Switch ubicado en la parte posterior del teach pendant, para activar los servos.
5. Según el modo seleccionado, pulsamos los botones correspondientes para hacer movimiento de las articulaciones nombradas S L U R B T, que van desde la 1 a 6 en ese orden. O que corresponden al movimiento de sistemas coordenado, a lo largo de los ejes, o rotaciones alrededor de uno de ellos.

A continuación unas imagenes que ilustran de mejor manera el pendant, los botones, velocidades y más.
![image](https://github.com/user-attachments/assets/5995cea6-5c5a-49e2-b1a3-bebf17451290) ![image](https://github.com/user-attachments/assets/c8e13e32-b1da-458b-8fd3-2bfcf1417f5a) ![image](https://github.com/user-attachments/assets/6d2ddac3-b8ad-471e-8149-693e2fd0bf73) ![image](https://github.com/user-attachments/assets/293536dc-213b-4451-9647-ace42ccb6c72) ![image](https://github.com/user-attachments/assets/054ea505-0aca-4cac-bcf2-f5f296f15945)



  ## Explicación sobre niveles de velocidad
  La velocidad con la que opera el manipulador, se puede ajustar entre Inching, Low speed, Medium Speed y High Speed. Podemos ir cambiando en estas velocidades, oprimiendo los botones del pendant correspondientes a "Slow" y "Fast", de esta manera se incrementa o disminuye la velocidad según la que tengamos actualmente.
  ![image](https://github.com/user-attachments/assets/f77eab09-4766-4f31-8616-6c671bd576d4)

  
  ## Descripción de las funcionalidades de RoboDK
  El software de RoboDK es una gerramienta de programación y simulación para robots industriales, pues a pesar de que en el laboratorio lo estams utilizando para hacer control del robot Motoman, cuenta con una extensa bibilioteca de más de 1000 robots de diferentes fabricantes con los que podemos trabajar e interactuar. Permite hacer la calibración de diferentes tipos de herramientas, no se requiere una experiencia previa de programación, permite crear un gemelo digital.

Nos brinda diferentes herramientas que pueden ser muy útiles para la aplicación y desarrollo, como lo es la capacidad de importar diseños 3D de CAD, pudiendo de esta manera tener mayor precisión y personalización con las herramientas que se trabajan, el entorno o piezas. Otra herramienta que facilita el uso del software, es la implementación de scripts con Python, con esta API podremos generar secuencias automatizadas, tener un control más preciso y optimizado de las trayectorias y mucho más. 

Además, podremos hacer uso dentro del software de probar las simulaciones bajo ciertas condiciones virtuales, con el fin de comprobar posibles colisiones, precisión, seguridad, y diferentes parámetros importantes previos a un desarrollo físico, e incluso integrar sensores, visión artificial, cámaras, entre otros, para representar escenarios cada vez más realistas.

## Comunicación con el RoboDK
En primera instancia, debemos cambiar en el pendant la llave para seleccionar la opción de "Remote". Luego debemos entrar en la opción de conectar en el RoboDK y pulsar la opción "Conectar Robot", como se ve en la imagen:
![image](https://github.com/user-attachments/assets/89d70664-90e1-4089-858f-7a533b62259c)

En la ventana que nos aparece, con los recuadros de la dirección IP del robot, puerto del Robot, y demás. Debemos asignar la dirección y puerto del robot, comprobamos con un ping para confirmar que es posible realizar la conexión. Pulsamos el botón de "Conectar", y nos debe aparecer en verde el estado de la conexión con "Ready".
Finalmente, para ejecutar el programa de la trayectoria polar, hacemos click derecho en el archivo .py, y seleccionamos "Ejecutar en el robot". De esta manera ya el manipulador iniciará la trayectoria programada.


  
  ## Análisis comparativo entre RoboDK y RobotStudio
![image](https://github.com/user-attachments/assets/805545be-1a80-48bb-a1ef-fc2e0b5a1b67)

  


  
