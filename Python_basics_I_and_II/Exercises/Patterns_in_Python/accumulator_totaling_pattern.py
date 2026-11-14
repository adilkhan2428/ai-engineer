# Whenever you need to keep a running total, count items based on a condition, or collect results as you loop through data, you need an accumulator variable.

# Task 1. 
# we have a dict of weekly study hours logged by different students.
study_hours = {"Ali": 12, "Sara": 4, "Ahmed": 8, "Ayesha": 15}
total = 0
count_studious_student = 0
for name, hour in study_hours.items():
    total += hour
    if hour >= 10:
        count_studious_student += 1
print(f"Combined Study hours: {total}")
print(f"Number of Studious Student: {count_studious_student}")