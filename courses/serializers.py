from rest_framework import serializers
from .models import Course, Enrollment

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title','description', 'is_active', 'created_at']


class EnrollmentSerializer(serializers.ModelSerializer):
    course_title = serializers.ReadOnlyField(sourse='course.title')

    class Meta:
        model = Enrollment
        fields=['id', 'course', 'course_title', 'enrolled_on']
        