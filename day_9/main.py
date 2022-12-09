import time
import timeit

def main():
    with open("test.txt") as f:
        moves = [line.strip().split() for line in f.readlines()]
        directions = [move[0] for move in moves]
        distances = [int(move[1]) for move in moves]
        moves = list(zip(directions, distances))
    print(moves)
                


if __name__ == "__main__":
    main()