from rest_framework import serializers
from .views import *
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = (
            'Licence',
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
            'FKLicenceType'
        )

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'IdCourse',
            'NameCourse',
            'Description',
            'Teacher',
        )

class AssitanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistance
        fields = (
            'IdAssistance',
            'FKIdCourse',
            'Date'
        )

class AssistanceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssistanceList

        fields = (
            'IdAssistanceList',
            'FKLicence',
            'Estate',
            'FKIdAssistance'
        )

