> 📖 🇪🇸 También disponible en español: [README.es.md](README.es.md)
# Sudoku 3x3
[![Python](https://img.shields.io/badge/code-Python-yellow.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Game](https://img.shields.io/badge/Game-puzzle-blue)]()


## Overview

**Sudoku3x3** is a simple, interactive logic game built in Python as part of my first programming course, *Pensamiento Computacional*. The project challenged me to apply core computing concepts to create a playable Sudoku puzzle, where users must complete a 9x9 board without repeating numbers in any row, column, or 3x3 box.

This version features adjustable difficulty levels and live input validation. It also demonstrates how to handle grid based constraints efficiently, all while maintaining an accessible user interface via the command line.

---

## What the Program Does

* Allows the player to choose a difficulty level: Easy, Intermediate, or Hard.
* Generates a partially filled 9x9 Sudoku board (modeled as 3x3 boxes).
* Validates that the board starts with no duplicate numbers in rows, columns, or 3x3 squares.
* Lets players fill in empty positions by selecting a box, position, and number.
* Re-validates constraints on each move; ends the game if a rule is broken.
* Displays the board in a visually segmented format for ease of use.

---

## How It Works

Behind the scenes, the game logic:

* **initializes the 9x9 grid** using a set of two dimensional lists to represent:

  * `filas` (rows)
  * `columnas` (columns)
  * `cuadrados` (3x3 subgrids)

  This structure simplifies constraint checking and board updates. 

* **Randomly generates board values** based on difficulty level, using weighted choices to determine how many cells are pre-filled.

* **Implements constraint checking logic** across all directions (rows, columns, boxes) with helper functions that detect and replace duplicates.

* **Handles user input validation** gracefully, guiding players through each step while preventing invalid actions.

---

## Concepts and Skills Demonstrated

While building this project, I gained experience with:

* **Data structure design**: Using Python lists to represent and manage structured grid data.
* **Constraint satisfaction**: Writing logic to enforce Sudoku rules using iteration and conditionals.
* **Input handling and validation**: Managing real time player input and maintaining data integrity.
* **Algorithmic thinking**: Designing board transformation functions that preserve rule consistency after each move.
* **Debugging and iteration**: Improving board generation and duplicate checking through testing and refinement.

---

## Learning Outcomes

This project directly supported my development in several key academic and professional areas:

* **Evaluating technologies to solve problems** (SEG0702): I chose core Python data structures and flow control to implement game mechanics efficiently, gaining confidence in selecting tools fit for purpose.
* **Analyzing problem components using engineering principles** (SING0301): I broke down the Sudoku rules into manageable conditions and developed code that enforces them consistently.
* **Applying professional standards to problem-solving** (SING0401): I practiced clean, modular coding and worked toward robust input validation, aiming to create a reliable, user friendly experience.

---

## Getting Started

To run the program:

1. Clone the repository.
2. Run `Sudoku.py` using any Python 3 interpreter.
3. Follow on screen instructions **in spanish** to select a difficulty and begin playing.

This is a terminal-based game, no external libraries or GUI are required.

---

## Final Thoughts

Sudoku3x3 was my first substantial programming project. It gave me a chance to see how fundamental logic and structure can turn an abstract idea into a working system. While simple, the design decisions I made reflect how I approach problems: with curiosity, analytical thinking, and a drive to build things that actually work.
