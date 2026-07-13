'''
 Insert New Book by Price
A bookstore maintains a sorted list of book prices.
A new book arrives, and its price needs to be placed at the correct
position while keeping the list sorted.
Write a program to perform this task.
'''
price = list(map(int, input("Enter sorted prices: ").split()))
new = int(input("Enter new book price: "))

price.append(new)

i = len(price) - 2

while i >= 0 and price[i] > new:
    price[i + 1] = price[i]
    i -= 1

price[i + 1] = new

print("Updated Price List:", price)