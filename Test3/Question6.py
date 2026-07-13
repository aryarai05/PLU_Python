'''
 Employee Salary Report
An HR department has employee salary records collected from two different
branches.
Write a program to combine both lists and display all salaries in
ascending order.
'''
salary1 = list(map(int, input("Enter salaries of Branch 1: ").split()))
salary2 = list(map(int, input("Enter salaries of Branch 2: ").split()))

salary = salary1 + salary2

salary.sort()

print("Ascending Salaries:", salary)
