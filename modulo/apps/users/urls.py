from django.urls import path
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.RegistroUsuario, name='register'),
    path('administrator', login_required(views.administrator, 'modulo:index', '/users/login') , name='administrator'),
    path('student', login_required(views.student, 'modulo:index', '/users/login'), name='student'),
    path('teacher', login_required(views.teacher, 'modulo:index', '/users/login'), name='teacher'),
    path('supervisor', login_required(views.supervisor, 'modulo:index', '/users/login'), name='supervisor'),
    path('logout', LogoutView.as_view(template_name='modulo/index.html'), name='logout'),
    path('courses',  login_required(views.courses, 'modulo:index', '/users/login') , name='courses'),
    path('create-course', login_required(views.CreateCourse.as_view(), 'modulo:index', '/users/login') , name ='create-course'),
    path('update-course/<int:pk>/',login_required(views.UpdateCourse.as_view(), 'modulo:index', '/users/login')  , name='update-course'),
    path('delete-course/<int:pk>/', login_required(views.DeleteCourse.as_view(), 'modulo:index', '/users/login') , name='delete-course'),
    path('users', login_required(views.users,'modulo:index', '/users/login'),  name='users'),
    path('create-user', login_required(views.CreateUser.as_view(), 'modulo:index', '/users/login') , name='create-course'),
    path('update-user/<int:pk>/', login_required(views.UpdateUser.as_view(), 'modulo:index', '/users/login') , name='update-course'),
    path('delete-user/<int:pk>/', login_required(views.DeleteUser.as_view(), 'modulo:index', '/users/login') , name='delete-course'),
    path('types', login_required(views.types, 'modulo:index', '/users/login'), name='types'),
    path('create-type', login_required(views.CreateTypeUser.as_view(), 'modulo:index', '/users/login'), name='create-type'),
    path('update-type/<int:pk>/', login_required(views.UpdateUserType.as_view(), 'modulo:index', '/users/login'), name='update-type'),
    path('delete-type/<int:pk>/', login_required(views.DeleteType.as_view(), 'modulo:index', '/users/login'), name='delete-type'),
    path('assign-course', login_required(views.assigncourse, 'modulo:index', '/users/login'), name='assign-course'),
    path('delete-assign/<int:pk>/', login_required(views.DeleteAssign.as_view(), 'modulo:index', '/users/login'), name='delete-assign'),
    path('assistance-course/<int:pk>/', login_required(views.assistance_course, 'modulo:index', '/users/login'), name='assitance-course'),
    path('create-assistance/<int:pk>/', login_required(views.create_assistance, 'modulo:index', '/users/login'), name='create-assistance'),
    path('assistences-students/<int:pk>/', login_required(views.assistences_students, 'modulo:index', '/users/login'), name='assistences_students'),
    path('groups', login_required(views.groups, 'modulo:index', '/users/login'), name='groups'),
    path('create-group', login_required(views.create_group, 'modulo:index', '/users/login'), name='create-group'),
    path('persons/<int:pk>/', login_required(views.persons, 'modulo:index', '/users/login'), name='persons'),
    path('faces/<int:pk>/', login_required(views.faces, 'modulo:index', '/users/login'), name='faces'),
]
