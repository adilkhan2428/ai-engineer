students = {
    "Ali": 85,
    "Sara": 72, 
    "Ahmad": 35, 
    "Ayesha": 91, 
    "Usman": 55, 
}

def grade(marks):
    if marks >= 80: 
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"
for name, marks in students.items():
    grades = grade(marks)
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grades}")


