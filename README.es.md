# Sudoku 3x3 – Juego de Lógica en Python
[![Python](https://img.shields.io/badge/code-Python-yellow.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Juego](https://img.shields.io/badge/Juego-puzzle-blue)]()

## Descripción General

**Sudoku3x3** es un juego de lógica interactivo y sencillo, desarrollado en Python como parte de mi primer curso de programación, *Pensamiento Computacional*. El proyecto me desafió a aplicar conceptos fundamentales de la computación para crear un Sudoku jugable, donde el usuario debe completar un tablero de 9x9 sin repetir números en ninguna fila, columna o subcuadro de 3x3.

Esta versión incluye niveles de dificultad ajustables y validación de entradas en tiempo real. También demuestra cómo manejar restricciones basadas en cuadrículas de forma eficiente, todo a través de una interfaz accesible desde la línea de comandos.

---

## Qué Hace el Programa

* Permite al jugador elegir un nivel de dificultad: Fácil, Intermedio o Difícil.
* Genera un tablero de Sudoku parcialmente lleno (modelado como subcuadros de 3x3).
* Valida que el tablero inicial no tenga números duplicados en filas, columnas o subcuadros.
* Permite al jugador rellenar posiciones vacías eligiendo un subcuadro, una posición y un número.
* Revalida las restricciones en cada jugada; termina el juego si se rompe alguna regla.
* Muestra el tablero de forma segmentada visualmente para mayor claridad.

---

## Cómo Funciona

Detrás de escena, la lógica del juego:

* **Inicializa la cuadrícula 9x9** usando listas bidimensionales para representar:

  * `filas`
  * `columnas`
  * `cuadrados` (subcuadros de 3x3)

  Esta estructura simplifica la validación de restricciones y las actualizaciones del tablero.

* **Genera valores aleatorios en el tablero** según el nivel de dificultad, utilizando pesos para determinar cuántas celdas se llenan previamente.

* **Implementa lógica de verificación de restricciones** en todas las direcciones (filas, columnas y subcuadros) con funciones auxiliares que detectan y corrigen duplicados.

* **Maneja la validación de entradas del usuario** de forma clara, guiando al jugador paso a paso y previniendo acciones no válidas.

---

## Conceptos y Habilidades Demostradas

Durante el desarrollo de este proyecto, adquirí experiencia en:

* **Diseño de estructuras de datos**: Uso de listas en Python para representar y gestionar datos estructurados en cuadrículas.
* **Satisfacción de restricciones**: Escritura de lógica para aplicar las reglas del Sudoku mediante iteraciones y condicionales.
* **Manejo y validación de entradas**: Procesamiento de la entrada del jugador en tiempo real manteniendo la integridad de los datos.
* **Pensamiento algorítmico**: Diseño de funciones que transforman el tablero manteniendo las reglas del juego después de cada jugada.
* **Depuración e iteración**: Mejora del generador de tableros y del sistema de verificación mediante pruebas y ajustes.

---

## Resultados de Aprendizaje

Este proyecto apoyó directamente mi desarrollo en varias áreas clave, tanto académicas como profesionales:

* **Evaluar tecnologías para resolver problemas** (SEG0702): Elegí estructuras de datos y control de flujo en Python para implementar la lógica del juego de forma eficiente, ganando confianza al seleccionar herramientas adecuadas.
* **Analizar componentes de un problema usando principios de ingeniería** (SING0301): Descompuse las reglas del Sudoku en condiciones manejables y desarrollé código para aplicarlas de manera consistente.
* **Aplicar estándares profesionales en la solución de problemas** (SING0401): Practiqué una codificación limpia y modular, trabajando hacia una validación robusta de entradas con el objetivo de crear una experiencia confiable y amigable para el usuario.

---

## Cómo Empezar

Para ejecutar el programa:

1. Clona este repositorio.
2. Ejecuta `Sudoku.py` usando cualquier intérprete de Python 3.
3. Sigue las instrucciones en pantalla para elegir la dificultad y comenzar a jugar.

Este es un juego basado en terminal; no requiere bibliotecas externas ni interfaz gráfica.

---

## Reflexión Final

Sudoku3x3 fue mi primer proyecto de programación sustancial. Me permitió experimentar cómo la lógica y la estructura fundamentales pueden convertir una idea abstracta en un sistema funcional. Aunque sencillo, las decisiones de diseño que tomé reflejan mi forma de abordar problemas: con curiosidad, pensamiento analítico y el deseo de construir cosas que realmente funcionen.
