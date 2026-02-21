#Prompt: assign a list to the values [1, 2, 3, 4, 5]. Calculate (we've decided on calculating the average), then output the list backwards.
def questionSeven():
  myList = [1, 2, 3, 4, 5]
  myListAverage = sum(myList) / len(myList)


  print(myListAverage)
  print(myList[::-1])


#Prompt: assign a variable to the string "seven." Output the string with 1 of the first letter followed by 2 of the second letter...5 of the fifth letter.
def questionEight():
  myVar = "seven"
  for i in range(len(myVar)):
    print(myVar[i] * (i + 1))

#Prompt: declare a var, assign it to "froglizardfroglizard," and output True if "frog" and lizard appear the same number of times. If last condition is not true, output False.
def questionTen():
  myVar = "froglizardfroglizard"
  frogCount = 0
  lizardCount = 0


  for i in range(len(myVar)):
    if myVar[i:i+4] == "frog":
        frogCount += 1
    if myVar[i:i+6] == "lizard":
        lizardCount += 1

  if frogCount == lizardCount:
    print(True)
  else:
    print(False)

def questionNine():
  my_var = 5
  rmdr = my_var % 7
  days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

  print(days[rmdr])

def questionEleven():
  weirdList = [8, 6, 2, 8, 7, 5, 2]
  weirdListSum = 0
  
  for v in weirdList:
      if v != 8 and v!= 2:
          weirdListSum += v
  
  print(weirdListSum)
