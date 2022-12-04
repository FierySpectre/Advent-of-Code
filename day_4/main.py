import time

def main():
    starttime = time.time()
    sum = 0
    with open("input.txt") as f:
        lines = [[[int(val) for val in pair.split('-')] for pair in line.strip().split(',')] for line in f.readlines()]
    for set in lines:
        if set[0][0] <= set[1][0] and set[0][1] >= set[1][1]:
            sum += 1
            #print(0, set)
        elif set[0][0] >= set[1][0] and set[0][1] <= set[1][1]:
            sum += 1
            #print(1, set)
    print(sum)
    endtime = time.time()
    print(endtime - starttime)

def main2():
    sum = 0
    with open("input.txt") as f:
        lines = [[[int(val) for val in pair.split('-')] for pair in line.strip().split(',')] for line in f.readlines()]
    starttime = time.time()
    for set in lines:
        done = False
        for i in range(set[0][0], set[0][1] + 1):
            if done:
                break
            for j in range(set[1][0], set[1][1] + 1):
                if i == j:
                    sum += 1
                    done = True
        """
        if set[0][0] <= set[1][0] and set[0][1] <= set[1][0]:
            sum += 1
            print(0, set)
        elif set[0][1] >= set[1][0] and set[0][1] >= set[1][1]:
            sum += 1
            print(1, set)
        """
    print(sum)
    endtime = time.time()
    print(endtime - starttime)

if __name__ == "__main__":
    main()
    main2()