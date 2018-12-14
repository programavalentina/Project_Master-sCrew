from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from django import forms

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'DPI',
            'Photo',
            'Name1',
            'Name2',
            'Name3',
            'LastName1',
            'LastName2',
            'BirthDate',
            'Email',
            'Phone',
            'FKLicenceType',

        ]
        labels = {
            'username':'Username',
            'DPI':'DPI',
            'Photo':'Photo',
            'Name1':'Name1',
            'Name2': 'Name2',
            'Name3': 'Name3',
            'LastName1': 'LastName',
            'LastName2': 'LastName2',
            'BirthDate': 'BirthDate',
            'Email': 'Email',
            'Phone': 'Phone',
            'FKLicenceType':'FKLicenceType',
        }
        years = [x for x in range(1980, 2019)]
        widgets = {
            'username': widgets.TextInput(attrs={'class': ''}),
            'DPI': widgets.TextInput(),
            'Photo': widgets.FileInput(),
            'Name1': widgets.TextInput(attrs={'class': ''}),
            'Name2': widgets.TextInput(attrs={'class': ''}),
            'Name3': widgets.TextInput(attrs={'class': ''}),
            'LastName1': widgets.TextInput(attrs={'class': ''}),
            'LastName2': widgets.TextInput(attrs={'class': ''}),
            'Email': widgets.TextInput(attrs={'class': ''}),
            'Phone': widgets.TextInput(attrs={'class': ''}),
            'BirthDate': widgets.SelectDateWidget(attrs={'class': ''}, years=years),
            'FKLicenceType ': widgets.Select(attrs={'class': ''}),
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'DPI',
            'Photo',
            'Name1',
            'Name2',
            'Name3',
            'LastName1',
            'LastName2',
            'BirthDate',
            'Email',
            'Phone',
        ]
        labels = {
            'username':'Username',
            'DPI':'DPI',
            'Photo':'Photo',
            'Name1':'Name1',
            'Name2': 'Name2',
            'Name3': 'Name3',
            'LastName1': 'LastName',
            'LastName2': 'LastName2',
            'BirthDate': 'BirthDate',
            'Email': 'Email',
            'Phone': 'Phone',
        }
        years = [x for x in range(1980, 2019)]
        widgets = {
            'username': widgets.TextInput(attrs={'class': ''}),
            'DPI': widgets.TextInput(),
            'Photo':widgets.FileInput(),
            'Name1': widgets.TextInput(attrs={'class': ''}),
            'Name2': widgets.TextInput(attrs={'class': ''}),
            'Name3': widgets.TextInput(attrs={'class': ''}),
            'LastName1': widgets.TextInput(attrs={'class': ''}),
            'LastName2': widgets.TextInput(attrs={'class': ''}),
            'Email': widgets.TextInput(attrs={'class': ''}),
            'Phone': widgets.TextInput(attrs={'class': ''}),
            'BirthDate': widgets.SelectDateWidget(attrs={'class': ''}, years=years),
        }

class LoginForm(forms.Form):
    username = forms.Field(widget=widgets.TextInput(attrs={'class':''}))
    password = forms.Field(widget=widgets.PasswordInput(attrs={'class':''}))

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course

        fields = [

            'NameCourse',
            'Description',
            'Teacher',
        ]
        labels = {
            'NameCourse':'NameCourse',
            'Description': 'Description',
            'Teacher':'Teacher',
        }
        teachers = User.objects.filter(FKLicenceType=7)

        widgets = {
            'NameCourse': widgets.TextInput(attrs={'class': ''}),
            'Description': widgets.TextInput(attrs={'class': ''}),
            'Teacher': widgets.Select(attrs={'class':''}),
        }

class TypeUserForm(forms.ModelForm):
    class Meta:
        model = UserType

        fields = [
            'Description',
        ]

        labels = {
            'Description':'Description',
        }

        widgets = {
            'Description' : widgets.TextInput(attrs={'class': ''}),
        }

class AssignCourseForm(forms.ModelForm):
    class Meta:
        model = ListStudents

        fields = [
            'FKIdCourse',
        ]

        labels = {
            'FKIdCourse':'FKIdCourse',
        }

        widgets = {
            'FKIdCourse' : widgets.Select(attrs={'class': ''}),
        }

class CheckAssistanceForm():
    class Meta:
        model = AssistanceList

        fields = [
            'Estate',
        ]

        labels = {
            'Estate':'Estate',
        }

        widgets = {
            'Estate' : widgets.Select(),
        }
