import random

# Solicitar al usuario que elija el modo de juego
print("Escoge el modo de juego: (F)ácil  (I)ntermedio  (D)ifícil")
modo_seleccionado = str(input())

# Determinar la cantidad de números que se mostrarán en la cuadrícula según el modo
if modo_seleccionado == "d" or modo_seleccionado == "D":
    cantidad_numeros_mostrados = int(2)
elif modo_seleccionado == "i" or modo_seleccionado == "I":
    cantidad_numeros_mostrados = int(3)
elif modo_seleccionado == "f" or modo_seleccionado == "F":
    cantidad_numeros_mostrados = int(4)

cuadricula = []  # Lista para almacenar los números en la cuadrícula
posiciones_fila = []  # Lista para almacenar las posiciones de fila
for i in range(4):
    posiciones_fila.append(i)
random.shuffle(posiciones_fila)  # Mezclar las posiciones de fila

numeros = []  # Lista para almacenar números del 1 al 4
for i in range(1, 5):
    numeros.append(i)
random.shuffle(numeros)  # Mezclar los números

# Crear la cuadrícula con los números iniciales y espacios vacíos
for i in range(5 - cantidad_numeros_mostrados):
    if i == 0:
        for i in range(cantidad_numeros_mostrados):
            posicion = posiciones_fila[i]
            numero = numeros[i]

            for i in range(posicion):
                cuadricula.append(0)  # Agregar ceros antes del número
            cuadricula.append(numero)  # Agregar el número
            for i in range(3 - posicion):
                cuadricula.append(0)  # Agregar ceros después del número
    else:
        for i in range(4):
            cuadricula.append(0)  # Agregar ceros para filas vacías

# Imprimir la cuadrícula inicial
for i in range(4):
    if i == 2:
        print("———————+———————")
    fila = []
    fila.append("[")
    fila.append(cuadricula[0 + (i * 4)])
    fila.append("][")
    fila.append(cuadricula[1 + (i * 4)])
    fila.append("] | [")
    fila.append(cuadricula[2 + (i * 4)])
    fila.append("][")
    fila.append(cuadricula[3 + (i * 4)])
    fila.append("]")
    for i in range(9):
        print(fila[i], end="")
    print("")

respuestas_usuario = []  # Lista para almacenar las respuestas del usuario
entrada = "0"
while entrada != "submit":
    entrada = str(input())
    if entrada != "submit":
        respuestas_usuario.append(int(entrada))

# Función para obtener las filas de la cuadrícula
def obtener_fila(cual_fila):
    fila_obtenida = []
    for i in range(4):
        fila_obtenida.append(cuadricula[i + (4 * cual_fila)])
    return fila_obtenida

# Obtener las filas originales
fila1 = obtener_fila(0)
fila2 = obtener_fila(1)
fila3 = obtener_fila(2)
fila4 = obtener_fila(3)

contador = 0

# Función para reemplazar los espacios vacíos con los números del usuario
def reemplazar_vacios(fila, contador):
    contador_filas = int(contador)
    for i in range(4):
        if fila[i] == 0:
            fila.pop(i)
            fila.insert(i, respuestas_usuario[contador_filas])
            contador_filas = contador_filas + 1
    return fila

# Llenar las filas con los números del usuario
reemplazar_vacios(fila1, contador)
contador += 3
reemplazar_vacios(fila2, contador)
contador += 3
reemplazar_vacios(fila3, contador)
if cantidad_numeros_mostrados == 2:
    contador += 4
else:
    contador += 3
reemplazar_vacios(fila4, contador)

# Función para obtener las columnas de la cuadrícula
def obtener_columna(numero_columna):
    columna = []
    columna.append(fila1[numero_columna])
    columna.append(fila2[numero_columna])
    columna.append(fila3[numero_columna])
    columna.append(fila4[numero_columna])
    return columna

# Obtener las columnas
columna1 = obtener_columna(0)
columna2 = obtener_columna(1)
columna3 = obtener_columna(2)
columna4 = obtener_columna(3)

# Función para validar si no hay números repetidos en una fila o columna
def validar(array):
    for i in range(1, 5):
        cantidad_repeticiones = int(array.count(i))
        if cantidad_repeticiones != 1:
            print("TU RESPUESTA ES ERRÓNEA")  # Mostrar mensaje de error
            return False
    return True

# Validar filas y columnas
if not validar(fila1) or not validar(fila2) or not validar(fila3) or not validar(fila4):
    exit()

if not validar(columna1) or not validar(columna2) or not validar(columna3) or not validar(columna4):
    exit()

print("¡Tu respuesta es correcta!")  # Imprimir mensaje de éxito
