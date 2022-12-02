signscores = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

battlescores = {
    "A" : {
        "X" : 3,
        "Y" : 6,
        "Z" : 0
    },
    "B" : {
        "X" : 0,
        "Y" : 3,
        "Z" : 6
    },
    "C" : {
        "X" : 6,
        "Y" : 0,
        "Z" : 3
    }
}

signscores2 = {
    "X" : 0,
    "Y" : 3,
    "Z" : 6
}

battlescores2 = {
    "A" : {
        "X" : 3,
        "Y" : 1,
        "Z" : 2
    },
    "B" : {
        "X" : 1,
        "Y" : 2,
        "Z" : 3
    },
    "C" : {
        "X" : 2,
        "Y" : 3,
        "Z" : 1
    }
}




def main():
    sum = 0
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines)
    for line in lines:
        a, b = line.split(" ")
        sum += battlescores[a][b] + signscores[b]
    print(sum)
    
def main2():
    sum = 0
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines)
    for line in lines:
        a, b = line.split(" ")
        sum += battlescores2[a][b] + signscores2[b]
    print(sum)

if __name__ == '__main__':
    main2()