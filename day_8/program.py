import timeit

def main():
    f = open("input.txt", 'r')
    terrain = []
    for line in f:
        row = []
        for char in line.strip():
            row.append(int(char))
        terrain.append(row)

    visibleTrees = 2*len(terrain) + 2*len(terrain[0]) - 4
    for x in range(1, len(terrain)-1, 1):
        for y in range(1, len(terrain[0])-1, 1):
            tree = terrain[x][y]
            left = terrain[x][0: y: 1]
            right = terrain[x][y+1: len(terrain[1]): 1]
            top = []
            for it in range(0, x, 1):
                top.append(terrain[it][y])
            bottom = []
            for it in range(x+1, len(terrain), 1):
                bottom.append(terrain[it][y])
            #print(x, y, tree, max(left), max(right), max(top), max(bottom))
            if (max(left) < tree or max(right) < tree or max(top) < tree or max(bottom) < tree):
                visibleTrees += 1

    bestScore = 0
    for x in range(1, len(terrain)-1, 1):
        for y in range(1, len(terrain[0])-1, 1):
            tree = terrain[x][y]
            leftScore = 1
            while(y-leftScore > 0):
                if (terrain[x][y-leftScore] < tree):
                    leftScore += 1
                else:
                    break
            rightScore = 1
            while(y+rightScore < len(terrain[0])-1):
                if (terrain[x][y+rightScore] < tree):
                    rightScore += 1
                else:
                    break
            topScore = 1
            while(x-topScore > 0):
                if (terrain[x-topScore][y] < tree):
                    topScore += 1
                else:
                    break
            bottomScore = 1
            while(x+bottomScore < len(terrain)-1):
                if (terrain[x+bottomScore][y] < tree):
                    bottomScore += 1
                else:
                    break
            
            if (bestScore < leftScore*rightScore*topScore*bottomScore):
                bestScore = leftScore*rightScore*topScore*bottomScore
                #print(leftScore, rightScore, topScore, bottomScore)

    #print(visibleTrees, bestScore)
    f.close()

if __name__ == "__main__":
    print(timeit.timeit(main, number=100)/100)