





# subject_1 = Subject(
#     title = "Math"
# )

# subject_2 = Subject(
#     title = "PE"
# )

# subject_3 = Subject(
#     title = "English"
# )

# subject_4 = Subject(
#     title = "Art"
# )

# teacher_1 = Teacher(
#     name = "Addin Hall",
#     experiens = 10

# )

# teacher_2 = Teacher(
#     name = "Ben Dack",
#     experiens = 2
# )

# class_1 = Class(
#     title = "6-a",
#     boys = 10,
#     girls = 13,
#     total = 23
# )

# class_2 = Class(
#     title = "6-a",
#     boys = 14,
#     girls = 12,
#     total = 26
# )

# studen_1 = Student(
#     name = "Greg Brohg",
#     avg_grade = 3.7
# )

# studen_2 = Student(
#     name = "Stafany Moon",
#     avg_grade = 4.7
# )

# schedule_1 = Schedule_main(
#     day_variant = "MON",
#     lesson_number = 2

# )

# schedule_2 = Schedule_main(
#     day_variant = "FRI",
#     lesson_number = 4

# )

# grade_1 = Grade(
#     number_grade = 10
# )

# grade_2 = Grade(
#     letter_grade = "A+"
# )




import os
import django
from django.core.exceptions import ObjectDoesNotExist
from school_app.models import Schedule_main, Student, Subject, Teacher, Grade, Class


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_schedule.settings')


django.setup()


def add_subject():
    title = input("Введіть назву предмету:")
    if Subject.objects.filter(title=title).exists():
        print("Такий предмет вже існує!")
    else:
        Subject.objects.create(title=title)
        print("Предмет додано!")

def  add_teacher():
    name = input("Введіть ім'я вчителя")
    experience = input("Введіть досвід вчителя")






def main():
    while True:
        print("\n Шкільний розклад")
        print("1 - Додати предмет")
        print("2 - Додати вчителя")
        print("3 - Додати клас")
        print("3 - Додати учня")
        print("5 - Вихід")
        choice = input("Оберіть дію:")
        if choice == "1":
            add_subject()
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            print("До побачення!")
            break
        else:
            print("Невірний вибір!")

if __name__ == "_main__":
    main()