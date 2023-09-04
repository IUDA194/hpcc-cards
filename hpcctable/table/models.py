from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=200)
    year_of_study = models.IntegerField()

    def __str__(self):
        return self.full_name

class Group(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    parent_group = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subgroups')
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.name
