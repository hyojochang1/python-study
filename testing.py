import random
import time

books = [["The Bible","The Torah","The Quran"],["Winne Dixie","Peter Pan","Interior Chinatown"],["Hamlet","King Lear","Macbeth"]]
shopping_cart = []
print ("-----This is a shelf of books, chose which books u want-----")

for groups in books:
    for book in groups:
        print(book, end=" ") 
    print()

print("Enter the shelf row and column to pick up a book")
x = int(input("Which row is the book on: "))
y = int(input("Which column is the book on: "))
shopping_cart.append(books[(3-(x))][y-1])

y_n = input(f"Your current shopping cart has {shopping_cart}, would you like to add more (y): ")
while (y_n == "y"):
    x = int(input("Which row is the book on: "))
    y = int(input("Which column is the book on: "))
    shopping_cart.append(books[3-x][y-1])
    y_n = input(f"Your current shopping cart has {shopping_cart}, would you like to add more (y): ")
else:
    print (f"You are buying {shopping_cart}" )
    print("Thank you for shopping!")

print ("This is a simple algebra calculator")
val_before_x = float(input("Enter the multiplier of x: "))
val_added_to_x = float(input("Enter the number being added to x: "))
val_on_other_side = float(input("Enter the number on the other side of the equation: "))
print(f"The equation is {val_before_x}x + {val_added_to_x} = {val_on_other_side}")
answer = str((val_on_other_side-val_added_to_x)/val_before_x)
print ("x is " +answer)

print ("This is a guessing game!")
print ("I will think of a number between 1 and 200" )
print("I will tell you if your guess is lower or higher than the number")

target_number = (random.randint(1,200))

while True:

    guess = int(input("Guess:"))

    if guess == target_number:
        print("You have gotten the number!")
        break
    elif guess < target_number:
        print ("Your guess is lower than the number" )
     
    else:
        print("Your guess is higher than the number")

#print("This is a game of rock paper scissor!")
#print("On go, enter your move")
#movelist = ["scissor","paper","rock"]
#for i in (range(3,0,-1)):
 #   print (i)
  #  time.sleep(1)

#print ("Go!")
#move = input("")
#robot_move = movelist[random.randint(0,2)] 
#print (f"Robot: {robot_move} Player: {move}")

#if move == robot_move:
#    print("Tie!")
#elif move == "scissor" and robot_move == "rock" or 
#    print ("you lose!")

