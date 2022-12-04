def get_priority(char):
    if(char.isupper()):
        return ord(char) - 38
    else:
        return ord(char) - 96

def main():
    sum = 0
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    for line in lines:
        lenght = len(line) / 2
        first = line[:int(lenght)]
        second = line[int(lenght):]
        for char in first:
            if(char in second):
                sum += get_priority(char)
                break
    print(sum)

def main2():
    sum = 0
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    for line in lines[::3]:
        for char in line:
            if(char in lines[lines.index(line) + 1] and char in lines[lines.index(line) + 2]):
                sum += get_priority(char)
                break
    print(sum)

if __name__ == "__main__":
    main()
    main2()