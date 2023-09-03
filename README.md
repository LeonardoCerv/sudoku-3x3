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

Juego de Sudoku:

- SeleccionarModoDeJuego():
  - Mostrar("Elige nivel: Fácil, Intermedio o Difícil")
  - Pesos = {"Fácil": 15, "Intermedio": 10, "Difícil": 5}
  - Devolver Pesos[ObtenerEntradaUsuario()]

- VerificarDuplicadosEnLista(lista):
  - Para Cada Elemento en lista:
    - Si HayDuplicados(Elemento):
      - Mostrar("Números duplicados en la lista.")
      - Devolver Falso
  - Devolver Verdadero

- ImprimirTablero(tablero):
  - Para Cada Fila en tablero:
    - Mostrar(Fila)

- CrearTablero():
  - Peso = SeleccionarModoDeJuego()
  - GenerarTableroAleatorioConPesos(Peso)
  - Si No VerificarDuplicadosEnLista(Cuadrículas):
    - Mostrar("Tablero inicial con números duplicados.")
    - CrearTablero()
  - ActualizarTablero()

- ActualizarTablero():
  - LimpiarFilasColumnasCuadrículas()
  - LlenarFilasColumnasCuadrículasDesdeCuadrículas()
  - Si No VerificarDuplicadosEnLista(Filas) o No VerificarDuplicadosEnLista(Columnas) o No VerificarDuplicadosEnLista(Cuadrículas):
    - Mostrar("Números duplicados en el tablero.")
    - DetenerJuego()

- InicializarTableroDeSudoku()
- CrearTablero()
- ImprimirTablero(Tablero)
  
- Mientras Verdadero:
  - Mostrar("Elige cuadrícula (1-9), posición (1-9) y número (1-9)")
  - Cuadrícula, Posición, Número = ObtenerEntradaUsuario()
  - Si ValorCelda(Tablero, Cuadrícula, Posición) == 0:
    - ActualizarCelda(Tablero, Cuadrícula, Posición, Número)
    - Si ActualizarTablero():
      - ImprimirTablero(Tablero)
      - Mostrar("¡Bien hecho! Has completado el Sudoku.")
      - DetenerJuego()
  - Sino:
    - Mostrar("La casilla ya contiene un número.")

Fin del Juego de Sudoku


---------------------------------------------------------------------------------------------------------------------------------------

# Codigo

El codigo se encuentra dentro del repositorio y la version actual tiene como nombre SudokuV2.py
