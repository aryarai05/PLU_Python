'''
8. Hospital Emergency Queue
A hospital has a list of patients with different priority levels.
Write a program to arrange the patients so that the patient with the
highest priority is treated first.
'''
priority = list(map(int, input("Enter priorities: ").split()))

n = len(priority)

for i in range(n):
    for j in range(n - i - 1):
        if priority[j] < priority[j + 1]:
            priority[j], priority[j + 1] = priority[j + 1], priority[j]

print("Treatment Order:", priority)