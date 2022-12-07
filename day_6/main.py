def readfile(filename):
    with open(filename, "r") as f:
        return f.readlines()

def main(sig):
    chars = []
    print(sig)
    for i in range(3):
        chars.insert(0, sig[i])
    for i in range(3, len(sig)):
        print(sig[i], chars)
        chars.insert(0, sig[i])
        for j in range(len(chars)):
            charcp = chars.copy()
            charcp.pop(j)
            if(chars[j] in charcp):
                chars.pop()
                break
        else:
            print(i+1)
            return
            
        
    

def main2(sig):
    chars = []
    print(sig)
    for i in range(13):
        chars.insert(0, sig[i])
    for i in range(13, len(sig)):
        print(sig[i], chars)
        chars.insert(0, sig[i])
        for j in range(len(chars)):
            charcp = chars.copy()
            charcp.pop(j)
            if(chars[j] in charcp):
                chars.pop()
                break
        else:
            print(i+1)
            return
        

if __name__ == "__main__":
    sig = readfile("input.txt")
    #main(sig[0])
    main2(sig[0])