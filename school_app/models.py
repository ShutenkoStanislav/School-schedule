from django.db import models



class Subject(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class  Teacher(models.Model):
    name = models.CharField(max_length=100)
    experience = models.CharField(max_length=30)
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
    
    def __str__(self):
        return self.name
    


    
class Schedule_main(models.Model):
    WEEK_DAY_LIST = [
        ("MON", "понеділок"),
        ("TUE", "вівторок"),
        ("WED", "середа"),
        ("THU", "четвер"),
        ("FRI", "п'ятниця"),
    ]
    day_variant = models.CharField(max_length=3, choices=WEEK_DAY_LIST)
    lesson_number = models.IntegerField()
    conn_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    conn_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    conn_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class Meta:
        unique_together = ['day_variant', 'lesson_number', 'conn_class']
    def __str__(self):
        return f"{self.conn_class} - {self.day_variant}"

class Grade(models.Model):
    number_grade = models.IntegerField(null=True, blank=True)
    letter_grade = models.CharField(max_length=5,null=True, blank=True)
    rel_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rel_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.rel_student} - {self.rel_subject}"





    