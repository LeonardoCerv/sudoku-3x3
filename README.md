# Sudoku3x3

Es un juego de lógica en Python en el que los jugadores deben llenar una cuadrícula de 3x3 con números del 1 al 9, siguiendo ciertas reglas. Los números no deben repetirse en ninguna fila, columna o cuadrado, y la cuadrícula inicialmente contiene algunos números predeterminados.

Aquí está el resumen del flujo de trabajo del juego:

El jugador selecciona un modo de juego: fácil (F), intermedio (I) o difícil (D).

Se establece la cantidad de números que se muestran en la cuadrícula en función del modo seleccionado.

Se crea una cuadrícula 3x3 con algunos números iniciales y espacios vacíos.

El jugador ingresa los números en las posiciones vacías de la cuadrícula.

El programa valida si las filas y columnas cumplen con las reglas del juego: no deben haber números repetidos.

Si la cuadrícula cumple con las reglas, se muestra un mensaje de éxito. Si no cumple, se muestra un mensaje de error y el programa se detiene.


-------------------------------------------------------------------------------------------------------------------------------------

# Pseudocodigo:

1. cantidad_numeros = seleccionar_modo_de_juego()

2. INICIALIZAR cuadricula, posiciones_fila y numeros

3. MEZCLAR posiciones_fila y numeros

4. CREAR cuadricula inicial con números iniciales y espacios vacíos

5. IMPRIMIR cuadricula inicial

6. MIENTRAS entrada NO SEA "submit":
   6.1. SOLICITAR entrada AL USUARIO Y AGREGAR A respuestas_usuario

8. PARA fila EN [1, 2, 3, 4]:
   7.1. reemplazar_vacios(fila, fila - 1)
   7.2. SI NO validar(fila) ENTONCES
       7.2.1. ESCRIBIR "Error en fila", fila, ": Números repetidos"
       7.2.2. SALIR

10. PARA columna EN [1, 2, 3, 4]:
   8.1. reemplazar_vacios(columna, columna + 3)
   8.2. SI NO validar(columna) ENTONCES
       8.2.1. ESCRIBIR "Error en columna", columna, ": Números repetidos"
       8.2.2. SALIR

12. ESCRIBIR "¡Éxito! Todas las validaciones pasaron"

---------------------------------------------------------------------------------------------------------------------------------------

# Codigo

El codigo se encuentra dentro del repositorio y la version actual tiene como nombre SudokuV2.py
