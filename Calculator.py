'''Simple calculator used to perform basic calculator functions such as addition,
subtraction,division and multplication'''

def Addition(value1, value2): # this function will add the two numbers
    return value1 + value2

def subtract (value1, value2):
    return value1 - value2

def Divide(value1, value2):
    return value1 / value2

def multiply(value1,value2):
    return value1 * value2

#print statement for selecting function
print("please selection function \n > Add \n > Subtract \n > Divide \n > Multiply")

#Input form the user to select function

FunctionInput = input("Enter option :")

Num1 = int(input("Please enter the first number:  "))
Num2 = int(input("PLease enter the second number:  "))


# If statement done to select function and read in values

if FunctionInput == "Add":
    print("The answer is ",Addition( Num1, Num2))

elif FunctionInput == "Subtract":
    print("The answer is ",subtract( Num1, Num2))

elif FunctionInput == "Divide":
    print("The answer is ",Divide( Num1, Num2))

elif FunctionInput == "Multipy":
    print("The answer is ",multiply( Num1, Num2))

else:
    print("Error, PLease try again")

#else statement with print error - incase something gose wrong you know its working
#better that and actual error


