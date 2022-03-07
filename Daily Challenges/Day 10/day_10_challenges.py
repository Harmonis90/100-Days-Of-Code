# Fuctions with outputs
def format_name(f_name, l_name):
    """Takes a first and last name and returns
    a Tile Case formatted full name as a string."""
    return str(f_name + " " + l_name).title()


name = format_name("seth", "kaplan")

print(name)

# leap if % 4 == 0 or % 400 == 0 but not if only % 100 == 0
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False


def days_in_month(year, month):
    """Takes in an int year and an int month.
    Returns the number of days in the given month accounting for the year.
    (Differs only for February during a leap year)."""
    num_days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap = is_leap_year(year)
    if is_leap and month == 2:
        return 29
    else:
        return num_days_in_month[month - 1]


print(days_in_month(2001, 12))