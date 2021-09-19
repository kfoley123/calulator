import operator

firstNumber = 0
secondNumber = 0 
chosenOperator = ""
answer = 0

operatorMap = {
    "+":operator.add,
    "-":operator.sub,
    "*":operator.mul,
    "/":operator.truediv
}

firstNumber = input("Enter your first number: ")
firstNumber = float(firstNumber)

secondNumber = input("Enter second number: ")
secondNumber = float(secondNumber)

chosenOperator = input("please select operator (+, -, *, /):  ")

if(secondNumber == 0.0 or secondNumber == 0 and chosenOperator == "/"):
    print("you can't divide by zero")

else: 
    answer = operatorMap[chosenOperator](firstNumber,secondNumber)
    print("your answer is: " , answer)

