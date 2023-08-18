# Sudoku4x4

Es un juego de lógica en Python en el que los jugadores deben llenar una cuadrícula de 4x4 con números del 1 al 4, siguiendo ciertas reglas. Los números no deben repetirse en ninguna fila ni columna, y la cuadrícula inicialmente contiene algunos números predeterminados.

Aquí está el resumen del flujo de trabajo del juego:

El jugador selecciona un modo de juego: fácil (F), intermedio (I) o difícil (D).

Se establece la cantidad de números que se muestran en la cuadrícula en función del modo seleccionado.

Se crea una cuadrícula 4x4 con algunos números iniciales y espacios vacíos.

El jugador ingresa los números en las posiciones vacías de la cuadrícula.

El programa valida si las filas y columnas cumplen con las reglas del juego: no deben haber números repetidos.

Si la cuadrícula cumple con las reglas, se muestra un mensaje de éxito. Si no cumple, se muestra un mensaje de error y el programa se detiene.


-------------------------------------------------------------------------------------------------------------------------------------

# Pseudocodigo:

1. Solicitar al usuario que elija el modo de juego
2. Determinar la cantidad de números que se mostrarán en la cuadrícula según el modo
3. Inicializar cuadricula, posiciones_fila y numeros
4. Mezclar posiciones_fila y numeros
5. Crear la cuadrícula inicial con números iniciales y espacios vacíos
6. Imprimir la cuadrícula inicial
7. Inicializar respuestas_usuario y entrada
8. Mientras entrada no sea "submit":
   1. Solicitar entrada al usuario y agregar a respuestas_usuario
9. Definir función obtener_fila(cual_fila) que retorna una fila de la cuadrícula
10. Obtener filas originales (fila1, fila2, fila3, fila4)
11. Definir función reemplazar_vacios(fila, contador) que llena espacios vacíos con respuestas_usuario
12. Llenar las filas con los números del usuario usando reemplazar_vacios
13. Obtener columnas originales (columna1, columna2, columna3, columna4)
14. Definir función validar(array) que verifica si no hay números repetidos en el array
15. Validar filas usando validar y si no son válidas, mostrar mensaje de error y salir
16. Validar columnas usando validar y si no son válidas, mostrar mensaje de error y salir
17. Imprimir mensaje de éxito si todas las validaciones pasan

---------------------------------------------------------------------------------------------------------------------------------------

# Codigo

El codigo se encuentra dentro del repositorio y la version actual tiene como nombre Sudoku.py
