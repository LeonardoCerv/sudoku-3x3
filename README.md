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

Inicio del Juego de Sudoku:

  Función SeleccionarModoDeJuego():
    Mostrar("Selecciona el nivel: Fácil, Intermedio o Difícil")
    Modo = ObtenerEntradaUsuario()
    Pesos = {"Fácil": 15, "Intermedio": 10, "Difícil": 5}
    Devolver Pesos[Modo]

  Función VerificarDuplicadosEnLista(lista):
    Para Cada Elemento en lista Hacer
      Si HayDuplicados(Elemento) entonces
        Mostrar("Hay números duplicados en la lista.")
        Devolver Falso
      Fin Si
    Fin Para
    Devolver Verdadero

  Función ImprimirTablero(tablero):
    Para Cada Fila en tablero Hacer
      Mostrar(Fila)
    Fin Para

  Función CrearTablero():
    Peso = SeleccionarModoDeJuego()
    GenerarTableroAleatorioConPesos(Peso)
    Si No VerificarDuplicadosEnLista(Cuadrículas) entonces
      Mostrar("El tablero inicial tiene números duplicados.")
      CrearTablero()
    Fin Si
    ActualizarTablero()

  Función ActualizarTablero():
    LimpiarFilasColumnasCuadrículas()
    LlenarFilasColumnasCuadrículasDesdeCuadrículas()
    Si No VerificarDuplicadosEnLista(Filas) o No VerificarDuplicadosEnLista(Columnas) o No VerificarDuplicadosEnLista(Cuadrículas) entonces
      Mostrar("Hay números duplicados en el tablero.")
      DetenerJuego()
    Fin Si

  InicializarTableroDeSudoku()
  CrearTablero()
  ImprimirTablero(Tablero)
  
  Mientras Verdadero:
    Mostrar("Elige cuadrícula (1-9), posición (1-9) y número (1-9)")
    Cuadrícula, Posición, Número = ObtenerEntradaUsuario()
    Si ValorCelda(Tablero, Cuadrícula, Posición) == 0 entonces
      ActualizarCelda(Tablero, Cuadrícula, Posición, Número)
      Si ActualizarTablero() entonces
        ImprimirTablero(Tablero)
        Mostrar("¡Bien hecho! Has completado el Sudoku.")
        DetenerJuego()
      Fin Si
    Sino
      Mostrar("La casilla ya contiene un número.")
    Fin Si

Fin del Juego de Sudoku


---------------------------------------------------------------------------------------------------------------------------------------

# Codigo

El codigo se encuentra dentro del repositorio y la version actual tiene como nombre SudokuV2.py
