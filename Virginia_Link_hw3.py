##########################################################
# Hommework 3 Leap Year Code with error checking
# CS 362
# Virginia Link
# 01/30/2021
##########################################################

#Get user input and check if it is an integer and greater than 0 (making it a possible year)
while True:
    year = input("Please enter a year to check: ")
    try:
        temp = int(year)
        if temp < 0:
            print("Sorry, years must be possitive!")
            continue
        break
    except ValueError:
        print("Sorry, years have to be an integer!")

year = int(year)
#1. Check if evenly divisible by 4
if (year % 4):
    #2. Check if evenly divisible by 100
    if (year % 100):
        #3. Check if evenly divisible by 400
        if (year % 400):
            print("%s is not a leap year :(" %year)
        else:
            print("%s is a leap year!" %year)
    else:
        print("%s is not a leap year :(" %year)
else:
    print("%s is a leap year!" %year)



