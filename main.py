# 1. Which of the following is the correct extension of the Python file?
# a) .python
# b) .pl
# c) .py
# d) .p
#
# 2. What will be the value of the following Python expression?
#  4 + 3 % 5
# a) 7
# b) 2
# c) 4
# d) 1
#
# 3. Which keyword is used for function in Python language?
# a) Function
# b) def
# c) Fun
# d) Define
#
# 4. What will be the output of the following Python code?
#
# i = 1
# while True:
#     if i%3 == 0:
#         break
#     print(i)
#     i += 1
#
# 5. What will be the output of the following Python code snippet if x=1?
# print(x<<2)
# a) 4
# b) 2
# c) 1
# d) 8
#
# 6. What will be the output of the following Python function?
# len(["hello",2, 4, 6])
# a) Error
# b) 6
# c) 4
# d) 3
#
# 7. What will be the output of the following Python code?
# x = 'abcd'
# for i in x:
#     print(i.upper(), end="")
# a) abcd
# b) ABCD
# c) aBCD
# d) ABC
#
# 8. What will be the output of the following Python code snippet?
# for i in [1, 2, 3, 4][::-1]:
#     print(i, end=' ')
# a) 4 3 2 1
# b) 1 2 3
# c) 1 2 3 4
# d) 4 3 2
#
# 9. What will be the output of the following Python code?
#
# x = 'abcd'
# for i in range(len(x)):
#     print(i)
#
# 10. Which of the following is a Python tuple?
# a) {1, 2, 3}
# b) {}
# c) [1, 2, 3]
# d) (1, 2, 3)
#
# 11. Suppose list1 is [3, 4, 5, 20, 5, 25, 1, 3], what is list1 after list1.pop(1)?
#
# 12 Write the output of below programs?
# 1.
# a = True
# b = False
# c = False
#
# if a or b and c:
#     print("GEEKSFORGEEKS")
# else:
#     print("geeksforgeeks")
#
# 2.
# a = True
# b = False
# c = False
#
# if not a or b:
#     print(1)
# elif not a or not b and c:
#     print(2)
# elif not a or b or not b and a:
#     print(3)
# else:
#     print(4)
#
# 3.
# for i in  range(2):
#     print (i)
#
# for i in range(4,6):
#     print (i)
#
# 4.
# a = "GeeksforGeeks "
# b = 13
# print(a + b)
#
# 5.
# dictionary = {}
# dictionary[1] = 1
# dictionary['1'] = 2
# dictionary[1] += 1
#
# sum = 0
# for k in dictionary:
#     sum += dictionary[k]
#
# print(sum)
#
# 6.
# dictionary = {1:'1', 2:'2', 3:'3'}
# del dictionary[1]
# dictionary[1] = '10'
# print(dictionary)
# del dictionary[2]
# print(len(dictionary))
#
# 7.
# nameList = ['Harsh', 'Pratik', 'Bob', 'Dhruv']
# print(nameList[1][-1])
#
# 8.
# nameList = ['Harsh', 'Pratik', 'Bob', 'Dhruv']
# pos = nameList.index("Bob")
# print(pos * 5)
#
# 9.
# geekCodes = [1, 2, 3, 4]
# # List will look like as [1,2,3,4,[5,6,7,8]]
# geekCodes.append([5, 6, 7, 8])
# print(len(geekCodes))
#
# 10.
# def gfg(x, l=[]):
#     for i in range(x):
#         l.append(i * i)
#     print(l)
#
# gfg(2)
#
# 11.
# list1 = ['physics', 'chemistry', 1997, 2000]
# list2 = [1, 2, 3, 4, 5, 6, 7 ]
# print("list1[0]: ", list1[0])
# print("list1[0]: ", list1[-2])
# print("list1[-2]: ", list1[1:])
# print("list2[1:5]: ", list2[1:5])
#
# 12.
# count = 0
# while (count < 3):
#     count = count + 1
#     print("Hello Geek")
#
# 13.
# count = 0
# while (count < 3):
#     count = count + 1
#     print("Hello Geek")
# else:
#     print("In Else Block")
#
# 14.
# count = 0
# while (count == 0):
#     print("Hello Geek")
#
# 15.
# n = 4
# for i in range(0, n):
#     print(i)
#
# 16.
# l = ["geeks", "for", "geeks"]
# for i in l:
#     print(i)
#
# 17.
# print("\nTuple Iteration")
# t = ("geeks", "for", "geeks")
# for i in t:
#     print(i)
#
# 18.
# print("\nString Iteration")
# s = "Geeks"
# for i in s:
#     print(i)
#
# 19.
# print("\nDictionary Iteration")
# d = dict()
# d['xyz'] = 123
# d['abc'] = 345
# for i in d:
#     print(i, d[i])
#
# 20.
# print("\nSet Iteration")
# set1 = {1, 2, 3, 4, 5, 6}
# for i in set1:
#     print(i)
#
# 21.
# for i in range(1, 5):
#     for j in range(i):
#         print(i, end=' ')
#     print()
#
# 22.
# for letter in 'python':
#     if letter == 'y' or letter == 'x':
#         continue
#     print(letter)
#
# 23.
# for letter in 'python':
#     if letter == 'y' or letter == 'x':
#         break
#     print(letter)
#
# 24.
# fruits = ["apple", "orange", "kiwi"]
# for fruit in fruits:
#     print(fruit[0])
#
# 25.
# def digitSum(n):
#     dsum = 0
#     for ele in str(n):
#         dsum += int(ele)
#     return dsum
# digitSum(258)
#
# 26.
# i = 10
# if (i == 10):
#     if (i < 15):
#         print("i is smaller than 15")
#     if (i < 12):
#         print("i is smaller than 12 too")
#     else:
#         print("i is greater than 15")
#
# 27.
# x,y = 12,14
# if(x+y==26):
#     print("true")
# else:
#     print("false")
#
# 28.
# def fun(x):
#     x = x + 1
#     print(x)
# x = 10
# fun(x)
# print(x)
#
# 29.
# a = 10
# b = 56
# print(a, b)
# t = a
# a = b
# b = t
# print(a, b)
#
# 30.
# for i in range(5):
#     for j in range(i):
#         print(j, end=" ")
#     print()
