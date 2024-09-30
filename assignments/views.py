from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from assignments.models import Assigments

# Create your views here.
def index(request):
    assignments = Assigments.objects.all()
    return render(request, 'index.html', {'assignments': assignments})



def login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request,username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return render(request, 'user.html')
        else:
            return HttpResponse('Invalid login credentials')
    else:
        return render(request, 'login.html')

def post_assignment(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        subject = request.POST.get('subject')
        file = request.FILES['assignment_file']  # Accessing file properly
        posted_by = request.user.username
        print(title, description, subject, file, posted_by)
        
        # Create and save the assignment object
        asg = Assigments.objects.create(
            title=title,
            description=description,
            subject=subject,
            assignment_file=file,  # Ensure the field name matches the model
            posted_by=posted_by
        )
        asg.save()
        return HttpResponse('Assignment posted successfully')
    
    # If it's a GET request, render the form
    return render(request, 'post_assignment.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


def assigments_display(request, course_name):
    assignments = Assigments.objects.filter(subject=course_name)
    return render(request, 'assignments_display.html', {'assignments': assignments})