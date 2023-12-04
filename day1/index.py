import re
input = open("input.txt", "r")

## regex doesn't easily handle overlapping matches
##took about 4 hours. Spent too long trying to start with optimal regex solution. only took ~60 minutes considering current solution
numberDict = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}

# oneight
# two
# threight
# four
# fiveight
# six
# sevenine
# eighthree
# eightwo
# nineight

total = 0
i = 0
for x in input:
  i+=1
#   if i < 4:
#     continue

#   x = "oneighteight"
  string = x
#   for key in numberDict:
#     numberList = re.split(rf"({key})", x)
#     for item in numberList:
#       if item
#     print(thing)

  string = re.sub('oneight','18', string)
  string = re.sub('twone','21', string)
#   string = re.sub('threeight','38', string)
#   string = re.sub('fiveight','58', string)
#   string = re.sub('sevenine','79', string)
#   string = re.sub('eighthree','83', string)
  string = re.sub('eightwo','82', string)
#   string = re.sub('nineight','98', string)

  numbers = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', string)
  first = numberDict[numbers[0]] if numbers[0] in numberDict else numbers[0]
  last = numberDict[numbers[-1]] if numbers[-1] in numberDict else numbers[-1]
  number = int(first + last)
  total += number

#   matches = re.finditer(r'one|two|three|four|five|six|seven|eight|nine', x)
# #   results = [int(match.group(1)) for match in matches]
#   for i in matches:
#     print(i.start(1), i.end(1))


#   print(x)
#   print(string)
#   print(numbers)
#   print(f'{i} {number}')
#   break

  #break
print(total)