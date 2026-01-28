from django.urls import path
from .views import(
    CourseListAPI,
    CourseCreateAPI,
    EnrollCourseAPI,
    MyEnrollmentsAPI
)

urlpatterns = [
    path('api/courses/', CourseListAPI.as_view()),
    path('api/courses/create', CourseCreateAPI.as_view()),
    path('api/enroll/', EnrollCourseAPI.as_view()),
    path('api/my-Courses/', MyEnrollmentsAPI.as_view()),
]
