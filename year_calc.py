#Calculating a leap year
year = int(input("Enter a year to check if it is a leap one"))

if year % 4 == 0:
    print("It's a leap year")

else:
    print("It's not a leap year!")