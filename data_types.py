# 1. Integer (int)

no_of_books = 10
# print(type(no_of_books))

# 2. Float (float)
average = 85.5
# print(type(average))

# 3. boolean (bool)
isValid = True
isMarried = False
# print(type(isMarried))

# 4. String (str)
subject = "Mathematics"
name = 'John'
# print(type(subject))

print(subject[0])  # output: M
print(subject[6])  # output: a
print(subject[-9])  # output: t

print(subject[2:5])  # output: the
print(subject[-5:-2])  # output: ati

print(subject[2: 9: 2])  # output: taei
print(subject[2: 9: 3])  # output: tmi
print(subject[-10: -2: 3])  # output: aet

print(subject[:: 4])  # output: Mei
print(subject[:5:])  # output: Mathe

print(len(subject))  # 11
print(subject.count("a"))  # 2
print(subject.count("x"))  # 0
print(subject.upper())  # MATHEMATICS

print("My favourite subject is " + subject + "!")  # My favourite subject is Mathematics!
print("cat" * 3)

# 4. List (list)
my_list = [2, 5]
print(my_list[1: 3: 1])

my_list[0] = 45  # [45, 5, 'hello', 5.6]

my_list.append(85)  # [45, 5, 85]
my_list.insert(1, 10)  # [45, 10, 5, 85]
my_list.pop()  # [45, 10, 5]
my_list.remove(10)  # [45, 5]
my_list.reverse()  # [5, 45]
print(my_list)

# 6. Tuple (tuple)
my_tuple = (1, 2, 3, 4, "hello")
print(my_tuple[2])

# 7. Dictionary
student_marks = {"mala": 89, "john": 58, "rahul": 78, "jack": 25}
print(student_marks.keys())  # dict_keys(['mala', 'john', 'rahul', 'jack'])
print(student_marks.values())  # dict_values([89, 58, 78, 25])
print(student_marks.get("mala"))  # 89

# 8. Set
my_set = {1, 1, 1, 1, 2}
my_set.add(5)
print(my_set)  # {1, 2, 5}
print(my_set.intersection({2, 8, 9}))  # {2}
