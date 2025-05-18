age = input("What is your current age?\n")

# Constants
DAYS_IN_YEAR = 365
WEEKS_IN_YEAR = 52
MONTHS_IN_YEAR = 12
MAX_AGE = 90

# Convert input to int
current_age = int(age)

# Total time for 90 years
total_days = MAX_AGE * DAYS_IN_YEAR
total_weeks = MAX_AGE * WEEKS_IN_YEAR
total_months = MAX_AGE * MONTHS_IN_YEAR

# Time already lived
lived_days = current_age * DAYS_IN_YEAR
lived_weeks = current_age * WEEKS_IN_YEAR
lived_months = current_age * MONTHS_IN_YEAR

# Time left
days_left = total_days - lived_days
weeks_left = total_weeks - lived_weeks
months_left = total_months - lived_months

# Output
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
