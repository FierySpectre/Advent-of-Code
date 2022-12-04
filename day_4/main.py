import time

def main():
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

def main2():
    sum = 0
    with open("input.txt") as f:
        lines = [[[int(val) for val in pair.split('-')] for pair in line.strip().split(',')] for line in f.readlines()]
    for set in lines:
        for i in range(set[0][0], set[0][1] + 1):
            if i >= set[1][0] and i <= set[1][1]:
                sum += 1
                break
    print(sum)

if __name__ == "__main__":
    main()
    main2()