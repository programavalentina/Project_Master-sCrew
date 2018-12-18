from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .backends import UserAuth
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import *
from .models import *
import cognitive_face as CF

SUBSCRIPTION_KEY = 'KEY...'
BASE_URL = 'https://eastus.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)
CF.Key.set(SUBSCRIPTION_KEY)
# Create your views here.

def RegistroUsuario(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.FKLicenceType = UserType.objects.get(LicenceType=8)
            post.save()
            return redirect('users:login')
        return render(request, 'users/register.html', {'form': form})
    form = RegisterForm
    return render(request, 'users/register.html', {'form':form})

def administrator(request):
    if request.user.FKLicenceType.LicenceType == 8:
        # Estudiante
        return redirect('users:student')
    if request.user.FKLicenceType.LicenceType == 7:
        # Teacher
        return redirect('users:teacher')
    if request.user.FKLicenceType.LicenceType == 6:
        # Supervisor
        return redirect('users:supervisor')
    if request.user.FKLicenceType.LicenceType == 9:
        # Administrador
        return render(request, 'users/administrator.html')
    auth.logout(request)
    return redirect('users:login')

def supervisor(request):
    if request.user.FKLicenceType.LicenceType == 8:
        # Estudiante
        return redirect('users:student')
    if request.user.FKLicenceType.LicenceType == 7:
        # Teacher
        return redirect('users:teacher')
    if request.user.FKLicenceType.LicenceType == 6:
        # Supervisor
        return render(request, 'users/supervisor.html')
    if request.user.FKLicenceType.LicenceType == 9:
        # Administrador
        return redirect('users:administrator')
    auth.logout(request)
    return redirect('users:login')

def teacher(request):
    if request.user.FKLicenceType.LicenceType == 8:
        # Estudiante
        return redirect('users:student')
    if request.user.FKLicenceType.LicenceType == 7:
        # Teacher
        return render(request, 'users/teacher.html')
    if request.user.FKLicenceType.LicenceType == 6:
        # Supervisor
        return redirect('users:teacher')
    if request.user.FKLicenceType.LicenceType == 9:
        # Administrador
        return redirect('users:administrator')
    auth.logout(request)
    return redirect('users:login')

def student(request):
    if request.user.FKLicenceType.LicenceType == 8:
        # Estudiante
        return render(request, 'users/student.html')
    if request.user.FKLicenceType.LicenceType == 7:
        # Teacher
        return redirect('users:teacher')
    if request.user.FKLicenceType.LicenceType == 6:
        # Supervisor
        return redirect('users:supervisor')
    if request.user.FKLicenceType.LicenceType == 9:
        # Administrador
        return redirect('users:administrator')
    auth.logout(request)
    return redirect('users:login')

def login(request):
    error = 0
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print('entro')
            username = request.POST['username']
            password = request.POST['password']
            auth_ = UserAuth()
            user = auth_.authenticate(username=username, password=password)
            if user is not None:
                print("existe")
                auth.login(request, user)
                if user.FKLicenceType.LicenceType == 8:
                    #Estudiante
                    return redirect('users:student')
                if user.FKLicenceType.LicenceType == 7:
                    #Teacher
                    return redirect('users:teacher')
                if user.FKLicenceType.LicenceType == 6:
                    # Supervisor
                    return redirect('users:supervisor')
                if user.FKLicenceType.LicenceType == 9:
                    # Administrador
                    return redirect('users:administrator')
                auth.logout(request)
                return redirect('users:login')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form, 'error':error})


def courses(request):
    if request.user.FKLicenceType.LicenceType == 7:
        courses = Course.objects.filter(Teacher=request.user.Licence)
        return render(request, 'users/courses.html', {'courses': courses})
    elif request.user.FKLicenceType.LicenceType == 8:
        assgns = ListStudents.objects.filter(FKLicence=request.user.Licence)
        return render(request, 'users/courses.html', {'assigns': assgns})
    elif request.user.FKLicenceType.LicenceType == 9:
        courses = Course.objects.all()
        return render(request, 'users/courses.html', {'courses':courses})
    else:
        return redirect('modulo:index')

class CreateCourse(CreateView):
    model= Course
    template_name = 'users/create_course.html'
    form_class = CourseForm
    success_url = reverse_lazy('users:courses')

class UpdateCourse(UpdateView):
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('users:courses')
    template_name = 'users/update_course.html'

