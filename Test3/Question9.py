'''
9. Library Book Search
A library has 10,000 books, and the Book IDs are already arranged in
ascending order.
Write a program to find a given Book ID efficiently.
Also mention which searching algorithm you used and why it is suitable.
'''
books = list(map(int, input("Enter sorted Book IDs: ").split()))
key = int(input("Enter Book ID: "))

low = 0
high = len(books) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if books[mid] == key:
        print("Book Found at Position:", mid)
        found = True
        break
    elif books[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Book Not Found")