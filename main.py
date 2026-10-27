"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45
CS1430_CLASS_MINUTES = 50

# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return cost_per_semester(annual_cost) / CLASS_DAYS_PER_SEMESTER


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return cost_per_semester(annual_cost) / credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return cost_per_credit(annual_cost, credits) * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER


def cost_of_late(annual_cost, credits, minutes_late):
    return (cost_per_class(annual_cost, credits) / CS1430_CLASS_MINUTES) * minutes_late

# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    annual_cost = float(input("Total cost for one year: "))
    credits = int(input("Credits this semester: "))
    while True:
        # Show your menu here.
        print("""
    THE COST OF COLLEGE
    1   Per semester
    2   Per month
    3   Per class day
    4   Per credit
    5   Per CS 1430 class
    6   Cost of being late to CS 1430
    Q   Quit""")
        choice = input("Choose an option: ")

        if choice == "Q":
            print("Thanks for running the numbers!")            
            break
        elif choice == "1":
            print(f"One semester costs ${cost_per_semester(annual_cost):,.2f}")
        elif choice == "2":
            print(f"One month costs ${cost_per_month(annual_cost):,.2f}")
        elif choice == "3":
            print(f"One class day costs ${cost_per_day(annual_cost):,.2f}")
        elif choice == "4":
            print(f"One credit costs ${cost_per_credit(annual_cost, credits):,.2f}")
        elif choice == "5":
            print(f"Every CS 1430 Class costs ${cost_per_class(annual_cost, credits):,.2f}")
        elif choice == "6":
            minutes_late = int(input("Minutes late: "))
            print(f"Being {minutes_late} minute(s) late costs you ${cost_of_late(annual_cost, credits, minutes_late):,.2f}")
        else:
            print("Invalid Option, Try Again!")
        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
