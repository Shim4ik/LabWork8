# Створення словника
students = {}

# Функція для додавання студента до словника
def add_student(group_number, full_name, course, subjects_grades):
        student_id = len(students) + 1 # Створення унікального ID для кожного студента
        students[student_id] = {  # Додавання інформації про студента до словника
        'group_number': group_number,
        'full_name': full_name,
        'course': course,
        'subjects_grades': subjects_grades
    }

# Функція для виведення інформації про всіх студентів
def display_students():
    for student_id, student_info in students.items(): # Перебір кожного студента в словнику
        print(f"ID Студента: {student_id}")
        print(f"Група: {student_info['group_number']}")
        print(f"ПІБ: {student_info['full_name']}")
        print(f"Курс: {student_info['course']}")
        print("Предмети та оцінки:")
        for subject, grade in student_info['subjects_grades'].items(): # Перебір предметів та оцінок кожного студента
            print(f"{subject}: {grade}")
        print("------------------------")

# Функція для виведення студентів, відсортованих за середнім балом
def display_sorted_students_by_average():
    sorted_students = sorted(
        students.items(),
        key=lambda item: sum(item[1]['subjects_grades'].values()) / len(item[1]['subjects_grades']),
        reverse=True
    )
    
    print("Студенти, відсортовані за середнім балом:")
    for student_id, student_info in sorted_students:
        average_grade = sum(student_info['subjects_grades'].values()) / len(student_info['subjects_grades'])
        print(f"ID Студента: {student_id}")
        print(f"Група: {student_info['group_number']}")
        print(f"ПІБ: {student_info['full_name']}")
        print(f"Курс: {student_info['course']}")
        print(f"Середній бал: {average_grade:.2f}")
        print("------------------------")

# Додавання студентів до словника
add_student(101, "Адамчук Олег Вікторович", 3, {"Математика": 78, "Фізика": 80, "Програмування": 89})
add_student(102, "Бабич Олександр Олександрович", 3, {"Математика": 92, "Фізика": 88, "Програмування": 94})
add_student(103, "Гавришко Ірина Петрівна", 1, {"Математика": 85, "Фізика": 87, "Програмування": 90})
add_student(104, "Коваль Марія Павлівна", 1, {"Математика": 88, "Фізика": 84, "Програмування": 91})
add_student(105, "Іванов Іван Іванович", 2, {"Математика": 90, "Фізика": 85, "Програмування": 95})
add_student(106, "Петренко Петро Олегович", 2, {"Математика": 80, "Фізика": 88, "Програмування": 91})

# Виведення інформації про студентів
display_students()

# Виведення відсортованих студентів за середнім балом
display_sorted_students_by_average()

#студенту Гордієнко Владиславу потрібно розробити функцію пошуку студента за прізвищем.
