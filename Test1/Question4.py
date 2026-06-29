#Print the multiplication table of a given number up to 10.
n = int(input("Enter the number you want to print the table: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
