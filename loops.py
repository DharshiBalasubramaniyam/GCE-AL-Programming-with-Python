# loops

# 1. while

# count = 6
# while count < 5: # it checks the condition first
#     print("Hello world!")
#     count = count + 1

# 1 2 3 4 5 6 7 8 9 10
# 2 4 6 8 10

# 2. for
# for count in range(1, 6):
#     print(count, end=" ")
#
# print()
#
# for count in range(6):
#     print(count, end=" ")
#
# print()
#
# for count in range(1, 11, 2):
#     print(count, end=" ")
#
# print()
#
# for count in range(10, 1, -2):
#     print(count, end=" ")

# Enter the base: 2
# Enter the power: 5
# result = 32

# base = int(input("Enter the base: "))
# power = int(input("Enter the power: "))
# result = 1
# for count in range(power):
#     result = result * base
#
# print("Result: ", result)


# Enter a number: 5
# factorial = 120

# marks = [54, 78, 96, 35, 25]
#
# # for index in range(len(marks)):
# #     print(marks[index], end=" ")
# # print()
# for mark in marks:
#     if mark % 2 == 0:
#         print(mark, end=" ")
#
# print()
# name = "John smith"
# for letter in name:
#     print(letter, end=" ")

# print whether a number is exists in the list or not

# number = int(input("Enter the base: "))  # 100

# find number of vowels in a string
# find the factorial of a number
#
# number = int(input("Enter the number: "))
# factorial = 1
# if number < 0:
#     print("Cannot find factorial for negative number")
# else:
#     for count in range(1, number+1):
#         factorial *= count # x = x+1 => x+=1
#     print(number, "! =", factorial)
# find the number of elements in the list using loop
# myList = [1, 2, 3, 4, 5]
# count = 0
# for number in myList:
#     count+=1
# print(count)
# find the average of the numbers in the list
# myList = [1, 2, 3, 4, 5]
# total = 0
# for number in myList:
#     total += number
# average = total/len(myList) # 0 / 5 = 0
# print(average)
# print(total)

# find the largest number in the list
# myList = [10, 58, 45, 63, 22]
# largestNo = myList[0]
# for number in myList:
#     if number > largestNo:
#         largestNo = number
# print(largestNo)

# find the smallest number in the list
# reverse a string: input: hello -> output: olleh
# word = input("Enter a word: ")
# for index in range(-1, len(word) * -1 - 1, -1):
#     print(word[index], end="")
#
# for index in range(len(word) - 1, -1, -1):
#     print(word[index], end="")

# find whether a number is prime or not
number = int(input("enter a number:"))
i = 2
isPrime = True
for i in range(2, number):  # 1 - 5
    if number % i == 0:
        isPrime = False
        break
    i += 1
if isPrime:
    print("is a prime number")
else:
    print("is not a prime number")

# if noOfFactors > 2:
#     print("is not a prime number")
# else:
#     print("is a prime number")
# number = int(input("enter: "))
# for i in range(1, 16):
#     value = number * i
#     print(i, "x", number, "=", value)

# nested loops


# break, continue
# file handling
# sorting
