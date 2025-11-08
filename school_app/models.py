from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class  Teacher(models.Model):
    name = models.CharField(max_length=100)
    expiriens = models.IntegerField()
    teacher_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Class(models.Model):
    title = models.CharField(max_length=15)
    boys = models.IntegerField()
    girls = models.IntegerField()
    total_pupil = models.IntegerField()
    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    school_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    avg_grade = models.FloatField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

# Create your models here.

# Модель "Клас" (Class):
# Модель "Учень" (Student):
# Використовуйте ForeignKey для встановлення зв'язку між учнем та класом.

# Модель "Предмет" (Subject):
# Модель "Вчитель" (Teacher):
# Використовуйте ForeignKey для встановлення зв'язку між вчителем та предметом.