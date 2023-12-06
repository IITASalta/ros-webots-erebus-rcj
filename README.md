## Notas

Para usar el código se debería utilizar el workspace de ros del propio repositorio. Es necesario hacer todos los pasos de activación y source, solo que con la carpeta del workspace que tengan en el repo.

## Instrucciones de Instalación

#### 1. Instalar Ubuntu 22.04

Por si alguno no tiene Ubuntu en su máquina, acá hay un tutorial de como hacer un doble boot de Ubuntu y Windows: https://davesroboshack.com/installing-linux/installing-ubuntu-as-dualboot/

Descargar Ubuntu 22.04 (la que aparece primero): https://ubuntu.com/download/desktop

#### 2. Instalar Webots R2023b

Version de Webots: https://github.com/cyberbotics/webots/releases/tag/R2023b

No lo probé con la R2023a. Habría que hacer el experimento a ver si funciona.

#### 3. Instalar ROS

Seguir las instrucciones de este artículo:
https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html

Instalar el que dice "ros-humble-desktop" y el que dice "ros-dev-tools". No hace falta instalar "ros-humble-ros-base".
La instalación va a tardar un cacho y son como 2 GB de datos.

#### 4. Hacer source

directorio de home y abrir el archivo .bashrc. Agregar al final la siguientes líneas:

source /opt/ros/humble/setup.bash
export WEBOTS_HOME=/usr/local/webots

Cerrar la terminal y volverla a abrir.

#### 5. Instalar webots-ros2

Seguir las instrucciones que dicen 'Install webots_ros2 from sources':

https://docs.ros.org/en/humble/Tutorials/Advanced/Simulators/Webots/Installation-Ubuntu.html#tasks

#### 6. Instalar ejemplo de turtlebot en webots

Seguir las instrucciones de este sitio pero la del cartelito que dice 'or compile the package from source':

https://github.com/cyberbotics/webots_ros2/wiki/Navigate-TurtleBot3

Al correr el último comando de ese sitio se deberían abrir webots y R-Viz, el cual es un programa para SLAM y permite controlar el robot.
