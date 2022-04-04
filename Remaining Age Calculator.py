# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆
x = 365
y = 52
z = 12
a = 0
b = 90

#Write your code below this line 👇
e = b*x
f = b*y
g = b*z
#total age - current age
age_days = int(age)*x
age_weeks = int(age)*y
age_months = int(age)*z

age_days_new = e - age_days
age_weeks_new = f - age_weeks
age_months_new = g - age_months

print(f"You have {age_days_new} days, {age_weeks_new} weeks, and {age_months_new} months left.")


