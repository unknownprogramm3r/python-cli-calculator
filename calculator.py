import operator

menu = "1) +", "2) -", "3) *", "4) /"

choiceDict = { 
	1 : "+", 
	2 : "-", 
	3 : "*", 
	4 : "/"
}

operatorDict = {
    1 : operator.add,
    2 : operator.sub,
    3 : operator.mul,
    4 : operator.floordiv,
}

while True:

  print("What kind of operation would you like to perform?")

  for i in menu:
    print(i)

  userChoice = int(input())
  if (userChoice <= len(menu) and userChoice != 0):
    userChoice -= 1
    y = userChoice
    y += 1
    print("your operator: ",choiceDict[y])
    firstNumber = int(input("Please give me first number: "))
    secondNumber = int(input("Please give me second number: "))
    print(operatorDict[y](firstNumber, secondNumber))

    yn = input("Again? y/n")
    if yn == "n":
        break
  else:
    print("Wrong input, please try again!")