import random

# Función para seleccionar el modo de juego
def seleccionar_modo_de_juego():
    print("Escoge el modo de juego: (F)ácil  (I)ntermedio  (D)ifícil")
    modo_seleccionado = str(input())

    # Configuración de peso según el modo seleccionado
    if modo_seleccionado.lower() == "d":
        peso = 5
    elif modo_seleccionado.lower() == "i":
        peso = 10
    elif modo_seleccionado.lower() == "f":
        peso = 15
    return peso

# Función para verificar duplicados en una lista
def verificar_lista(lista, reemplazar):
    for i in range(9):
        for j in range(1, 10):
            if lista[i].count(j) > 1:
                if reemplazar:
                    num = lista[i].index(j)
                    lista[i].remove(j)
                    lista[i].insert(num, 0)
                else:
                    num = lista[i].index(j)
                    print(num, i, j)
                    return False
    return True

# Función para imprimir el tablero del Sudoku
def imprimir_tablero():
    for i in range(9):
        if i == 3 or i == 6:
            print("\033[1;34m ——————————————————|————————————————————|———————————————————")
        for j in range(9):
            if j == 3 or j == 6:
                print("\033[1;34m | ", end="")
            if j == 8:
                print("\033[1;37m", "[", end="")
                if columnas[j][i] != 0:
                    print("\033[1;33m", columnas[j][i], end="")
                    print("\033[1;37m", "]")
                else:
                    print("\033[1;37m", columnas[j][i], "]")
            else:
                print("\033[1;37m", "[", end="")
                if columnas[j][i] != 0:
                    print("\033[1;33m", columnas[j][i], end="")
                    print("\033[1;37m", "]", end="")
                else:
                    print("\033[1;37m", columnas[j][i], "]", end="")

# Función para crear el tablero de Sudoku
def crear_tablero():
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    peso = seleccionar_modo_de_juego()
    
    # Generar números aleatorios para el tablero
    numeros = random.choices(lista, weights=(100, peso, peso, peso, peso, peso, peso, peso, peso, peso), k=81)

    # Llenar el tablero de cuadrados
    for i in range(9):
        for j in range(9):
            cuadrados[i].insert(j, (numeros[(j + (6 * (j // 3)) + (i * 3 + (i // 3 * 18)))]))
    
    # Verificar duplicados en el tablero
    verificar_lista(cuadrados, True)
    verificar_lista(cuadrados, True)
    
    # Actualizar el tablero
    actualizar_tablero(True)

# Función para actualizar el tablero
def actualizar_tablero(reemplazar):
    for i in range(9):
        filas[i].clear()
        for j in range(9):
            filas[i].insert(j, (cuadrados[(j // 3) + (3 * (i // 3))][(3 * (i) - 3 * ((i // 3) * 3)) + (j - ((j // 3) * 3))]))
    
    # Verificar duplicados en las filas
    if not verificar_lista(filas, reemplazar):
        return False

    for i in range(9):
        columnas[i].clear()
        for j in range(9):
            columnas[i].insert(j, (filas[j][i]))
    
    # Verificar duplicados en las columnas
    if not verificar_lista(columnas, reemplazar):
        return False

    for i in range(9):
        cuadrados[i].clear()
        for j in range(9):
            cuadrados[i].insert(j, (columnas[(3 * (i) - 3 * ((i // 3) * 3)) + (j - ((j // 3) * 3))][(j // 3) + (3 * (i // 3))]))
    
    # Verificar duplicados en los cuadrados
    if not verificar_lista(cuadrados, reemplazar):
        return False

    return True

# Inicializar listas para filas, columnas y cuadrados
filas = [[], [], [], [], [], [], [], [], []]
columnas = [[], [], [], [], [], [], [], [], []]
cuadrados = [[], [], [], [], [], [], [], [], []]

# Crear el tablero inicial
crear_tablero()
imprimir_tablero()

# Iniciar el juego
while True:
    print("Elige el cuadro (1-9)")
    cuadro = int(input()) - 1

    print("Elige la posición (1-9)")
    pos = int(input()) - 1

    print("Ahora introduce el número que irá en esa posición")
    numero = int(input())

    auxiliar = int(cuadrados[cuadro][pos])

    if auxiliar == 0:
        cuadrados[cuadro].pop(pos)
        cuadrados[cuadro].insert(pos, numero)
        if actualizar_tablero(False):
            imprimir_tablero()
            print("¡Bien hecho!")
        else:
            imprimir_tablero()
            print("¡Has perdido!")
            exit()
    else:
        print("No puedes hacer eso")
