from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class Teacher(models.Model):
    is_teacher = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    email = models.EmailField(max_length=50,blank=True,unique=True)
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    phone_number = models.CharField(max_length=20,blank=True)
    department = models.CharField(max_length=20,blank=True)
    noc = models.IntegerField(default=0)
    def __str__(self):
        return self.first_name

class Student(models.Model):
    is_student = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    email = models.EmailField(max_length=50,blank=True,unique=True)
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    phone_number = models.CharField(max_length=20,blank=True)
    department = models.CharField(max_length=20,blank=True)
    roll_number = models.CharField(max_length=10,blank=True)
    qr_code = models.ImageField(upload_to='QR_Codes', blank=True)
    noc =  models.IntegerField(default=0)

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.email)
        fname = f'qr_code-{self.email}.png'
        buffer = BytesIO()
        qrcode_img.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        qrcode_img.close()
        super().save(*args, **kwargs)


class attendance(models.Model):
    Student_id = models.EmailField(max_length=50)
    def __str__(self):
        return self.Student_id

