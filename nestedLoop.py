# for i in range(5):
#     for j in range(i+1):
#         print("* ", end="")
#     print()

# *
# * *
# * * *
# * * * *
# * * * * *

# break and continue

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i, end=" ")

myList = [1, 2, 3, 4, 5]
target = int(input("Enter a number to find: "))  # 1
isFound = False
for number in myList:
    if number == target:
        isFound = True
        break
if isFound:
    print("in the list")
else:
    print("not in the list")














