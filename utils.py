
def show_all_students(all_students):
    print('#'*55)
    print(f'{"name":<15}{"family":<20}{"age":^8}{"grade":^10}')
    for student in all_students:
        print(
            f'{student["name"]:<15}{student["family"]:<20}{student["age"]:^8}{student["grade"]:^10}')


def generate_student():
    student = {}
    name = input('Enter student`s name: ')
    family = input('Enter student`s family: ')
    age = input('Enter student`s age: ')
    grade = input('Enter student`s grade ')
    student['name'] = name
    student['family'] = family
    student['age'] = age
    student['grade'] = grade
    return student
