import time
import timeit

class Dir():
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.subdirs = []
        self.files = []

    def get_size(self):
        size = 0
        for file in self.files:
            size += file.size
        for subdir in self.subdirs:
            size += subdir.get_size()
        return size

    def get_solution(self):
        if(self.get_size() < 100000):
            return self.get_size() + sum([subdir.get_solution() for subdir in self.subdirs])
        else:
            return sum([subdir.get_solution() for subdir in self.subdirs])
    
    def get_solution2(self, minimum_size):
        if(self.get_size() < minimum_size):
            return None
        else:
            solutions = [subdir.get_solution2(minimum_size) for subdir in self.subdirs]
            solutions.append(self.get_size())
            solutions = list(filter(lambda val: val != None, solutions))
            #print(solutions)
            return min(solutions)
            

    def get_subdir(self, name):
        for subdir in self.subdirs:
            if subdir.name == name:
                return subdir
        return None

    def get_parent(self):
        return self.parent

    def make_subdir(self, name):
        subdir = Dir(name, self)
        self.subdirs.append(subdir)
        return subdir

    def make_file(self, name, size):
        file = File(name, size)
        self.files.append(file)
        return file

    def print(self, level=0):
        print("  " * level + self.name)
        for file in self.files:
            print("  " * (level + 1) + file.name + " " + str(file.size))
        for subdir in self.subdirs:
            subdir.print(level + 1)

class File():
    def __init__(self, name, size):
        self.name = name
        self.size = size

def main():
    with open("input.txt") as f:
        root = Dir("root")
        current_dir = None
        for line in f.readlines():
            line = line.strip()
            if line == '$ ls':
                continue
            elif line == '$ cd ..':
                current_dir = current_dir.get_parent()
            elif line == '$ cd /':
                current_dir = root
            elif line.startswith('$ cd '):
                name = line[5:]
                current_dir = current_dir.get_subdir(name)
            elif line.startswith('dir '):
                name = line[4:]
                current_dir.make_subdir(name)
            else:
                size, name = line.split(' ')
                size = int(size)
                current_dir.make_file(name, size)
    #print(root.print())
    root.get_solution()
    root.get_solution2(30000000 - (70000000 - root.get_size()))



if __name__ == "__main__":
    print(timeit.timeit(main, number=1000))
    import timeit
    print(timeit.timeit("main()", setup="from __main__ import main", number=10000))