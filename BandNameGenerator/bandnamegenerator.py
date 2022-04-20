print("What is the city that you grew up in?")
city = input() ##input function takes user input on a new line
print("What is the name of your favorite pet?")
pet = input()
bandName = "The " + city + " " + pet + "s"
print(f"Your band name is: {bandName}") ##f is used in front of string literal to tell print function that item in {} is a variable to be used
