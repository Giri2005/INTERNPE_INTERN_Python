import random

print("Welcome to Connect Four")
print("-----------------------")

possibleletters = ["A","B","C","D","E","F","G"]
gameboard = [["","","","","","",""], ["","","","","","",""], ["","","","","","",""],
              ["","","","","","",""], ["","","","","","",""], ["","","","","","",""]]

rows = 6
cols = 7

def printgameboard():
  print("\n     A    B    C    D    E    F    G  ", end="")
  for x in range(rows):
    print("\n   +----+----+----+----+----+----+----+")
    print(x, " |", end="")
    for y in range(cols):
      if(gameboard[x][y] == "🟡"):
        print("",gameboard[x][y], end=" |")
      elif(gameboard[x][y] == "🔴"):
        print("", gameboard[x][y], end=" |")
      else:
        print(" ", gameboard[x][y], end="  |")
  print("\n   +----+----+----+----+----+----+----+")

def modifyArray(spacePicked, turn):
  gameboard[spacePicked[0]][spacePicked[1]] = turn


def modifyArray(spacePicked, turn):
      gameboard[spacePicked[0]][spacePicked[1]] = turn

def checkForWinner(chip):
  # to Check horizontal spaces
  for y in range(rows):
    for x in range(cols - 3):
      if gameboard[x][y] == chip and gameboard[x+1][y] == chip and gameboard[x+2][y] == chip and gameboard[x+3][y] == chip:
        print("\nGame over", chip, "wins! Thank you for playing :)")
        return True

  # to Check vertical spaces
  for x in range(rows):
    for y in range(cols - 3):
      if gameboard[x][y] == chip and gameboard[x][y+1] == chip and gameboard[x][y+2] == chip and gameboard[x][y+3] == chip:
        print("\nGame over", chip, "wins! Thank you for playing :)")
        return True

  # to Check upper right to bottom left diagonal spaces
  for x in range(rows - 3):
    for y in range(3, cols):
      if gameboard[x][y] == chip and gameboard[x+1][y-1] == chip and gameboard[x+2][y-2] == chip and gameboard[x+3][y-3] == chip:
        print("\nGame over", chip, "wins! Thank you for playing :)")
        return True

  # to Check upper left to bottom right diagonal spaces
  for x in range(rows - 3):
    for y in range(cols - 3):
      if gameboard[x][y] == chip and gameboard[x+1][y+1] == chip and gameboard[x+2][y+2] == chip and gameboard[x+3][y+3] == chip:
        print("\nGame over", chip, "wins! Thank you for playing :)")
        return True
  return False

def coordinateParser(inputString):
  coordinate = [None] * 2
  if(inputString[0] == "A"):
    coordinate[1] = 0
  elif(inputString[0] == "B"):
    coordinate[1] = 1
  elif(inputString[0] == "C"):
    coordinate[1] = 2
  elif(inputString[0] == "D"):
    coordinate[1] = 3
  elif(inputString[0] == "E"):
    coordinate[1] = 4
  elif(inputString[0] == "F"):
    coordinate[1] = 5
  elif(inputString[0] == "G"):
    coordinate[1] = 6
  else:
    print("Invalid")
  coordinate[0] = int(inputString[1])
  return coordinate

def isSpaceAvailable(intendedCoordinate):
  if(gameboard[intendedCoordinate[0]][intendedCoordinate[1]] == '🔴'):
    return False
  elif(gameboard[intendedCoordinate[0]][intendedCoordinate[1]] == '🟡'):
    return False
  else:
    return True

def gravityChecker(intendedCoordinate):
  # to Calculate space below
  spaceBelow = [None] * 2
  spaceBelow[0] = intendedCoordinate[0] + 1
  spaceBelow[1] = intendedCoordinate[1]
  # to Is the coordinate at ground level
  if(spaceBelow[0] == 6):
    return True
  # to Check if there's a token below
  if(isSpaceAvailable(spaceBelow) == False):
    return True
  return False

leaveLoop = False
turnCounter = 0
while(leaveLoop == False):
  if(turnCounter % 2 == 0):
    printgameboard()
    while True:
      spacePicked = input("\nChoose a space: ")
      coordinate = coordinateParser(spacePicked)
      try:
        # to Check if the space is available
        if(isSpaceAvailable(coordinate) and gravityChecker(coordinate)):
          modifyArray(coordinate, '🟡')
          break
        else:
          print("Not a valid coordinate")
      except:
        print("Error occured. Please try again.")
    winner = checkForWinner('🟡')
    turnCounter += 1
  # to It's the computers turn
  else:
    while True:
      cpuChoice = [random.choice(possibleletters), random.randint(0,5)]
      cpuCoordinate = coordinateParser(cpuChoice)
      if(isSpaceAvailable(cpuCoordinate) and gravityChecker(cpuCoordinate)):
        modifyArray(cpuCoordinate, '🔴')
        break
    turnCounter += 1
    winner = checkForWinner('🔴')

  if(winner):
    printgameboard()
    break
            
