def main():
    with open("input.txt") as f:
        input = f.readlines()
        stripped = []
        max = 0
        for line in input:
            stripped.append(line.strip())
        sub = 0
        for line in stripped:
            if line != "":
                sub += int(line)
            else:
                if sub > max:
                    max = sub
                sub = 0

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