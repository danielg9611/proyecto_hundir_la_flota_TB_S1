# Hundir la Flota

¡Bienvenido a Hundir la Flota! Este es un juego de batalla naval implementado en Python. El objetivo del juego es hundir todos los barcos del oponente antes de que él hunda los tuyos.

## Estructura del Proyecto

El proyecto tiene la siguiente estructura de archivos:

- `art.py`: Contiene el arte ASCII que se muestra al inicio del juego.
- `main.py`: Contiene la lógica principal del juego.
- `player.py`: Define la clase `Player` que maneja la lógica de los jugadores, tanto humano como computadora.
- `test.py`: Contiene ejemplos de tableros para pruebas.
- `utils.py`: Contiene funciones utilitarias, como la función `print_boards` para imprimir los tableros.

## Cómo Jugar

1. Clona el repositorio en tu máquina local.
2. Asegúrate de tener Python instalado.
3. Ejecuta el archivo `main.py` para iniciar el juego:  
  .En la terminal escribe lo siguiente en el directorio del codigo

```sh
python main.py
```

## Reglas del Juego

- El juego se juega en un tablero de 10x10.
- Cada jugador tiene una flota de barcos de diferentes tamaños.
- Los jugadores se turnan para disparar a las coordenadas del tablero del oponente.
- El objetivo es hundir todos los barcos del oponente.

## Funcionalidades

- **Usuario vs Computadora:** Puedes jugar contra la computadora.
- **Lógica de Disparo de la Computadora:** La computadora tiene una lógica para disparar a las casillas adyacentes si acierta un barco.
- **Arte ASCII:** El juego muestra un arte ASCII al inicio.

## Trabajos Futuros

1. Mejorar la logica de la computadora
    - Hacer que la computadora tenga una lógica de juego más avanzada, como recordar las posiciones de los disparos fallidos y ajustar su estrategia en consecuencia.

2. Mejorar la experiencia del usuario
    - Hacer mejoras tanto graficas como de flujo del juego para que sea mas comprensible y legible para los usuarios


## Ejemplo de Uso

Al iniciar el juego, verás el siguiente mensaje:

```
                            __/___
                      _____/______|
              _______/_____\_______\_____
              \              < < <       |
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            
    BIENVENIDO A HUNDIR LA FLOTA
    ES TU TURNO
```

Luego, se te pedirá que ingreses las coordenadas para disparar. La computadora también tomará su turno automáticamente.

Cuando uno de los jugadores *[ Usuario o PC ]* tengan toda su flota destruida, el juego llegara a su final declarando al ganador y preguntara al usuario si quiere jugar otra partida

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
3. Realiza tus cambios y haz commit (git commit -am 'Añadir nueva funcionalidad').
4. Haz push a la rama (git push origin feature/nueva-funcionalidad).
5. Crea un nuevo Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.  

.
  
______________  
# ¡Gracias por jugar Hundir la Flota! Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue o contactarme.
_________________