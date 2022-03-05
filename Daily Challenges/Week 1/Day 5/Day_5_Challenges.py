
def student_height_avg():
    # 🚨 Don't change the code below 👇
    student_heights = input("Input a list of student heights ").split()
    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])

    # 🚨 Don't change the code above 👆
    counter = 0
    height_sum = 0
    for i in student_heights:
        height_sum += i
        counter += 1
    print(round(height_sum / counter))

    #Write your code below this row 👇


def find_high_score():
    # 🚨 Don't change the code below 👇
    student_scores = input("Input a list of student scores ").split()
    for n in range(0, len(student_scores)):
        student_scores[n] = int(student_scores[n])
    print(student_scores)
    # 🚨 Don't change the code above 👆
    high_score = student_scores[0]
    for score in student_scores:
        if score > high_score:
            high_score = score

    print(f"The highest score is: {high_score}")
    #Write your code below this row 👇


def sum_of_evens(range_min, range_max):
    print(sum([i for i in range(range_min, range_max + 1) if i % 2 == 0]))


def fizz_buzz(range_min, range_max):

    # print each number from 1 to 100 in turn.
    # When the number is divisible by 3 then instead of printing the number it should print "Fizz".
    # When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
    # And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
    for num in range(range_min, range_max + 1):
        if num % 3 == 0:
            if num % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

