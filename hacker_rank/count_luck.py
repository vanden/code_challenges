# https://www.hackerrank.com/challenges/count-luck/problem

from collections import defaultdict

class Node():
    def __init__(self, row, col, celltype):
        self.row = row
        self.col = col
        if celltype == "*":
            celltype = "G"
        elif celltype == '.':
            celltype = "."
        elif celltype == "M":
            celltype = "S"
        self.celltype = celltype
        self.parent = None

    def __repr__(self):
        return "Node(row=%s, col=%s, celltype=%s)" %(self.row, self.col, self.celltype)

    def __str__(self):
        return self.celltype

class Maze():
    def __init__(self, matrix):
        self.numrows = len(matrix)
        self.numcols = len(matrix[0])
        self.cells = defaultdict(dict)
        for i, row in enumerate(matrix):
            for j, _ in enumerate(row):
                if matrix[i][j] in ".*M":
                    cell = matrix[i][j]
                    self.cells[i][j] = Node(i, j, cell)
                    if cell == 'M':
                        self.start = self.cells[i][j]
                    elif cell == "*":
                        self.goal = self.cells[i][j]

    def __str__(self):
        maze = [" "+("0123456789"*3)[:self.numcols]]

        for rowIndex in range(self.numrows):
            row = ["%s" %(rowIndex%10)]
            for colIndex in range(self.numcols):
                try:
                    cell = self[(rowIndex, colIndex)]
                    row.append(str(cell))
                except KeyError:
                    row.append("#")
            maze.append(''.join(row))
        return "\n".join(maze)

    def __getitem__(self, coords):
        row, col = coords
        return self.cells[row][col]

    def getNeighbours(self, cell):
        neighbours = []
        row, col = cell.row, cell.col
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            try:
                neighbours.append(self.cells[row+rowOffset][col+colOffset])
            except KeyError:
                pass
        return neighbours

    def solve(self):
        toExplore = [self.start]
        done = []
        while toExplore:
            current = toExplore.pop()
            if current == self.goal:
                break
            for n in self.getNeighbours(current):
                if n not in done:
                    n.parent = current
                    toExplore.append(n)
            done.append(current)
        return current == self.goal

    def getPath(self):
        path = [self.goal]
        while self.start != path[-1]:
            path.append(path[-1].parent)
            if path[-1] not in (self.start, self.goal):
                path[-1].celltype = "o"

        return reversed(path)

    def countWaves(self):
        waves = 0
        path = self.getPath()
        last = None
        for cell in path:
            if cell == self.goal:
                return waves
            choices = self.getNeighbours(cell)
            try:
                choices.remove(last)
            except ValueError:
                pass
            last = cell
            if len(choices) > 1:
                waves += 1
        return waves

def main():
    maze = Maze(['*.M', '.X.'])

    maze = Maze(['.X.X......X', '.X*.X.XXX.X', '.XX.X.XM...', '......XXXX.'])
    maze.solve()
    print(maze.countWaves())

if __name__ == "__main__":
    main()
