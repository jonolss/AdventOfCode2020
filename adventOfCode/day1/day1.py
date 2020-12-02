def main():
    print("HEJ")
    path = "inputDay1.csv"
    list = getDynamicList(path)
    sortedList = sortList(list)

    print("Part1 start")
    part1(sortedList)
    print("Part1 end")

    print("Part2 start")
    part2(list)
    print("Part2 end")

def part2(list):
    list.sort()
    ind1 = 0
    ind2 = 1
    ind3 = len(list)-1
    result = -1
    while (ind2 != ind3 and result == -1):
        val1 = list[ind1]
        val2 = list[ind2]
        val3 = list[ind3]
        result = checkSumIs2020AndReturnMul3(val1, val2, val3)
        if(val1+val2+val3 > 2020):
            ind3 -= 1
        else:
            ind1 += 1
        if(ind1 == ind2):
            ind1 = 0
            ind2 += 1
    print(result)

def part1(list):
    ind1 = 0
    ind2 = len(list)-1
    result = -1
    while (ind1 != ind2 and result == -1):
        val1 = list[ind1]
        val2 = list[ind2]
        result = checkSumIs2020AndReturnMul(val1, val2)
        if(determineWhichToMove(val1, val2)):
            ind1 += 1
        else:
            ind2 -= 1
    print(result)

def determineWhichToMove(val1, val2):
    if(val1+val2 > 2020):
        return True
    return False

def sortList(list):
    sortedList = list
    sortedList.sort(reverse=True)
    return sortedList

def getDynamicList(path):
    stringList = getDynamicListString(path)
    numList = []
    for str in stringList:
        numList.append(int(str))
    return numList

def getDynamicListString(path):
    with open(path) as f:
        lines = [line.rstrip() for line in f]
        return lines

def getList(path):
    list = [1721,979,366,299,675,1456]
    return list

def checkSumIs2020AndReturnMul(val1, val2):
    if(val1 + val2 == 2020):
        return val1 * val2
    return -1

def checkSumIs2020AndReturnMul3(val1, val2, val3):
    if(val1 + val2 + val3 == 2020):
        return val1 * val2 * val3
    return -1

main()
