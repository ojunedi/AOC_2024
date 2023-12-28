

def part1():
    RED = 12
    GREEN = 13
    BLUE = 14


    D = open("input.txt").read().strip()
    res = 0
    id = 1
    for line in D.split('\n'):
        words = line.split()
        possible = True
        for i, c in enumerate(words):
            if (c.isdigit()):
                c = int(c)
                if words[i+1].startswith('red') and c > RED:
                    possible = False
                elif words[i+1].startswith('blue') and c > BLUE:
                    possible = False
                elif words[i+1].startswith('green') and c > GREEN:
                    possible = False
        if possible:
            res += id
        id += 1

    print(res)


def part2():


    D = open("input.txt").read().strip()
    res = 0
    id = 1
    for line in D.split('\n'):
        words = line.split()
        blue_max = 0
        red_max = 0
        green_max = 0
        for i, c in enumerate(words):
            if (c.isdigit()):
                c = int(c)
                if words[i+1].startswith('red'):
                    red_max = max(red_max, c)
                elif words[i+1].startswith('blue'):
                    blue_max = max(blue_max, c)
                elif words[i+1].startswith('green'):
                    green_max = max(green_max, c)

        power = (blue_max * green_max * red_max)
        res += power

    print(res)

part1()
part2()