
books = [["The Bible","The Torah","The Quran"],["Winne Dixie","Peter Pan","Interior Chinatown"],["Hamlet","King Lear","Macbeth"]]
shopping_cart = [""]
print ("-----This is a shelf of books, chose which books u want-----")

for groups in books:
    for book in groups:
        print(book, end=" ") 
    print()

print("Enter the shelf row and column to pick up a book")
x = int(input("Which row is the book on: "))
y = int(input("Which column is the book on: "))

y_n = input(f"Your current shopping cart has {shopping_cart}, would you like to add more (y/n): ")
while (y_n == "y"):
    x = int(input("Which row is the book on: "))
    y = int(input("Which column is the book on: "))
    shopping_cart.append(books[x][y])
    y_n = input(f"Your current shopping cart has {shopping_cart}, would you like to add more (y/n): ")
else:
    print("Thank you for shopping!")