class DeleteCourse(DeleteView):
    model = Course
    success_url = reverse_lazy('users:courses')
    template_name = 'users/delete_course.html'

def users(request):
    users = User.objects.all()
    return render(request, 'users/users.html', {'users':users})

class CreateUser(CreateView):
    model= User
    template_name = 'users/create_user.html'
    form_class = UserForm
    success_url = reverse_lazy('users:users')

class UpdateUser(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:users')
    template_name = 'users/update_user.html'


class DeleteUser(DeleteView):
    model = User
    success_url = reverse_lazy('users:users')
    template_name = 'users/delete_user.html'

class CreateTypeUser(CreateView):
    model = UserType
    form_class = TypeUserForm
    success_url = reverse_lazy('users:types')
    template_name = 'users/create_types.html'

def types(request):
    types = UserType.objects.all()
    return render(request, 'users/types.html', {'types': types})

class UpdateUserType(UpdateView):
    model = UserType
    form_class = TypeUserForm
    template_name = 'users/update_type.html'
    success_url = reverse_lazy('users:types')

class DeleteType(DeleteView):
    model = UserType
    template_name = 'users/delete_type.html'
    success_url = reverse_lazy('users:types')

def assigncourse(request):
    if request.user.FKLicenceType.LicenceType == 8:
        if request.method == 'POST':
            form = AssignCourseForm(request.POST)
            if form.is_valid():
                course = form.cleaned_data['FKIdCourse']
                assign = ListStudents.objects.filter(FKLicence=request.user.Licence, FKIdCourse=course.IdCourse)
                if not assign:
                    post = form.save(commit=False)
                    post.FKLicence = request.user
                    post.save()
                    return redirect('users:courses')
                else:
                    return redirect('users:courses')
            return render(request, 'users/assign_course.html', {'form': form})
        form = AssignCourseForm
        return render(request, 'users/assign_course.html', {'form': form})
    else:
        return redirect('modulo:index')

class DeleteAssign(DeleteView):
    model = ListStudents
    template_name = 'users/delete_assign.html'
    success_url = reverse_lazy('users:courses')

def assistance_course(request, pk):
    assistances = Assistance.objects.filter(FKIdCourse=pk)
    print(assistances)
    return render(request, 'users/assistance_course.html', { 'IdCourse': pk,'assistances':assistances})

def create_assistance(request, pk):
    date = datetime_safe.datetime.now().date()
    print(date)
    assistances = Assistance.objects.filter(Date=date, FKIdCourse = pk)
    print(assistances)
    if not assistances:
        print('Crear Asistencia')
        assistance = Assistance()
        assistance.Date = date
        assistance.FKIdCourse = Course.objects.get(IdCourse=pk)
        assistance.save()
        assigns = ListStudents.objects.filter(FKIdCourse=pk)
        for assign in assigns:
            assistancelist = AssistanceList()
            assistancelist.Estate = False
            assistancelist.FKLicence = assign.FKLicence
            assistancelist.FKIdAssistance = assistance
            assistancelist.save()
            print(assistancelist)
    for assistance in assistances:
        print(assistance.Date)
    return redirect('/users/assistance-course/'+str(pk)+'/')

def assistences_students(request, pk):
    if request.method == 'POST':
        list_of_id_for_action = request.POST.getlist('for_action')
        print(list_of_id_for_action)
        list_of_obj = AssistanceList.objects.filter(IdAssistanceList__in=list_of_id_for_action)
        list_of_obj.update(Estate=True)
    assistencesLists = AssistanceList.objects.filter(FKIdAssistance=pk)
    return render(request, 'users/assistences_students.html', {'IdAssistance':pk,'assistenceLists':assistencesLists})

def groups(request):
    groups = Group.objects.all()
    return render(request, 'users/groups.html', {'groups':groups})

def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            try:
                CF.person_group.create(group.IdGroup, group.Name,group.Description)
                if group.Default:
                    print('Entro')
                    dgroup = Group.objects.get(Default=True)
                    dgroup.Default = False
                    dgroup.save()
                group.save()
                return redirect('users:groups')
            except Exception as e:
                print(e)
    form = GroupForm
    return render(request, 'users/create_group.html', {'form':form})

def persons(request, pk):
    persons = Person.objects.filter(FKGroup=pk)
    return render(request, 'users/persons.html', {'persons':persons})

def faces(request, pk):
    faces = Face.objects.filter(FKPerson=pk)
    return render(request, 'users/faces.html', {'faces':faces})

