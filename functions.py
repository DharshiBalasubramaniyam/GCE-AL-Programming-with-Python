# functions
# function_name()
# built in functions
# print(pow(2, 5)) # function call


# user-defined function

def sayHello():  # function definition
    print("Hello world!")


# sayHello()  # function call

def sayHelloToUser(name):
    print("Hello", name)


# sayHelloToUser("John")
#
def addTwoNumbers(a=1, b=8):
    result = a + b
    print(result)


# addTwoNumbers(4, 5)
# addTwoNumbers(4)
# addTwoNumbers()

def sindhu(x, *y):
    print(x)
    print(y)


# sindhu(1, 2, 3, 4)

# power = pow(2, 5)
#
# list = [1, 2]
#
# print(len(list))

def addTwoNumbers2(a, b):
    result = a + b
    return result


# result = addTwoNumbers2(1, 2)
# print(result)

def vilashini(x):
    answer = x + 5
    print(x)
    print(answer)


# vilashini(12)

def findY(x):
    result = x ** 2 + 5 * x - 7
    return result


# print(findY(3))

def getNameWithInitials(firstName, lastName):
    name = lastName[0] + ". " + firstName
    return name


print(getNameWithInitials("Dharshi", "Balasubramaniyam"))
