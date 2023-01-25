#we import the locale module to handle currencies
import locale
#imports our regular expression
import re

#This sets the current locale to the US
locale.setlocale(locale.LC_ALL, 'en_US.utf8')

#Defines a regular expression pattern to match currency symbols
pattern = r'[$£€¥]'

#Below prints our welcome message
print("Welcome to the tip calculator.")

#Creating our input variables
#re.sub is used to replace any symbols found in pattern and our total bill input with a empty space
bill = (re.sub(pattern, "", input("What is was the total bill? \n")))

tip_percentage = input(
    "What percentage tip would you like to give? 15, 18, or 20? \n")

party = int(input("How many people are spliting the bill? \n"))

#We create a loop in order to make sure party size is not zero

while True:
    if party >= 1:
        party = party
        break
    else:
        party = 1

#Type Conversion
tip = float("1." + tip_percentage)
bill = float(bill)

#Our output, formatted as our currency, and rounded to 2 decimal places
total_per_person = locale.currency(round((bill * tip) / party, 2), grouping=True)
#grouping is used to help us format the number with the local thousands separator

#f-string for ease of reading the syntax
print(f"Each person should pay: {total_per_person}")

