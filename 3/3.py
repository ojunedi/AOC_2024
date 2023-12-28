from collections import defaultdict
D = open("input.txt").read().strip()
G = [line for line in D.split("\n")]
j = 0
ans = 0
R = len(G)
C = len(G[0])

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
gears = set()

nums = defaultdict(list)

for i in range(len(G)):
    j = 0
    while j < len(G[0]):
        # compute what the number is
        symbol_adjacent = False
        if (G[i][j].isdigit()):
            word = ""
            while (j < len(G[0]) and G[i][j].isdigit() and G[i][j] != "."):
                # explore all eight directions
                for offset in dirs:
                    dx = i + offset[0]
                    dy = j + offset[1]
                    if (dx < 0 or dy < 0 or dx >= len(G) or dy >= len(G[0])):
                        continue
                    if (G[dx][dy] != "." and not G[dx][dy].isdigit()):
                        symbol_adjacent = True

                    if G[dx][dy] == "*":
                        gears.add((dx, dy))
            
                word += G[i][j]
                j += 1
        
        if (symbol_adjacent):
            ans += int(word)
            for gear in gears:
                nums[gear].append(int(word))
            word = 0
            gears = set()

        j += 1


res = 0
for k, v in nums.items():
    if len(v) == 2:
        res += (v[0] * v[1])

print(res)


