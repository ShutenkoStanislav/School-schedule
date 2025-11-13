





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

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_schedule.settings')
django.setup()


from school_app.models import Schedule_main, Student, Subject, Teacher, Grade, Class


def add_subject():
    title = input("Введіть назву предмету:")
    if Subject.objects.filter(title=title).exists():
        print("Такий предмет вже існує!")
    else:
        Subject.objects.create(title=title)
        print("Предмет додано!")

def  add_teacher():
    name = input("Введіть ім'я вчителя: ")
    experience = input("Введіть досвід вчителя: ")
    print("Тепер додамо предмет до вчителя/ки: ")
    all_subject = Subject.objects.all()
    print("Список предметів: ")
    print(all_subject)
    id_subject = int(input("Введіті ID предмету: "))
    subject = Subject.objects.get(id=id_subject)
    if Teacher.objects.filter(name=name, experience=experience).exists():
        print("Вчитель/ка вже існує!")
    else:
        Teacher.objects.create(name=name, experience=experience, teacher_subject=subject)
        print("Вчитель/ка додано!")

def add_class():
    title = input("Введіть ім'я класу: ")
    boys = int(input("Введіть кількість хлопців: "))
    girls = int(input("Введіть кількість дівчат: " ))
    total_pupil = boys + girls
    if Class.objects.filter(title=title).exists():
        print("Такий клас вже існує")
    else:
        Class.objects.create(title=title, boys=boys, girls=girls, total_pupil=total_pupil)
        print("Клас додано")

def add_student():
    name = input("Введіть ім'я учня/учениці: ")
    avg_grade = float(input("Введіть середній бал учня/учениці у вигляді 3.6: "))
    classes = Class.objects.all()
    print("\nТепер підєднаюмо учня/учениці до класу ")
    print("\nДоступні класи: ")
    print(classes)

    class_id = input("Введіть ID класу: ")
    school_class = Class.objects.get(id=class_id)

    if Student.objects.filter(name=name, avg_grade=avg_grade, school_class=school_class).exists():
        print("Такий учнь/учениця вже існує")
    else:
        Student.objects.create(name=name, avg_grade=avg_grade, school_class=school_class)
        print("Уцня/уцениця додана")


def add_lesson_schedule():
    print("\nДні тижня: 1-ПН, 2-ВТ, 3-СР, 4-ЧТб 5-ПТ")
    day_num = int(input("Введіть номер дня тижня: "))
    days = ["MON","TUE","WED","THU","FRI"]
    day_variant = days[day_num - 1]
    
    lesson_number = int(input("Введіть номер урока (1-9): "))  
    

    all_subject = Subject.objects.all()
    print("\nДоступні уроки: ", all_subject)
    subject_id = int(input("ID предмета: "))
    conn_subject = Subject.objects.get(id=subject_id)

    all_class = Class.objects.all()
    print("\nДоступні класи: ", all_class)
    class_id = int(input("ID класа: "))
    conn_class = Class.objects.get(id=class_id)

    all_teachers = Teacher.objects.all()
    print("\nДоступні вчителі: ",all_teachers)
    teacher_id = int(input("ID вчителя: "))
    conn_teacher = Teacher.objects.get(id=teacher_id)

    if Schedule_main.objects.filter(lesson_number=lesson_number,day_variant=day_variant,conn_class=conn_class).exists():
        print("\nЦей урок вже зайнятий!")
    else:
        Schedule_main.objects.create(lesson_number=lesson_number,day_variant=day_variant,conn_class=conn_class, conn_teacher=conn_teacher, conn_subject=conn_subject)
        print("\nРозклад додано!")

def add_grade():
    all_student = Student.objects.all()
    print("\nУсі вільні учні\учениці:", all_student)
    student_id = int(input("ID учня\учениці: "))
    rel_student = Student.objects.get(id=student_id)

    all_lessons = Subject.objects.all()
    print("\nУсі вільні предмети: ", all_lessons)
    lesson_id = int(input("ID предмета: "))
    rel_subject = Subject.objects.get(id=lesson_id)

    var_grade = int(input("\nВиберт формат оцінки 1-Цифрою, 2-Буквою: "))
    number_grade = None
    letter_grade = None
    
    if var_grade == 1:
        number_grade = int(input("Оцінка цифрою: "))
    else:
        letter_grade = input("Оцінка буквою: ")

    

    Grade.objects.create(number_grade=number_grade,
                        letter_grade=letter_grade,
                        rel_subject=rel_subject,
                        rel_student=rel_student)
    print("Оцінку додано!")








    






def main():
    while True:
        print("\n Шкільний розклад")
        print("1 - Додати предмет")
        print("2 - Додати вчителя")
        print("3 - Додати клас")
        print("4 - Додати учня")
        print("5 - Додати заняття в розклад")
        print("6 - Додати оцінку")
        print("7 - Кінець")

        choice = input("Оберіть дію:")
        if choice == "1":
            add_subject()
        elif choice == '2':
            add_teacher()
        elif choice == '3':
            add_class()
        elif choice == '4':
            add_student()
        elif choice == '5':
            add_lesson_schedule()
        elif choice == '6':
            add_grade()
        elif choice == '7':
            print("До побачення!")
            break
        else:
            print("Невірний вибір!")

if __name__ == "__main__":
    main()