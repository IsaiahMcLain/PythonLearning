print("Welcome to the tip calculator")

bill = input("What was the total bill? $") ##Lets initilization and output happen on same line

bill = round(float(bill),2) ##converts string input to float and rounds it, more explained on round with final bill
##print(f"${convertedBill}")

tip = input("What percentage tip would you like to give? 10, 12, or 15?")
tip = (float(tip) / 100) + 1 ##Taking the tip and / 100 gives us a percentage but adding a 1 to it gives a value that is the total bill + the amount the percent tip gives us
##print(f"{convertedTip}")

amountOfPeople = int(input("How many people should split the bill?"))
##print(f"{convertedPeople}")

totalPerPerson = (bill / amountOfPeople) * tip

totalPerPerson = round(totalPerPerson, 2) ##Round function takes float you wish to round and int after , is the precision you want

totalPerPerson = "{:.2f}".format(totalPerPerson) ##Deals with issue where 0 won't be added on in the case that the math results in a value with only 1 decimal place. Turns float into a string

print(f"The total amount each person should pay is: ${totalPerPerson}")
