from collections import defaultdict, deque

def part_1():
    D = open("input.txt").read().strip()
    res = 0
    for line in D.split("\n"):
        line = line[(line.find(":") + 1):].split("|")
        wins = set(line[0].split())
        mine = line[1].split()

        matches = 0
        for m in mine:
            matches += 1 if m in wins else 0
        

        res += (2 ** (matches - 1)) if matches else 0

    print(res)

def part_2():
    D = open("input.txt").read().strip()
    res = 0
    N = defaultdict(int)
    for i, line in enumerate(D.split("\n")):
        card = int(line[line.find(":") - 1])
        N[i] += 1
        line = line[(line.find(":") + 1):].split("|")
        wins = set(line[0].split())
        mine = line[1].split()

        matches = 0
        for m in mine:
            if m in wins:
                matches += 1

        for j in range(matches):
            N[i+1+j] += N[i]


    print(sum(N.values()))




    
part_2()