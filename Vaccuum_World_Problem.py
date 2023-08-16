import turtle

class VacuumWorld:
    def __init__(self, grid):
        self.grid = grid
        self.position = (0, 0)   

    def move_left(self):
        self.position = (self.position[0], max(self.position[1] - 1, 0))

    def move_right(self):
        self.position = (self.position[0], min(self.position[1] + 1, len(self.grid[0]) - 1))

    def clean(self):
        self.grid[self.position[0]][self.position[1]] = "Clean"

    def draw_grid(self):
        for row in self.grid:
            for cell in row:
                if cell == "Dirty":
                    turtle.fillcolor("red")
                else:
                    turtle.fillcolor("white")
                turtle.begin_fill()
                for _ in range(4):
                    turtle.forward(50)
                    turtle.left(90)
                turtle.end_fill()
                turtle.forward(50)
            turtle.backward(50 * len(row))
            turtle.right(90)
            turtle.forward(50)
            turtle.left(90)

    def run(self):
        turtle.speed(1)
        self.draw_grid()

        while any("Dirty" in row for row in self.grid):
            if "Dirty" in self.grid[self.position[0]][self.position[1]]:
                self.clean()
            else:
                if self.position[0] % 2 == 0:
                    self.move_right()
                else:
                    self.move_left()

            turtle.clear()
            self.draw_grid()
            turtle.update()

# Example grid
grid = [
    ["Dirty", "Dirty", "Clean"],
    ["Clean", "Dirty", "Clean"],
    ["Dirty", "Clean", "Clean"]
]

turtle.setup(width=500, height=500)
turtle.title("Vaccuum World Problem")
vacuum = VacuumWorld(grid)
vacuum.run()
turtle.done()