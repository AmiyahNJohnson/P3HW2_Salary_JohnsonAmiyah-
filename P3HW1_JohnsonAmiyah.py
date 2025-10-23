# P3HW1_JohnsonAmiyah
# Amiyah Johnson
# Date: October 23, 2025
# This program takes numeric grades for six modules,
# determines the lowest, highest, sum, and average,
# and then displays the letter grade for the average.

# ---- Enter grades for six modules ----
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# ---- Add grades entered to a list ----
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# ---- Determine lowest, highest, sum, and average ----
low = min(grades)
high = max(grades)
sum_of_grades = sum(grades)
avg = sum_of_grades / len(grades)

# ---- Display results ----
print('------------Results------------')
print(f'Lowest Grade: {low:.1f}')
print(f'Highest Grade: {high:.1f}')
print(f'Sum of Grades: {sum_of_grades:.1f}')
print(f'Average: {avg:.2f}')
print('----------------------------------')

# ---- Determine letter grade for average ----
if avg >= 90:
print('Your grade is: A')
elif avg >= 80:
print('Your grade is: B')
elif avg >= 70:
print('Your grade is: C')
elif avg >= 60:
print('Your grade is: D')
else:
print('Your grade is: F')
