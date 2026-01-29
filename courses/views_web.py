from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Course, Enrollment

@login_required
def course_list_view(request):
    courses = Course.objects.filter(is_active=True)
    return render(request, 'courses/course_list.html', {'courses': courses})

@login_required
def enroll_course_view(request, course_id):
    course = Course.objects.get(id=course_id, is_active=True)

    enrollment, created = Enrollment.objects.get_or_create(
        student=request.user,
        course=course
    )

    if created:
        messages.success(request, "Enrolled successfully")
    else:
        messages.info(request, "You are already enrolled")
    
    return redirect('course_list')



def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def admin_create_course(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Course.objects.create(
            title = title,
            description = description
        )
        messages.success(request, "Course created successfully")
        return redirect('admin_dashboard')

    return render(request, 'courses/admin_create_course.html')

@user_passes_test(is_admin)
def admin_dashboard(request):
    courses = Course.objects.all()
    return render(request, 'courses/admin_dashboard.html', {'courses':courses})