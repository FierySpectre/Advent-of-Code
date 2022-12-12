import timeit

if __name__ == '__main__':
    print(timeit.timeit("aocday8.maincalc()", setup="import aocday8", number=100)/100)