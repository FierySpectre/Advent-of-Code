def main():
    with open("input.txt") as f:
        line = ""
        stacklines = []
        while line != '\n':
            line = f.readline()
            stacklines.append(line)
        stacklines.pop()
        instructions = f.readlines()
    stackamount = len(stacklines[-1])//4
    stacklines.pop()
    stacks = [[] for i in range(stackamount)]
    for stackline in reversed(stacklines):
        for i in range(stackamount):
            obj = stackline[1 + i*4]
            if obj != ' ':
                stacks[i].append(obj)
    for instruction in instructions:
        amount, leftover = instruction[5:].split(' from')
        amount = int(amount)
        src, dest = leftover.split(' to ')
        src = int(src) - 1
        dest = int(dest) - 1
        for i in range(amount):
            stacks[dest].append(stacks[src].pop())
    print(stacks)
    for stack in stacks:
        print(stack[-1], end='')
    print()

def main2():
    with open("input.txt") as f:
        line = ""
        stacklines = []
        while line != '\n':
            line = f.readline()
            stacklines.append(line)
        stacklines.pop()
        instructions = f.readlines()
    stackamount = len(stacklines[-1])//4
    stacklines.pop()
    stacks = [[] for i in range(stackamount)]
    for stackline in reversed(stacklines):
        for i in range(stackamount):
            obj = stackline[1 + i*4]
            if obj != ' ':
                stacks[i].append(obj)
    for instruction in instructions:
        amount, leftover = instruction[5:].split(' from')
        amount = int(amount)
        src, dest = leftover.split(' to ')
        src = int(src) - 1
        dest = int(dest) - 1
        for i in range(amount):
            stacks[dest].append(stacks[src][-amount+i])
        for i in range(amount):
            stacks[src].pop()
    for stack in stacks:
        print(stack[-1], end='')

if __name__ == "__main__":
    main()
    main2()