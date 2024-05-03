# conditional statements

# 1. if-else

# number = 7
# if number > 10:
#     print("number is greater than 10.")
# else:
#     print("number is not greater than 10.")

# def myFunc(number):
#     if number >= 0:
#         print(number, "is positive")
#     else:
#         print("negative")
#
#
# myFunc(4) # prints, 4 is a positive number
# myFunc(-4) # prints, -4 is a negative number

# 2. if-elif-else

# marks = 68
# if marks >= 75:
#     print("A")
# elif marks >= 65:
#     print("B")
# elif marks >= 55:
#     print("C")
# elif marks >= 40:
#     print("S")
# else:
#     print("W")


# def findDay(day):
#     if day == 0:
#         print("Monday")
#
# findDay(0) # Monday
# findDay(100) # Invalid argument

# 3. Nested if

# number = 0
# if number >= 0:
#     if number == 0:
#         print(number, "is zero")
#     else:
#         print(number, "is positive")
# else:
#     print(number, "is negative")
for i in range(6):
    for sp in range(i+5):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print()




