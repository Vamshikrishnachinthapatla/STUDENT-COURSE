from django.urls import path
from .views import(
    CourseListAPI,
    CourseCreateAPI,
    EnrollCourseAPI,
    MyEnrollmentsAPI
)

from .views_web import (
    course_list_view,
    enroll_course_view,
    admin_dashboard,
    admin_create_course
)

urlpatterns = [
    path('api/courses/', CourseListAPI.as_view()),
    path('api/courses/create', CourseCreateAPI.as_view()),
    path('api/enroll/', EnrollCourseAPI.as_view()),
    path('api/my-Courses/', MyEnrollmentsAPI.as_view()),


    path('courses/', course_list_view, name='course_list'),
    path('courses/enroll/<int:course_id>/', enroll_course_view, name='enroll_course'),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin/create-course/', admin_create_course, name='admin_create_course'),
]
