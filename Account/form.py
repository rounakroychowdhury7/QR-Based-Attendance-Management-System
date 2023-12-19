from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, fields
from django.db import transaction
from .models import User,Teacher, Student,attendance

class TeacherSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    department = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.is_active = True
        user.email=self.cleaned_data.get('email')
        user.first_name=self.cleaned_data.get('first_name')
        user.last_name=self.cleaned_data.get('last_name')
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.email=self.cleaned_data.get('email')
        teacher.first_name=self.cleaned_data.get('first_name')
        teacher.last_name=self.cleaned_data.get('last_name')
        teacher.phone_number=self.cleaned_data.get('phone_number')
        teacher.department=self.cleaned_data.get('department')
        teacher.save()
        return user


class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    department = forms.CharField(required=True)
    roll_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.is_active = True
        user.email=self.cleaned_data.get('email')
        user.first_name=self.cleaned_data.get('first_name')
        user.last_name=self.cleaned_data.get('last_name')
        user.save()
        student = Student.objects.create(user=user)
        student.email=self.cleaned_data.get('email')
        student.first_name=self.cleaned_data.get('first_name')
        student.last_name=self.cleaned_data.get('last_name')
        student.phone_number=self.cleaned_data.get('phone_number')
        student.department=self.cleaned_data.get('department')
        student.roll_number=self.cleaned_data.get('roll_number')
        student.save()
        return user



class registerForm(ModelForm):
    class Meta:
        model = attendance
        fields = ['Student_id']


class noc_update(ModelForm):
    noc = forms.IntegerField()
    class Meta:
        model = Student
        fields = ['noc']