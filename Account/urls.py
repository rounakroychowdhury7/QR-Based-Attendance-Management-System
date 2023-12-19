from django.urls import path
from .import  views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('student_register/',views.student_register.as_view(), name='student_register'),
    path('teacher_register/',views.teacher_register.as_view(), name='teacher_register'),
    path('',views.home, name='home'),
    path('teacher_login/',views.teacher_login, name='t_login'),
    path('student_login/',views.student_login, name='s_login'),
    path('teacher_home/',views.register, name='teacher_home'),
    path('student_home/',views.student_home, name='student_home'),
    path('result/',views.result, name='result'),
    path('about/',views.about, name='about'),
    path('reset_result_confirm/',views.reset_confirm, name='reset_result_confirm'),
    path('reset_result/',views.reset, name='reset_result'),
    path('all_attendance/',views.all_attendance,name='all_attendance'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)