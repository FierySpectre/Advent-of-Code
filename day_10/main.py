import timeit
import operator
import functools
        
def readfile(filename:str) -> list:
    with open(filename) as f:
        lines = [line.strip().split() for line in f.readlines()]
        lines = functools.reduce(operator.iconcat, lines, [])
    return lines

def main():
    solution = [0, 0]
    pc = 1
    x = 1
    total = 0
    crt = [['' for _ in range(40)] for _ in range(6)]
    for line in readfile("input.txt"):
        if(pc % 40 == 20):
            total += x * pc
            #print(f"{pc}: {x} * {pc} = {x * pc}")
            #print()
        if(pc % 40 == 0):
            print()
        print(f"{pc%40} in {list(range(x-1, x+2))}(x={x})")
        try:
            #print(f"{pc}: {x} + {int(line)} = {x + int(line)}")
            x += int(line)
        except ValueError:
            pass
            #print(line)
        
        crt[(pc-1)//40][(pc)%40] = '#' if pc%40 in range(x-1, x+2) else '.'
        pc += 1
        
    solution[0] = total
    solution[1] = crt
    for line in crt:
        print(''.join(line))
        
    return solution
            
            

if __name__ == "__main__":
    print(main())
    #print(timeit.timeit(lambda: main(), number=1000))