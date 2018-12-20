from django.shortcuts import render
from ..users.models import *
# Create your views here.
def login(request):
    print('login')