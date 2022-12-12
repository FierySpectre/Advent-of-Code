import time
import timeit

def maincalc():
    with open("input.txt") as f:
        trees = [[[int(char), False] for char in line.strip()] for line in f.readlines()]
    cdef int visibles = 0
    for i in range(len(trees)):
        up = -1
        down = -1
        left = -1
        right = -1
        for j in range(len(trees[i])):
            if(trees[i][j][0] > right):
                right = trees[i][j][0]
                if(not trees[i][j][1]):
                    trees[i][j][1] = True
                    visibles += 1
            if(trees[i][len(trees) - 1 - j][0] > left):
                left = trees[i][len(trees) - 1 - j][0]
                if(not trees[i][len(trees) - 1 - j][1]):
                    trees[i][len(trees) - 1 - j][1] = True
                    visibles += 1
            if(trees[j][i][0] > down):
                down = trees[j][i][0]
                if(not trees[j][i][1]):
                    trees[j][i][1] = True
                    visibles += 1
            if(trees[len(trees) - 1 - j][i][0] > up):
                up = trees[len(trees) - 1 - j][i][0]
                if(not trees[len(trees) - 1 - j][i][1]):
                    trees[len(trees) - 1 - j][i][1] = True
                    visibles += 1
    #print(visibles)
    max = 0
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            left = 1
            right = 1
            up = 1
            down = 1
            # view distance left:
            for k in range(1, j + 1):
                left = k
                if(trees[i][j - k][0] >= trees[i][j][0]):
                    break
            else:
                left = j

            # view distance right:
            for k in range(1, len(trees[i]) - j):
                right = k
                if(trees[i][j + k][0] >= trees[i][j][0]):
                    break
            else:
                right = len(trees[i]) - j - 1

            # view distance up:
            for k in range(1, i + 1):
                up = k
                if(trees[i - k][j][0] >= trees[i][j][0]):
                    break
            else:
                up = i

            # view distance down:
            for k in range(1, len(trees) - i):
                down = k
                if(trees[i + k][j][0] >= trees[i][j][0]):
                    break
            else:
                down = len(trees) - i - 1

            left = left if left > 0 else 1
            right = right if right > 0 else 1
            up = up if up > 0 else 1
            down = down if down > 0 else 1
            tot = left * right * up * down
            max = tot if tot > max else max
    #print(max)
                