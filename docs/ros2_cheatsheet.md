## Cheatsheet

```rqt_graph```: Abre prgrama para ver los nodos, topics, etc

```ros2 node list```: lista de los nodos activos

```ros2 node info 'nombre de nodo'```: información sobre el nodo

```ros2 topic list```: lista de los tópicos activos

```ros2 topic info 'nombre de topic'```: información sobre el tópico. En la sección que dice 'Type' está la interface (el formato del mensaje de ese tópico). Para ver como es hacer ```ros2 interface show```

```ros2 interface show 'nombre de la interface'```: Muestra el formato de una interface o tipo determinado.

```ros2 topic echo 'nombre del topic```: Imprime todos los mensajes del topic

```ros2 service list```: lista de los servicios activos

```ros2 service type 'nombre del servicio'```: interface o formato del servicio. Para ver como es hacer ```ros2 interface show```. Primero se imprime el formato de la request, luego '---' y después el formato de la respuesta.

```ros2 service call 'nombre del servicio' 'nombre del formato del servicio' "{'parámetro_de_ejemplo': 'valor de ejemplo'}"```: llamar al servicio desde la terminal y obtener la respuesta (si es que manda respuesta).

```ros2 topic hz 'nombre del tópico'```: mide la frecuencia de mensajes en un tópico.
