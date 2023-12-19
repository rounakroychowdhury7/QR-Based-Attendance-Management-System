from django.contrib.auth import login,authenticate
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import StudentSignUpForm,TeacherSignUpForm,registerForm,noc_update
from django.contrib.auth.forms import AuthenticationForm
from .models import Student, User ,attendance
from django.contrib.auth.decorators import login_required

class teacher_register(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = '../templates/teacher_register.html'
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('t_login')


class student_register(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = '../templates/student_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('s_login')


def teacher_login(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_teacher is True:
                    login(request,user)
                    return redirect('teacher_home')
                else:
                    messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    return render(request, 'teacher_login.html',
    context={'form':AuthenticationForm()})

def student_login(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                if user.is_student is True:
                    login(request,user)
                    return redirect('student_home')
                else:
                    messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    return render(request, 'student_login.html',
    context={'form':AuthenticationForm()})

def student_home(request):
    current_id = request.user.id
    obj = Student.objects.get(user_id=current_id)
    name = "Welcome to"
    context = {
        'name': name,
        'obj' : obj,
    }
    return render(request, 'student_home.html', context)


def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            try:
                demo=form.cleaned_data['Student_id']
                userr=Student.objects.filter(email=demo)
                user1=userr.get(email=demo)
                user_email=user1.email
                temp=user1.noc
                temp=temp+1
                user1.noc=temp
                user1.save()
                if user_email == demo:
                    form.save()
                    return redirect('result')
            except:
                return HttpResponse("Student does not exists")

    else:
        form = registerForm()
    return render(request, 'teacher_home.html')


def result(request):
    return render(request,'result.html')


def all_attendance(request):
    context={
        'attendance': Student.objects.all()
    }
    return render(request,'all_attendance.html',context)

@login_required
def home(request):
    if request.user.is_teacher == True:
        return redirect('teacher_home')
    else:
        return redirect('student_home')

def reset(request):
    stu=Student.objects.all()
    attendance.objects.all().delete()
    for x in stu:
        x.noc=0
        x.save()
    return redirect('all_attendance')

def reset_confirm(request):
    return render(request,'reset_confirm.html')

def about(request):
    return render(request,'about.html')
