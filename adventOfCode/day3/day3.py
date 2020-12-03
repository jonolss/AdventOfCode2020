def main():
    path = "inputDay3.csv"
    list = getDynamicListString(path)

    print("Part1 start")
    part1(list)
    print("Part1 end")

    print("Part2 start")
    part2(list)
    print("Part2 end")


def part1(list):
    velocityX = 3
    velocityY = 1

    maxX = len(list[0])
    maxY = len(list)
    print("maxX", maxX)
    print("maxY", maxY)

    result = runCheck(maxX, maxY, velocityX, velocityY, list)
    print("result:", result)

def part2(list):
    maxX = len(list[0])
    maxY = len(list)

    results = []
    results.append(runCheck(maxX, maxY, 1, 1, list))
    results.append(runCheck(maxX, maxY, 3, 1, list))
    results.append(runCheck(maxX, maxY, 5, 1, list))
    results.append(runCheck(maxX, maxY, 7, 1, list))
    results.append(runCheck(maxX, maxY, 1, 2, list))

    total = 1
    for result in results:
        print("result", result)
        total *= result
    print("total:", total)

def runCheck(maxX, maxY, velX, velY, list):
    numberOfTrees = 0
    x = 0
    y = 0
    while (y < maxY):
        if(list[y][x] == "#"):
            numberOfTrees += 1
        x = (x+velX) % maxX
        y = y+velY
    return numberOfTrees

def getDynamicListString(path):
    with open(path) as f:
        lines = [line.rstrip() for line in f]
        return lines

main()
