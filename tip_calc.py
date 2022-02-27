#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
#Greeting:
print("Tipsies Tip Calculator")

#Get and format total
get_total = input("Please enter the total bill amount with a decimal.\n\t Total: $")

bill = float("{:.2f}".format(float(get_total)))

#Get and format tip
get_tip = input("How much would you like to tip the server?\nAverage is 15% to 20%:\n\tTip: ")
is_enough = False
tip = int(get_tip)
while not is_enough:
  if 20 >= tip >= 10:
    is_enough = True
  elif tip < 10:
    get_tip_again = input(f"{tip}% is a bit low. Don't be stingy!\nPlease enter a higher tip\n\tTip: ")
    tip = int(get_tip_again)
  elif tip > 20:
    high_tip_check = input(f"Are you sure you want to add {tip}% to the bill?\n 'Y' 'N'")
    if high_tip_check[0].upper() == "Y":
      print(f"Very generous!")
      is_enough = True
    else:
      tip_redo = input("What would you like the new tip to be?\n\tTip: ")
      tip = int(tip_redo)
      continue

print(f"{tip} will be calculated into the total bill.")


#Get number of people to split total
people_count = input("How many people are splitting the bill?\n\tPeople: ")
print(people_count + " {p}".format(p="person" if int(people_count) == 1 else "people"))

formatted_tip = float((tip + 100) / 100)
formatted_bill = f"{bill:.2f}"
people = int(people_count)
total = (bill / people) * formatted_tip
formatted_total = f"{total:.2f}"
p = "person" if int(people_count) == 1 else "people"
print(f"With a total of:\n\t${formatted_bill}\nA tip of:\n\t{tip}%\nAnd {people_count} {p}...")
print(f"\nTOTAL: ${formatted_total}")

print("Thank you for using Tipsies Tip Calculator!")
print("I will \"Calc\" \"U\" \"Later\" ;-)")