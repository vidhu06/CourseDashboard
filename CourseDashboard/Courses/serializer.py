from rest_framework import serializers
from .models import Person, PersonCourseActivity


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ['user_id', 'name']


class PersonCourseActivitySerializer(serializers.ModelSerializer):
    person_id = serializers.IntegerField(source='user_id.user_id')
    person_name = serializers.CharField(source='user_id.name')
    manager = serializers.SerializerMethodField()
    course_name = serializers.CharField(source='course_id')
    total_modules = serializers.IntegerField(source='course_id.total_modules')
    completion_percent = serializers.SerializerMethodField()

    class Meta:
        model = PersonCourseActivity
        fields = ['person_id', 'person_name', 'manager', 'course_name', 'is_started',
                  'total_modules', 'completed_modules', 'is_completed', 'completion_percent']

    def get_manager(self, obj):
        manager = Person.objects.get(user_id=obj.user_id.manager_id)
        return PersonSerializer(manager).data

    def get_completion_percent(self, obj):
        percent = (obj.completed_modules/obj.course_id.total_modules)*100
        return str(percent)+"%"
