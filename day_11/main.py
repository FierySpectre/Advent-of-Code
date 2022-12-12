import timeit
import operator
import functools
import math

class Monkey:
    def __init__(self, items, operator, relief, value, test):
        self.items = items
        if(operator == "+"):
            self.operation = lambda x: (x + int(value)) // relief
        else:
            try:
                int(value)
                self.operation = lambda x: (x * int(value)) // relief
            except ValueError:
                self.operation = lambda x: (x * x) // relief
        self.test = test
        self.inspectcount = 0
        self.truemonkey = None
        self.falsemonkey = None
        self.supermod = 0
    
    def __str__(self):
        return f"Monkey has {self.items}, inspected {self.inspectcount} items"
    
    def info(self):
        return f"Monkey({self.items}, {self.truemonkey}, {self.falsemonkey})"
    
    def play(self):
        self.inspect_items()
        self.test_items()
    
    def take_item(self, item):
        self.items.append(item)
    
    def inspect_items(self):
        for i in range(len(self.items)):
            self.inspectcount += 1
            self.items[i] = self.operation(self.items[i])
        
    def test_items(self):
        for i in range(len(self.items)):
            self.items[i] = self.items[i] % self.supermod
            if(self.items[i] % self.test):
                self.falsemonkey.take_item(self.items[i])
            else:
                self.truemonkey.take_item(self.items[i])
        self.items = []


class MonkeyBusiness:
    def __init__(self, filename:str, relief:int=3):
        self.monkeys = []
        self.relief = relief
        self.readfile(filename)
    
    def add_monkey(self, items, operator, value, test):
        self.monkeys.append(Monkey(items, operator, self.relief, value, test))

    def readfile(self, filename:str) -> list:
        with open(filename) as f:
            monkeys = [[line.strip().split() for line in block.split("\n")] for block in f.read().split("\n\n")]
        mod = 1
        for monkey in monkeys:
            items = [int(item.strip(",")) for item in monkey[1][2:]]
            operator = monkey[2][-2]
            value = monkey[2][-1]
            test = int(monkey[3][-1])
            mod *= test
            self.add_monkey(items, operator, value, test)
        for m in range(len(monkeys)):
            #print(f"Linking monkey {m}: {self.monkeys[m].info()} to {int(monkeys[m][4][-1])}: {repr(self.monkeys[int(monkeys[m][4][-1])])} and {int(monkeys[m][5][-1])}: {repr(self.monkeys[int(monkeys[m][5][-1])])}")
            self.monkeys[m].truemonkey = self.monkeys[int(monkeys[m][4][-1])]
            self.monkeys[m].falsemonkey = self.monkeys[int(monkeys[m][5][-1])]
            self.monkeys[m].supermod = mod
            
    def play(self, rounds:int=1):
        for i in range(rounds):
            for monkey in self.monkeys:
                monkey.play()
                
    def __str__(self):
        monkeys = '\n'.join([str(monkey) for monkey in self.monkeys])
        return f"MonkeyBusiness has {len(self.monkeys)} monkeys: \n{monkeys}"
    
    def get_active_monkeys(self, amount:int=1):
        return sorted([monkey.inspectcount for monkey in self.monkeys])[-amount:]
        

def main():
    solution = [0, 0]
    
    monkeys = MonkeyBusiness("input.txt")
    monkeys.play(20)
    top = monkeys.get_active_monkeys(2)
    solution[0] = top[0] * top[1]
    crazy_monkeys = MonkeyBusiness("input.txt", 1)
    crazy_monkeys.play(10000)
    top = crazy_monkeys.get_active_monkeys(2)
    solution[1] = top[0] * top[1]
    
    return solution

if __name__ == "__main__":
    print(main())
    #print(timeit.timeit(lambda: main(), number=1000))