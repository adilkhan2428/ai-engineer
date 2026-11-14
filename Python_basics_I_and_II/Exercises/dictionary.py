student = {
    'name': 'Ali',
    'id': 123123,
    'class': 12,
    'subject': 'Artificial Intelligence',
    'gender': 'Male', 
}

print(student)

# Nested Dictionary

student = {
    1: {
    'name' : 'adil',
    'courses': ['AI', 'ecom', 'business']
    },
    2: {
    'name' : 'atif',
    'courses': ['bio', 'science']
    }
}

for i in range(0, 11):
    if i % 2 == 0:
        print(i)


students = {
    0: {
        'name': 'Ali',
        'id':'17301',
        'class': 12,
        'courses': [
            {'name': 'Maths', 'score': 87},
            {'name': 'Chem', 'score': 88},
            {'name': 'Phy', 'score': 89}
        ],
        'gender': 'Male',
    },
    1: {
        'name': 'Zaman',
        'id':'17302',
        'class': 12,
        'subject': 'Physics',
        'gender': 'Male',
        'courses': [
            {'name': 'Maths', 'score': 87},
            {'name': 'Chem', 'score': 88},
            {'name': 'Phy', 'score': 89}
        ],
    },
    2: {
        'name': 'Fakhar',
        'id':'17303',
        'class': 12,
        'subject': 'Physics',
        'gender': 'Male',
        'courses': [
            {'name': 'Maths', 'score': 87},
            {'name': 'Chem', 'score': 88},
            {'name': 'Phy', 'score': 89}
        ],
    },
}
print(students[1]['name'],'\t',students[1]['courses'][1]['name'] ,'\t',students[1]['courses'][1]['score'] )

print(students[1]['courses']['score'])