# person_2 = {
#     'id': 1,
#     'name': "sara",
#     'age': 30
# }

# for item in person_2:
#     print(item)

# for item in person_2.keys():
#     print(item)

# for item in person_2.values():
#     print(item)

# for item in person_2.items():
#     print(f'{item[0]} = {item[1]}')

# for index, value in person_2.items():
#     print(f'{index} = {value}')

# "msa".upper()


# def my_func_1(number1 , number2= 0):
#     print(number1, number2)

# my_func_1(1)

# def my_func(*args):
#     print(args)

# my_func(1,2,3,4,5,6)


# def my_func_2(name, family):
#     print(f'{name} {family}')

# my_func_2(family="rezaei", name="sara")

# def my_func_3(*args,**kwargs):
#     print(args)
#     print(kwargs)

# my_func_3(name="blalal", family = "sssss", age= 19)
# my_func_3("blalal", "sssss", 19)


# numbers = [1,20,3,4]

# new_numbers = sorted(numbers)
# print(new_numbers)
# numbers.sort(reverse=True)
# print(numbers)


# یک تابع بنویسید که به تعداد دلخواه عدد بگیرد و اعداد داده شده را با هم جمع نماید و
# حاصل را نمایش دهد


# person = {
#     'id': 1,
#     'name': "sara",
#     'age': 30
# }

# person['age'] = 35
# person['national_code'] = 12345
# del person['name']
# print(person)

# numbers = [1,2,3,4,5,2,5]
# numbers.append(100)
# print(numbers)
# numbers.remove(2)
# del numbers[1]
# print(numbers)

# print(numbers.count(2))
# count = 0
# for num in numbers:
#     if num == 2:
#         count += 1

# print(count)
# numbers = [1,2,3,4,5,2,5]
# numbers.append([123,456])
# print(numbers[-1][0])
# numbers.extend([123,456])
# print(numbers)
# numbers += [123,456]
# print(numbers)

# string1 = "12345"
# string2 = "678"

# print(string1 + string2)


# numbers = [1,2,3,4,5,2,5]

# numbers.insert(1, 2000)
# print(numbers)

# x = numbers.pop()
# print(x)
# print(numbers)

# x = numbers.pop(0)
# print(x)
# print(numbers)

# numbers = [1,2,3,4,5,2,5]
# print(numbers.index(3))
from colorama import Fore, Back, Style
from utils import show_all_students, generate_student
all_students = []


running = True
while running:

    print(f'''
    {Fore.GREEN}To add a student -> 1{Style.RESET_ALL}
    {Back.RED}To Remove a student -> 2{Style.RESET_ALL}
    To Update a student -> 3
    To Show all students -> 4
    To Search a student -> 5
    To exit -> 0''')

    user_input = '6'
    while not user_input.isdecimal() or int(user_input) not in (0, 1, 2, 3, 4, 5):
        user_input = input('Enter a number between 0 util 5> ')

    if user_input == '1':
        student = generate_student()
        all_students.append(student)

    if user_input == '2':
        student_name_to_remove = input('Enter student`s name:> ')

    if user_input == '4':
        show_all_students(all_students)

    if user_input == '0':
        exit()
