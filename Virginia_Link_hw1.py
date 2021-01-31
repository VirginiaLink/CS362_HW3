##########################################################
# Homework 1 Leap Year Code
# CS 362
# Virginia Link
# 01/14/2021
##########################################################

print("Please enter a year to check: ")

#Get user input
year = int(input())

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







