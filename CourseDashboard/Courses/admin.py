from django.contrib import admin

# Register your models here.
from .models import Person, Courses, PersonCourseActivity

admin.site.register(Person)
admin.site.register(Courses)
admin.site.register(PersonCourseActivity)
