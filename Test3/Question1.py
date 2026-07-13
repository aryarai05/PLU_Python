'''
1. Student Roll Number Search
A teacher has stored the roll numbers of students in a list in the order
they registered. The list is not sorted.
Write a program to check whether a given roll number exists in the list.
If found, display its position; otherwise, print "Student Not Found."
'''
roll = list(map(int, input("Enter roll numbers: ").split()))
key = int(input("Enter roll number to search: "))

found = False

for i in range(len(roll)):
    if roll[i] == key:
        print("Student Found at Position:", i)
        found = True
        break

if not found:
    print("Student Not Found")