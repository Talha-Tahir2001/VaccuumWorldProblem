# Vacuum World Problem with Turtle Graphics

This repository contains a Python implementation of the "Vacuum World" problem using the Turtle graphics library for visualisation. The code simulates the behaviour of a vacuum cleaner agent moving through a grid, cleaning dirty cells and leaving clean cells untouched.

## Overview

The "Vacuum World" problem involves a simple agent (vacuum cleaner) moving through a grid of cells. The goal is to clean all the dirty cells in the grid using predefined movement patterns.

## Implementation Details

- The implementation uses the `VacuumWorld` class to define the behavior of the vacuum cleaner.
- The vacuum cleaner can move left or right within the grid using the `move_left` and `move_right` methods.
- The `clean` method marks dirty cells as "Clean" when the vacuum cleaner encounters them.
- The `draw_grid` method visualizes the grid using Turtle graphics, with dirty cells displayed in red and clean cells in white.
- The `run` method executes the vacuum cleaner's movement logic until all dirty cells are cleaned.
- The example `grid` provided demonstrates the functionality of the code.
- The Turtle graphics environment is set up with a window of size 500x500.

## Usage

1. Ensure you have Python 3.11 installed.
2. Clone this repository: `git clone https://github.com/Talha-Tahir2001/VacuumWorldProblem.git`
3. Navigate to the repository: `cd VacuumWorldProblem`
4. Run the script: `python vacuum_world.py`

## Example Grid

The example `grid` in the code represents the layout of cells in the vacuum world. You can modify this grid to create different scenarios for the vacuum cleaner.

## Note

This implementation focuses on simulating the vacuum cleaner's movement and visualisation using Turtle graphics. It doesn't involve search algorithms like BFS or DFS.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute by adding improvements or extending the implementation.

For questions or suggestions, please open an issue.




