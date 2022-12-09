def main():
    with open("input.txt") as f:
        elves = [[int(val) for val in elf.split("\n")] for elf in f.read().strip().split("\n\n")]
        max = 0
        for elf in elves:
            if sum(elf) > max:
                max = sum(elf)
    print(max)

def main2():
    with open("input.txt") as f:
        input = f.readlines()
        stripped = []
        maxes = [0, 0, 0]
        for line in input:
            stripped.append(line.strip())
        sub = 0
        for line in stripped:
            if line != "":
                sub += int(line)
            else:
                for i in range(len(maxes)):
                    if maxes[i] < sub:
                        maxes[i] = sub
                        break
                sub = 0
                        

    print(sum(maxes))

if __name__ == "__main__":
    main()