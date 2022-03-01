# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#Then check for the number of times the letters in the word LOVE occurs. 
#Then combine these numbers to make a 2 digit number
t = "TRUE"
t = [i for i in list(t)]
l = "LOVE"
l = [i for i in list(l)]
concat_name = f"{name1}{name2}".upper()
count_true = 0
count_love = 0

for i in t:
    for x in concat_name:
        if i == x:
            count_true += 1

for a in l:
    for y in concat_name:
        if a == y:
            count_love += 1

score = int(str(f"{count_true}{count_love}"))
if score < 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


