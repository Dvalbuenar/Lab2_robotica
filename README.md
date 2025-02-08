# Laboratorio 2 de Robótica 
## Análisis y Operación del Manipulador Motoman MH6
### Autores:
- Jonathan Andrés Jiménez Trujillo
- Daniel Felipe Valbuena Reyes
## Cuadro comparativo de Motoman MH6 y IRB140.
| **Item** | **Motoman MH6** | **IRB140** |
|:---------|:----------------|:-----------|
| **Carga máxima** | 6 kg | 5 kg |
| **Alcance** | 1422 mm | 810 mm |
| **Grados de libertad** | 6 | 6 |
| **Repetibilidad** | $\pm$ 0.08 mm | $\pm$ 0.03 mm|
| **Número de ejes** | 6 | 6|
| **Consumo de potencia** | 1.5 kVA | 4.5 kVA|
| **Rango de rotación de articulaciones**            |||
| Eje 1                       | $\pm$ 170°        | $\pm$ 180°    |
| Eje 2                       | +155°/-90°        | +110°/-90°    |
| Eje 3                       | +250°/-175°        | +50°/-230°    |
| Eje 4                       | $\pm$ 180°        | $\pm$ 200°    |
| Eje 5                       | +225°/-45°        | $\pm$ 115°    |
| Eje 6                       | $\pm$ 360°        | $\pm$ 400°    |
| **Velocidad** |  |  |
| Eje 1 | 140°/s | 200°/s |
| Eje 2 | 130°/s | 200°/s |
| Eje 3 | 135°/s | 260°/s |
| Eje 4 | 270°/s | 360°/s |
| Eje 5 | 270°/s | 360°/s |
| Eje 6 | 400°/s | 450°/s |
| **Torque máximo en articulaciones**        |||
| Art. 4                       | 11.8 Nm     | 8.58 Nm  |
| Art. 5                       | 9.8 Nm      | 8.58 Nm  |
| Art. 6                       | 5.9 Nm      | 4.91 Nm  |
| **Aplicaciones** | Tiene aplicaciones normalmente en áreas como montaje y ensamble, soldadura y corte, carga y descarga de materiales, inspección visual, entre otros. | Aplicaciones como manipulación de piezas y ensamblaje, manipulación de componentes pequeños, carga y descarga automatizada, entre otros. |
| **POSE Accuracy (mm)** | 0.08 | 0.02 |
| **Masa** | 130 kg | 98 kg |
| **Controlador** | DX100 | IRC5 |
| **Protección IP** | IP67 (Muñeca) IP54 (Cuerpo) |  IP67 (Muñeca) IP30 (Cuerpo) |
| **Espacio de trabajo** | ![Espacio de trabajo Motoman](/images/EspacioMotomanMH6.png) | ![Espacio de trabajo ABB IRB140](/images/EspacioABBIRB140.png)|

  
## Descripción de las configuraciones de home del Motoman MH6
El manipuladior Motoman MH6 cuenta con dos posiciones de Home desde fábrica.
Para las diferencias entre las posiciones de Home 1 y Home 2, es una ligera variación entre la posición del manipulador, pues en la primera disposición del Home, se tiene que todas las articulaciones del manipulador se encuentran a 0 grados. Sin embargo, en la segunda posicion de Home, se tiene una variación en las articulaciónes 2 y 3, que possen un valor de 45° y -45° respectivamente, por lo que el manipulador se encuentra como en una posición encogida, ocupando menos espacio y altura si se compara con la primera configuración. 

La selección de la posición de Home, dependera de las necesidades que tenga el usuario, por ejemplo en la primera, se facilita el acceso a todas las partes del manipulador como para hacer mantenimiento, y en la segunda, como se mencionó anteriormente, para ocupar menos espacio en el lugar de trabajo y tener sensación de estar recogido.
  
## Procedimiento detallado manipulación de Motoman
En el manipulador Motoman, como en el ABB IRB 140, el cuál se uso en el primer laboratorio, se puede realizar movimiento por ejes, modificando el ángulo de cada una de las articulaciones, o por el sistema de coordenadas cartesianas.

1. En el teach pendant se selecciona la opción de manejo manual, se consigue girando la llave a la posición de "Teach".
2. Mediante la tecla "Coord", se puede hacer la selección del tipo de coordenadas que se quiere utilizar.
3. Se puede hacer la configuración de la velocidad de operación del manipulador, como se vera más adelante.
4. Se pulsa el boton de Enable Switch ubicado en la parte posterior del teach pendant, para activar los servos.
5. Según el modo seleccionado, se presionan los botones correspondientes para hacer movimiento de las articulaciones nombradas S L U R B T, que van desde la 1 a 6 en ese orden. O para movimiento cartesiano ±X, ±Y, ±Z, (traslación) ±RX, ±RY, ±RZ (movimiento) 
6. Mantener presionado "Enable" y mover en la dirección deseada hasta alcanzar la posición requerida.

