from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db.models import Q

from .models import Course, Enrollment
from .serializers import CourseSerializer, EnrollmentSerializer
from .permissions import IsAdminUserOnly


from rest_framework.pagination import PageNumberPagination


class CoursePagination(PageNumberPagination):
    page_size = 5


class CourseListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        search = request.GET.get('search')

        courses = Course.objects.filter(is_active=True)

        if search:
            courses = courses.filter(
                Q(title__icontains=search)|
                Q(description__icontains=search)
            )
        
        paginator = CoursePagination()
        paginated_courses = paginator.paginate_queryset(courses, request)

        serializer = CourseSerializer(paginated_courses, many=True)
        return paginator.get_paginated_response(serializer.data)
    

class CourseCreateAPI(APIView):
    permission_classes = [IsAuthenticated, IsAdminUserOnly]

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EnrollCourseAPI(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        course_id = request.data.get('course')

        try:
            course = Course.objects.get(id=course_id, is_active=True)
        except Course.DoesNotExist:
            return Response(
                {"error":"Course not found"},
                status= status.HTTP_404_NOT_FOUND
            )
        enrollment, created = Enrollment.objects.get_or_create(
            student=request.user,
            course=Course
        )

        if not created:
            return Response(
                {"message": "Already enrolled"},
                status=status.HTTP_200_OK
            )
        
        serializer = EnrollmentSerializer(enrollment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class MyEnrollmentsAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get (self, request):
        enrollments = Enrollment.objects.filter(student=request.user)
        serializer = EnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)