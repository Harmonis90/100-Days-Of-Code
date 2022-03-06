# Making a dictionary
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop": "The action of doing something over and over again."}

capitals = {
    "France": "Paris", "Germany": "Berlin",
}
# Nesting a list[] in a dictionary{}
travel_log_trainer = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "USA",
        "states_visited": ["New Jersey", "New York", "Pennsylvania"],
        "favorite_state": "New Jersey"
    },
]
# Challenge: Create a listed nested with dictionaries


travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country, num_visits, cities_visited):
    country_log = {"country": country, "visits": num_visits, "cities": cities_visited}
    travel_log.append(country_log)


# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"
# Convert student scores to text in a separate dictionary
def student_score_to_grade():
    student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99,
        "Draco": 74,
        "Neville": 62,
    }

    student_grades = {}

    for key in student_scores:
        value = student_scores[key]
        if 91 <= value <= 100:
            student_grades[key] = "Outstanding"
        elif 81 <= value <= 90:
            student_grades[key] = "Exceeds Expectations"
        elif 71 <= value <= 80:
            student_grades[key] = "Acceptable"
        else:
            student_grades[key] = "Fail"
    print(student_grades)

