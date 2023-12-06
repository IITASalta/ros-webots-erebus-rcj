# Descubrimientos

Es necesario compilar tanto webots_ros2 como turtlebot3 desde la fuente para entender el código. Yo los puse en un workspace separado de este repo. En este repo solo estaría nuestro código.

Para lanzar el ejemplo de turtlebot solo, sin la complicación de la navegación (esto permite analizar mejor que está pasando):

```ros2 launch webots_ros2_turtlebot robot_launch.py nav:=false```

Ese comando lanza el archivo ubicado en: ```ros2_ext_ws/src/webots_ros2/webots_ros2_turtlebot/launch/robot_launch.py```
Ese archivo es el encargado de lanzar todos los programas y nodos que vemos cuando corremos el ejemplo.

Logré controlar el turtlebot del ejemplo con un nodo propio. Para probarlo:

``` bash
ros2 launch webots_ros2_turtlebot robot_launch.py nav:=false

#En otra terminal
ros2 run my_robot_controller draw_circle
```

Gracias a los comandos para obtener información sobre los nodos, topics e interfaces y modificando el archivo de launch podemos interactuar con cualquier parte del sistema que queramos.

Tutorial sobre archivos de launch: [https://docs.ros.org/en/humble/Tutorials/Intermediate/Launch/Creating-Launch-Files.html]
