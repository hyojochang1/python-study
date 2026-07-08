import math 
import time

##print (round(7.34))
#print (round(9.78))
#print (pow(2,5))o
#print (max(-2,34,5))
#print (min(-4,5,389))

#print (math.e)
#print (math.pi)
#print (math.ceil(9.1))
#print (math.floor(10.90))

timer = int(input("Enter the number of time in secounds (Max is 86399): "))

while timer > 86399 or timer < 0:
    print ("timer must be at least 0 and less than 24 hours")
    timer = int(input("Enter the number of time in secounds (Max is 86399): "))

for i in (range(timer,-1,-1)):
    seconds = i%60
    minutes = int(i/60) % 60
    hour = int(i/3600)
    print (f"{hour:02} : {minutes:02} : {seconds:02}")
    time.sleep(1)

print ("Finished!!!")

cakes = ["strawberry","Choco","Vanilla","Mint"]
fruit = ["Lime","Orange","lemon"]
dessert = [cakes,fruit]

print (dessert[0][3])

for collection in dessert:
    for food in collection:
        print(food,end= " ")