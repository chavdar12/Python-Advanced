def input_to_dictionary(number_of_entries):
    student_grade = {}
    for _ in range(number_of_entries):
        name, grade = input().split()

        if name not in student_grade:
            student_grade[name] = []
        student_grade[name].append(float(grade))

    return student_grade


def calculate_average(dictionary):
    student_grade_average = {}
    for student, grades in dictionary.items():
        avg = sum(grades) / len(grades)
        student_grade_average[student] = f'{avg:.2f}'

    return student_grade_average


def print_result(all_grades, avg_grades):
    for student, grades in all_grades.items():
        print(f"{student} -> {' '.join([f'{num:.2f}' for num in grades])} (avg: {avg_grades[student]})")


n = int(input())

students_corresponding_grades = input_to_dictionary(n)
students_avg_grades = calculate_average(students_corresponding_grades)
print_result(students_corresponding_grades, students_avg_grades)