A continuación unas imagenes que ilustran de mejor manera el pendant, los botones, velocidades y más.

![image](https://github.com/user-attachments/assets/5995cea6-5c5a-49e2-b1a3-bebf17451290) ![image](https://github.com/user-attachments/assets/c8e13e32-b1da-458b-8fd3-2bfcf1417f5a) ![image](https://github.com/user-attachments/assets/6d2ddac3-b8ad-471e-8149-693e2fd0bf73) ![image](https://github.com/user-attachments/assets/293536dc-213b-4451-9647-ace42ccb6c72) ![image](https://github.com/user-attachments/assets/054ea505-0aca-4cac-bcf2-f5f296f15945)



## Explicación sobre niveles de velocidad
La velocidad con la que opera el manipulador, se puede ajustar entre Inching, Low speed, Medium Speed y High Speed. Se pueden ir cambiando entre estas velocidades, presionando los botones del pendant correspondientes a "Slow" y "Fast", de esta manera se incrementa o disminuye la velocidad según la que se tenga actualmente.

![image](https://github.com/user-attachments/assets/f77eab09-4766-4f31-8616-6c671bd576d4)


## Descripción de las funcionalidades de RoboDK
El software de RoboDK es una herramienta de programación y simulación para robots industriales, pues a pesar de que en el laboratorio se está utilizando para hacer control del robot Motoman, cuenta con una extensa bibilioteca de más de 1000 robots de diferentes fabricantes con los que se puede trabajar e interactuar. Permite hacer la calibración de diferentes tipos de herramientas, no se requiere una experiencia previa de programación, permite la creacion de gemelos digitales.

Brinda diferentes herramientas que pueden ser muy útiles para la aplicación y desarrollo, como lo es la capacidad de importar diseños 3D de CAD, brindando de esta manera tener mayor precisión y personalización con las herramientas que se trabajan, el entorno o piezas. Otra herramienta que facilita el uso del software, es la implementación de scripts con Python, con esta API se puede generar secuencias automatizadas, tener un control más preciso y optimizado de las trayectorias y mucho más. 

Además, se puede hacer uso dentro del software de probar las simulaciones bajo ciertas condiciones virtuales, con el fin de comprobar posibles colisiones, precisión, seguridad, y diferentes parámetros importantes previos a un desarrollo físico, e incluso integrar sensores, visión artificial, cámaras, entre otros, para representar escenarios cada vez más realistas.

## Comunicación RoboDK - manipulador
En primera instancia, se debe cambiar en el pendant la llave para seleccionar la opción de "Remote". Luego se entra en la opción de conectar en el RoboDK y pulsar la opción "Conectar Robot", como se ve en la imagen:

![image](https://github.com/user-attachments/assets/89d70664-90e1-4089-858f-7a533b62259c)

Esta comunicación en la sala CAM se realiza a través de la conexión TCP/IP que brinda la red local de la universidad para la comunicación, ya sea entre PC-robot o PC-PAC.

En la ventana que  aparece, con los recuadros de la dirección IP del robot, puerto del Robot, y demás. Se debe asignar la dirección y puerto del robot, se comprueba con un ping para confirmar que es posible realizar la conexión. Se presiona en el botón de "Conectar", y debe aparecer en verde el estado de la conexión con "Ready".
Finalmente, para ejecutar el programa de la trayectoria polar, se hace click derecho en el archivo .py, y se selecciona "Ejecutar en el robot". De esta manera ya el manipulador iniciará la trayectoria programada.



## Análisis comparativo entre RoboDK y RobotStudio

![image](https://github.com/user-attachments/assets/805545be-1a80-48bb-a1ef-fc2e0b5a1b67)

## Trayectoria polar
### Código de la trayectoria

En el presente en enlace se encuentra el [código de la trayectoria](programs/Lissajous.py) realizado en Python con el uso de coordenadas polares como lo solicitado en el documento.

### Simulación RoboDK

https://github.com/user-attachments/assets/52ac481b-d20e-45df-8a98-4e02ce0a7d2a

### Implementación manipulador Motoman MH6 -  Sala CAM

https://github.com/user-attachments/assets/04346322-55e4-4e54-94a4-a837adaa0cbe

## Referencias.
+ [Documento con las especificaciones técnicas del Manipulador Motoman MH6.](https://pdf.directindustry.com/pdf/motoman/motoman-mh6-series-robots/14474-97220-_2.html)
+ [Documento con las especificaciones técnicas del Manipulador ABB IRB140.](https://library.e.abb.com/public/73e6655d65ab9569c1257b440052382f/IRB%20140%20datasheet.pdf)
+ [Información del Foro Knowledge Motoman sobre las posiciones de Home](https://knowledge.motoman.com/hc/en-us/articles/4415152176791-Home-Position-Second-Home-Position-and-Work-Home-Position)
