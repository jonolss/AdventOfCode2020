def main():
    path = "inputDay2.csv"
    list = getDynamicList(path)

    print("Part1 start")
    part1(list)
    print("Part1 end")

    print("Part2 start")
    part2(list)
    print("Part2 end")


def part1(list):
    numberOfValidRules = 0
    for pwAndRule in list:
        if(pwAndRule.calculateRule1()):
            numberOfValidRules += 1
    print("result:", numberOfValidRules)

def part2(list):
    numberOfValidRules = 0
    for pwAndRule in list:
        if(pwAndRule.calculateRule2()):
            numberOfValidRules += 1
    print("result:", numberOfValidRules)

class PasswordAndRule:
  def __init__(self, policyChar, policyLow, policyHigh, password):
    self.policyChar = policyChar
    self.policyLow = int(policyLow)
    self.policyHigh = int(policyHigh)
    self.password = password

  def calculateRule1(self):
      numOfPolcyChar = self.password.count(self.policyChar)
      if(numOfPolcyChar < self.policyLow or numOfPolcyChar > self.policyHigh):
        return False
      return True

  def calculateRule2(self):
      location1 = self.policyLow-1
      location2 = self.policyHigh-1
      charAtLocation1 = self.password[location1:location1+1]
      charAtLocation2 = self.password[location2:location2+1]

      print("location1:", location1)
      print("location2:", location2)
      print("charAtLocation1:", charAtLocation1)
      print("charAtLocation2:", charAtLocation2)
      print("self.policyChar:", self.policyChar)

      if(charAtLocation1 != charAtLocation2):
          if(charAtLocation1 == self.policyChar or charAtLocation2 == self.policyChar):
              return True
      return False

def getDynamicList(path):
    stringList = getDynamicListString(path)
    pwarList = []
    temp = True
    for str in stringList:
        minusLocation = str.find("-")
        low = str[:minusLocation]
        spaceBetweenHighAndChar = str.find(" ")
        high = str[minusLocation+1:spaceBetweenHighAndChar]
        colonLocation = str.find(":")
        char = str[colonLocation-1:colonLocation]
        password = str[colonLocation+2:]
        if(temp):
            temp = False
            print("low", low)
            print("high", high)
            print("char", char)
            print("password", password)
        pwarList.append(PasswordAndRule(char, low, high, password))
    return pwarList

def getDynamicListString(path):
    with open(path) as f:
        lines = [line.rstrip() for line in f]
        return lines

main()
