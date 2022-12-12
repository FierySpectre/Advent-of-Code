import timeit
import numpy as np

class RopeGrid:
    def __init__(self, expandamount=1, knots=2):
        self.width = 1
        self.height = 1
        self.expandamount = expandamount
        self.knots = [[0, 0] for _ in range(knots)]
        self.grid = np.ones((1, 1), dtype=int)

    def __str__(self):
        return "\n".join(["".join([str(x) for x in row]) for row in self.grid])

    def __getitem__(self, key):
        return self.grid[key]

    def __setitem__(self, key, value):
        self.grid[key] = value

    def __len__(self):
        return len(self.grid)

    def __iter__(self):
        return iter(self.grid)

    def __next__(self):
        return next(self.grid)

    def __repr__(self):
        return f"RopeGrid({self.width}, {self.height})"
    
    def __int__(self):
        return int(np.sum(self.grid))
    
    def sum(self):
        return int(np.sum(self.grid))
    
    def count(self):
        return int(np.count_nonzero(self.grid))
    
    def expand(self, direction:str) -> None:
        if(direction == "U"):
            temp = np.zeros((self.height + self.expandamount, self.width), dtype=int)
            temp[self.expandamount:, :] = self.grid
            self.grid = temp
            self.knots = [[knot[0], knot[1] + self.expandamount] for knot in self.knots]
            self.height += self.expandamount
        elif(direction == "D"):
            temp = np.zeros((self.height + self.expandamount, self.width), dtype=int)
            temp[:-self.expandamount, :] = self.grid
            self.grid = temp
            self.height += self.expandamount
        elif(direction == "L"):
            temp = np.zeros((self.height, self.width + self.expandamount), dtype=int)
            temp[:, self.expandamount:] = self.grid
            self.grid = temp
            self.knots = [[knot[0] + self.expandamount, knot[1]] for knot in self.knots]
            self.width += self.expandamount
        elif(direction == "R"):
            temp = np.zeros((self.height, self.width + self.expandamount), dtype=int)
            temp[:, :-self.expandamount] = self.grid
            self.grid = temp
            self.width += self.expandamount
    
    def step(self, direction:str, knot:int=0) -> None:
        if(knot == 0):
            if(direction == "U"):
                self.knots[knot][1] -= 1
            elif(direction == "D"):
                self.knots[knot][1] += 1
            elif(direction == "L"):
                self.knots[knot][0] -= 1
            elif(direction == "R"):
                self.knots[knot][0] += 1
            if(self.knots[knot][1] < 0 or self.knots[knot][1] >= self.height or self.knots[knot][0] < 0 or self.knots[knot][0] >= self.width):
                self.expand(direction)
            self.step(direction, knot+1)
        elif(knot == len(self.knots)):
            self.grid[self.knots[-1][1], self.knots[-1][0]] = 1
        else:
            if(abs(self.knots[knot][0] - self.knots[knot-1][0]) > 1):
                self.knots[knot][0] += 1 if self.knots[knot][0] < self.knots[knot-1][0] else -1
                if(self.knots[knot][1] != self.knots[knot-1][1]):
                    self.knots[knot][1] += 1 if self.knots[knot][1] < self.knots[knot-1][1] else -1
                self.step("U" if self.knots[knot][1] < self.knots[knot-1][1] else "D", knot+1)
            elif(abs(self.knots[knot][1] - self.knots[knot-1][1]) > 1):
                self.knots[knot][1] += 1 if self.knots[knot][1] < self.knots[knot-1][1] else -1
                if(self.knots[knot][0] != self.knots[knot-1][0]):
                    self.knots[knot][0] += 1 if self.knots[knot][0] < self.knots[knot-1][0] else -1
                self.step("L" if self.knots[knot][0] < self.knots[knot-1][0] else "R", knot+1)
        
        
        
    def move(self, direction:str, distance:int):
        for _ in range(distance):
            self.step(direction)
    
        
def readfile(filename:str) -> list:
    with open(filename) as f:
        moves = [line.strip().split() for line in f.readlines()]
        directions = [move[0] for move in moves]
        distances = [int(move[1]) for move in moves]
        moves = list(zip(directions, distances))
    return moves

def main():
    solution = [0, 0]
    moves = readfile("input.txt")
    grid = RopeGrid(expandamount=50)
    for direction, distance in moves:
        grid.move(direction, distance)
    solution[0] = grid.count()
    grid = RopeGrid(expandamount=50, knots=10)
    for direction, distance in moves:
        grid.move(direction, distance)
    solution[1] = grid.count()
    return solution

if __name__ == "__main__":
    print(timeit.timeit(lambda: main(), number=1000))