# read = "r"
# write = "w"
# append = "a"

# writing
# file = open("fruits.txt", "w") # open a new file if not exists, rewrite from scratch
# fruits = ["Apple", "Orange", "Mango", "Banana"]
#
# for fruit in fruits:
#     file.write(fruit + "\n")
#
# file.close()

# appending
# studentFile = open("students.txt", "a") # open a new file if not exists, write from the end
#
# newStudent = "Tanya"
# studentFile.write("\n")
# studentFile.write(newStudent)
#
# studentFile.close()


# reading
# studentsFile = open("students.txt", "r") # error if not exists file
#
# total = 0

# for line in studentsFile:
#     l = line.split(":")
#     marks = float(l[1])
#     total += marks
# studentsFile.close()
#
#
# outputFile = open("output.txt", "w")
#
# outputFile.write("Total marks = " + str(total))
#
# outputFile.close()


# studentsfile =open("students.txt", "r")
# resultfile =open("result.txt", "w")
# total=0
# max=0
#
# for line in studentsfile:
#     l=line.strip().split(",")
#     total=float(l[1])+float(l[2])+float(l[3])
#     avg=float(total/3)
#     avg = round(avg, 2)
#     if total > max:
#         max = total
#         topper = l[0]
#
#     resultfile.write(l[0] + "," + str(total) + "," + str(avg))
#     resultfile.write("\n")
# studentsfile.close()
# resultfile.write("TOPPER:"+topper)
#
#

#resultfile.close()

f = open("marks.txt", "w")
index = int(input("enter ind_no="))
while index != -1:
    m1 = (input("enter marks 1="))
    m2 = (input("enter marks 2="))
    m3 = (input("enter marks 3="))
    f.write(str(index) + "," + m1 + "," + m2 + "," + m3 + "\n")
    index = int(input("enter ind_no="))

f.close()



