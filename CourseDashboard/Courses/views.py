from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Person, PersonCourseActivity
from .serializer import PersonSerializer, PersonCourseActivitySerializer


class UserList(APIView):

    def get(self, request):
        users = Person.objects.all()
        serializer = PersonSerializer(users, many=True)
        return Response(serializer.data)


class UsersEnrollment(APIView):
    queryset = PersonCourseActivity.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id', 'course_id', 'user_id__manager_id',
                        'course_id__company', 'course_id__course_name']

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request):
        queryset = self.filter_queryset(self.queryset)
        serializer = PersonCourseActivitySerializer(queryset, many=True)
        return Response(serializer.data)
