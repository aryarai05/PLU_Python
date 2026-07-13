'''
10. School Annual Report
A school has recorded the marks of 50 students.
Write a program that:
Sorts the marks in ascending order.
Accepts a mark from the user.
Checks whether that mark exists in the sorted list.
Displays the position if found; otherwise, prints "Mark Not Found."
'''
marks = list(map(int, input("Enter marks: ").split()))

n = len(marks)

for i in range(n):
    for j in range(n - i - 1):
        if marks[j] > marks[j + 1]:
            marks[j], marks[j + 1] = marks[j + 1], marks[j]

print("Sorted Marks:", marks)

key = int(input("Enter mark to search: "))

found = False

for i in range(len(marks)):
    if marks[i] == key:
        print("Mark Found at Position:", i)
        found = True
        break

if not found:
    print("Mark Not Found")