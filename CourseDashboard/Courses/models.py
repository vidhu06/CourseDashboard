from django.db import models


class Person(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    manager_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=225)
    company = models.CharField(max_length=225)
    total_modules = models.IntegerField()

    def __str__(self):
        return self.course_name

    class Meta:
        unique_together = ('course_name', 'company')


class PersonCourseActivity(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('Person', on_delete=models.CASCADE)
    course_id = models.ForeignKey('Courses', on_delete=models.CASCADE)
    completed_modules = models.IntegerField(default=0)
    is_started = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    updated_ts = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user_id', 'course_id')
